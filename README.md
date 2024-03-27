# Parking Lot Management System

This project implements a simple parking lot management system using Python with FastAPI and MongoDB. It provides three API endpoints for parking, unparking, and retrieving car information.

## Prerequisites

Before running the application, make sure you have the following installed:

- Python 3.x
- MongoDB

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yamini-vaji/breachlock_backend_assignment
   cd breachlock_backend_assignment
    ```

2. Install the Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Set up the environment variables:

    Create a .env.sample file in the root directory of the project and add the following variables:

    ```plaintext
    PARKING_LOT_SIZE=<parking_lot_size>
    MONGODB_URI=<mongodb_connection_uri>
    ```
    
    NOTE: Replace <mongodb_connection_uri> with the MongoDB connection URI and <parking_lot_size> with the size of the parking lot as required.
   
    Example
      ```plaintext
      PARKING_LOT_SIZE="5"
      MONGODB_URI="mongodb://localhost:27017"
      ```
    
5. Start the MongoDB server:

    Make sure MongoDB is installed and running on your system.

6. Run the FastAPI application:
    ```bash
    uvicorn main:app --reload
    ```
    The application should now be running on http://localhost:8000

## API Endpoints

1. Park a Car

    Endpoint: POST /park/{car_number}

    Description: Parks a car and assigns a slot number to it.

    Request Body: None

    Query Parameters: None

    Example:
    ```bash
    curl -X POST "http://localhost:8000/park/ABC123"
    ```
    Response:
    ```json
    {"slot_number": 1}
    ```

2. Unpark the Car

    Endpoint: DELETE /unpark/{slot_number}

    Description: Unparks the car from the specified slot number.

    Request Body: None

    Query Parameters: None

    Example:
    ```bash
    curl -X DELETE "http://localhost:8000/unpark/1"
    ```
    Response:
    ```json
    {"message": "Car with slot number 1 has been unparked"}
    ```

3. Get Car/Slot Information

    Endpoint: GET /info/

    Description: Retrieves car information based on slot number or car number.

    Request Body: None

    Query Parameters (Either one of the Query parameters is required):

    slotNumber: Slot number of the car (optional)

    carNumber: Number of the car (optional)

    Example 1:
    ```bash
    curl -X GET "http://localhost:8000/info/?slotNumber=1"
    ```
    Response 1:
    ```json
        {"slot_number": 1, "car_number": "ABC123"}
    ```
    Example 2:
    ```bash
    curl -X GET "http://localhost:8000/info/?carNumber=ABC123"
    ```
    Response 2:
    ```json
    {"slot_number": 1, "car_number": "ABC123"}
    ```

## Solution Explanation
1. The solution is implemented using Python with FastAPI for building the web API and MongoDB for data storage.
2. Three API endpoints are provided to handle parking, unparking, and retrieving car information.
3. Environment variables are used to configure MongoDB connection URI and parking lot size.
4. MongoDB is used to store parked car data, and a separate collection is used to maintain a history of parked cars.
5. The application ensures that the parking lot does not exceed its capacity, and it assigns slot numbers sequentially without gaps.

## Sort Data based on sort Key
1. sort_dict.py contains the solution for given program in the interview
