"""
main.py
Ce script est le POINT D'ENTRÉE. Il utilise les fonctions définies dans utils.py.
"""

# Méthode 1 : Import entier
import utils

# Méthode 2 : Import spécifique
from utils import formater_log

print("--- Démarrage du Programme Principal ---\n")

# Utilisation via le module importé
print(f"Espace disque : {utils.check_disk_usage()}")

# Utilisation directe de la fonction importée
msg = formater_log("success", "Le module a été chargé correctement.")
print(msg)

print("\n--- Fin ---")
