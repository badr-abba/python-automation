"""
03_data.py
Manipulation de formats structurés : JSON et CSV.
"""

import json
import csv

print("--- Données Structurées ---\n")

# -----------------------------------------------------------------------------
# 1. JSON (JavaScript Object Notation)
# -----------------------------------------------------------------------------
data = {
    "serveur": "prod-01",
    "ip": "10.0.0.1",
    "services": ["nginx", "postgresql", "redis"],
    "uptime": 99.9
}

json_file = "config.json"

# Sauvegarde (Dump)
with open(json_file, "w") as f:
    json.dump(data, f, indent=4) # indent=4 pour que ce soit lisible
print(f"✅ JSON sauvegardé dans {json_file}")

# Lecture (Load)
with open(json_file, "r") as f:
    loaded_data = json.load(f)
    print(f"Chargé depuis JSON : IP = {loaded_data['ip']}")

# -----------------------------------------------------------------------------
# 2. CSV (Comma Separated Values)
# -----------------------------------------------------------------------------
csv_file = "utilisateurs.csv"
users = [
    ["Nom", "Role", "Actif"], # Header
    ["Alice", "Admin", "Oui"],
    ["Bob", "Dev", "Non"],
    ["Charlie", "User", "Oui"]
]

# Écriture
with open(csv_file, "w", newline="") as f: # newline="" important sous Windows
    writer = csv.writer(f)
    writer.writerows(users)
print(f"✅ CSV sauvegardé dans {csv_file}")

# Lecture (DictReader est top car il utilise le header comme clés !)
print("\nLecture CSV :")
with open(csv_file, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f" - {row['Nom']} ({row['Role']}) -> Actif: {row['Actif']}")

# Nettoyage
import os
os.remove(json_file)
os.remove(csv_file)
