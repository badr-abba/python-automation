"""
02_boucles.py
Itérer efficacement avec for et while.
"""

print("--- Boucles et Itérations ---\n")

files = ["data.csv", "image.png", "script.py", "backup.zip"]

# -----------------------------------------------------------------------------
# 1. Boucle FOR (Classique)
# -----------------------------------------------------------------------------
print("--- Analyse de fichiers ---")
for file_name in files:
    if file_name.endswith(".py"):
        print(f"[SCRIPT] {file_name}")
    elif file_name.endswith(".zip"):
        print(f"[ARCHIVE] {file_name}")
    else:
        print(f"[AUTRE] {file_name}")

# -----------------------------------------------------------------------------
# 2. Fonction enumerate()
# -----------------------------------------------------------------------------
# Très utile quand on a besoin de l'index ET de la valeur
print("\n--- Liste numérotée ---")
for index, file_name in enumerate(files, start=1):
    print(f"{index}. {file_name}")

# -----------------------------------------------------------------------------
# 3. Boucle WHILE
# -----------------------------------------------------------------------------
print("\n--- Compte à rebours ---")
count = 3
while count > 0:
    print(f"Lancement dans {count}...")
    count -= 1 # Équivalent à count = count - 1
print("🚀 Décollage !")

# -----------------------------------------------------------------------------
# 4. Break et Continue
# -----------------------------------------------------------------------------
print("\n--- Recherche de 'script.py' ---")
for file_name in files:
    if file_name == "script.py":
        print("✅ script.py trouvé ! On arrête la recherche.")
        break # Sort immédiatement de la boucle
    print(f"Analyse de {file_name}...")

print("\n--- Filtrer les images (Continue) ---")
for file_name in files:
    if not file_name.endswith(".png"):
        continue # Passe directement à l'itération suivante
    print(f"Traitement de l'image : {file_name}")
