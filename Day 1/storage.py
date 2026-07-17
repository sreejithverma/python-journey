import json

def load():
    try:
        with open("success_data.json", "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []

def save(data):
    with open("success_data.json", "w") as file:
        json.dump(data, file)



