# Test data 1
data = {
    "data": [
        {"country": "Belgium", "capital": "Brussels"},
        {"country": "Netherlands", "capital": "Amsterdam"},
        {"country": "Australia", "capital": "Sydney"},
        {"country": "Austria", "capital": "Vienna"},
        {"country": "Germany", "capital": "Berlin"}
    ]
}

# Test data 2
data2 = {
    "data": [
        {"country": "Belgium", "capital": "Brussels"},
        {"country": "Netherlands", "capital": "Amsterdam"},
        {"country": "Netherlands", "capital": "Rotterdam"},
        {"country": "Australia", "capital": "Sydney"},
        {"country": "Austria", "capital": "Vienna"},
        {"country": "Germany", "capital": "Berlin"}
    ]
}

def custom_sort(item, sort_keys):
    sort_values = []
    for key in sort_keys:
        if key.startswith('-'):
            sort_values.append(-sum(ord(c) for c in item[key[1:]]))
        else:
            sort_values.append(item[key])
        print(sort_values)
    return tuple(sort_values)

def sortData(data,sort_key):
    reverse = sort_key.startswith('-')
    sort_keys = sort_key.lstrip('-').split(',')

    sorted_data = sorted(data["data"], key=lambda x: custom_sort(x, sort_keys), reverse=reverse)

    return sorted_data

sorted_data = sortData(data, "country")
print(sorted_data)
sorted_data = sortData(data, "-country")
print(sorted_data)
sorted_data = sortData(data2, "country,-capital")
print(sorted_data)