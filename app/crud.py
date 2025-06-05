import json
from app.models import Fruit

DB_PATH = "app/db.json"

SUPPORTED_FRUITS = {
    "apple": "red",
    "banana": "yellow",
    "orange": "orange",
    "grape": "purple",
    "kiwi": "green",
    "lemon": "yellow",
    "mango": "orange",
    "pear": "green",
    "pineapple": "brown",
    "strawberry": "red"   
    }

def load_db():
    with open(DB_PATH, "r") as file:
        return json.load(file)

def save_db(data):
    with open(DB_PATH, "w") as file:
        json.dump(data, file, indent=4)

def get_all_fruits():
    return load_db()

def get_fruit_by_name(name):
    fruits = load_db()
    for fruit in fruits:
        if fruit["fruit"].lower() == name.lower():
            return fruit
    return None    

def get_fruit_by_id(fruit_id):
    fruits = load_db()
    for fruit in fruits:
        if fruit["id"] == fruit_id:
            return fruit
    return None

def add_fruit(fruit: Fruit):
    fruits = load_db()

    fruit_name = fruit.fruit.lower()
    
    if fruit_name not in SUPPORTED_FRUITS:
        raise ValueError(f"{fruit_name} is not a supported fruit.")
    
    for f in fruits:
        if f["fruit"] == fruit_name:
            f["count"] += 1
            save_db(fruits)
            return f

    new_id =max([f["id"] for f in fruits], default=0) + 1
    new_fruit = {
        "id": new_id,
        "fruit": fruit_name,
        "color": SUPPORTED_FRUITS[fruit_name],
        "count": 1
    }
    fruits.append(new_fruit)
    save_db(fruits)
    return new_fruit