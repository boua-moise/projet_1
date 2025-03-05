import json

def load_db(file):
    """Charge les utilisateurs depuis le fichier JSON."""
    with open(file, "r") as f:
        return json.load(f)

def save_db(data, file):
    """Sauvegarde les données dans le fichier JSON."""
    with open(file, "w") as file:
        json.dump(data, file, indent=4)



def list_users(file):
    """Affiche la liste des utilisateurs enregistrés."""
    bd_content = load_db(file)  # On charge les données du fichier JSON
    users = bd_content.get("Users", [])  # On récupère la liste des utilisateurs

    if not users:  # Si la liste est vide
        print("Aucun utilisateur enregistré.")
        return

    print("Liste des utilisateurs :")
    for user in users:  # On parcourt chaque utilisateur
        print(f"Email: {user['email']}, Rôle: {user['role']}")  # On affiche son email et son rôle

