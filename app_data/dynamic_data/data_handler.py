import json
import os

DATA_FILE = "test_data.json"

def read_data():
    """Read data from a JSON file."""
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_data(key, value):
    """Save dynamic test data into JSON file."""
    data = read_data()
    data[key] = value
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Saved data: {key} -> {value}")

def get_data(key):
    """Retrieve data by key."""
    data = read_data()
    return data.get(key, None)
