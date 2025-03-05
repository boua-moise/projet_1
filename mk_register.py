import json
import os

file_name = "bd.json"

def register(email: str, password: str):
    if os.path.exists(file_name):
        with open(file_name, "r+") as f:
            data = json.load(f)
            data["users"].append({"email": email, "password": password, "role": "USER"})
            json.dump(data, f, indent=4)
    else:
        with open(file_name, "w") as f:
            data = {"users": [{"email": email, "password": password, "role": "USER"}]}
            json.dump(data, f, indent=4)
    
    print("Inscription réussie !")
