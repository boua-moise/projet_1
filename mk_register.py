import json
import os

file_name = "db.json"

def register(email: str, password: str):
    if os.path.exists(file_name):
            data = load_db(file_name)
            data["Users"].append({"email": email, "password": password, "role": "USER"})
            save_db(data, file_name)
    else:
        data = {"users": [{"email": email, "password": password, "role": "USER"}]}
        save_db(data, file_name)

    print("Inscription réussie !")