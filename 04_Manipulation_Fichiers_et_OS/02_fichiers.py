"""
02_fichiers.py
Lecture et écriture de fichiers texte.
Utilisation obligatoire du 'with open()' pour fermer automatiquement le fichier.
"""

filename = "exemple.txt"

print("--- Manipulation de Fichiers ---\n")

# -----------------------------------------------------------------------------
# 1. Écriture (Mode 'w' - Écrase le contenu !)
# -----------------------------------------------------------------------------
print(f"Écriture dans {filename}...")
lines_to_write = [
    "Ligne 1 : Bonjour\n",
    "Ligne 2 : Ceci est un test\n",
    "Ligne 3 : Python est génial\n"
]

with open(filename, "w", encoding="utf-8") as f:
    f.writelines(lines_to_write)
    f.write("Ligne 4 : Fin de l'écriture.\n")

print("✅ Fichier créé.")

# -----------------------------------------------------------------------------
# 2. Lecture (Mode 'r')
# -----------------------------------------------------------------------------
print(f"\nLecture de {filename} :")
with open(filename, "r", encoding="utf-8") as f:
    contenu = f.read()
    print("--- Contenu ---")
    print(contenu)
    print("---------------")

# -----------------------------------------------------------------------------
# 3. Ajout (Mode 'a' - Append)
# -----------------------------------------------------------------------------
print("\nAjout d'une ligne...")
with open(filename, "a", encoding="utf-8") as f:
    f.write(f"Ligne 5 : Ajoutée après coup.\n")

# Vérification rapide
with open(filename, "r") as f:
    print(f"Nombre total de lignes : {len(f.readlines())}")

# Nettoyage
import os
os.remove(filename)
print(f"\n[Nettoyage] {filename} supprimé.")
