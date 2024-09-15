import json

# Python data (could be a dictionary or list)
data = {
    'name': 'John Doe',
    'age': 30,
    'city': 'New York'
}

# Open a file and write the JSON data
with open('output.json', 'w') as file:
    json.dump(data, file, indent=4)  # indent=4 makes the JSON output pretty

print("Data written to output.json")

# Open the file and load the JSON data
