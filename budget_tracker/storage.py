import json 

FILE = "data.json"

# Daten laden
def load_data():
    try: 
        with open(FILE, "r") as f: 
            return json.load(f)
    except: 
        return []

# Daten speichern    
def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)
