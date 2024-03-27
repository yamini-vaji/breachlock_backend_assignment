from fastapi import FastAPI, HTTPException, Query
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env.sample file
dotenv_file = ".env.sample"
load_dotenv(dotenv_file)

app = FastAPI()

# MongoDB connection
client = MongoClient(os.getenv("MONGODB_URI"))
db = client["parking_lot"]
collection = db["parked_cars"]

# Get parking lot size from environment variable
parking_lot_size = int(os.getenv("PARKING_LOT_SIZE"))

def get_next_available_slot():
    slots = collection.find().sort("slot", 1)  # Sort by slot number in ascending order
    slot_numbers = [slot["slot"] for slot in slots]
    for i, slot_number in enumerate(slot_numbers, start=1):
        if i != slot_number:
            return i
    return len(slot_numbers) + 1 if slot_numbers else 1

# Endpoint to park a car
@app.post("/park/{car_number}")
def park_car(car_number: str):
    if collection.count_documents({}) >= parking_lot_size:
        raise HTTPException(status_code=400, detail="Parking lot is full")
    
    slot_number = get_next_available_slot()
    collection.insert_one({"slot": slot_number, "car_number": car_number})
    return {"slot_number": slot_number}

# Endpoint to unpark a car
@app.delete("/unpark/{slot_number}")
def unpark_car(slot_number: int):
    car = collection.find_one({"slot": slot_number})
    if not car:
        raise HTTPException(status_code=404, detail="Car not found in the slot")
    
    # Move the parked car to history collection before deleting it
    db["parking_history"].insert_one(car)
    collection.delete_one({"slot": slot_number})
    return {"message": f"Car with slot number {slot_number} has been unparked"}

# Endpoint to get car/slot information
@app.get("/info")
def get_info(slotNumber: int = Query(None, description="Slot number of the car"),
             carNumber: str = Query(None, description="Number of the car")):
    # Check if given query parameter is slotNumber,  if yes then search in the database
    if slotNumber:
        car = collection.find_one({"slot": slotNumber})
        if not car:
            raise HTTPException(status_code=404, detail="Car not found in the slot")
        return {"slot_number": car["slot"], "car_number": car["car_number"]}
    
    # Check if given query parameter is carNumber,  if yes then search in the database
    if carNumber:
        car = collection.find_one({"car_number": carNumber})
        if not car:
            raise HTTPException(status_code=404, detail="Car not found")
        return {"slot_number": car["slot"], "car_number": car["car_number"]}
    
    #  if neither of 2 parameters are given then return 400 Bad Request Error
    raise HTTPException(status_code=400, detail="Please provide either slot number or car number")
