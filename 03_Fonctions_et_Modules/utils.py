"""
utils.py
Ce fichier est un MODULE. Il contient des fonctions destinées à être importées ailleurs.
"""

import datetime
import os

def get_timestamp():
    """Retourne la date et l'heure actuelles formatées."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def check_disk_usage(path="."):
    """Simule une vérification d'espace disque (pour l'exemple)."""
    # En vrai, on utiliserait shutil.disk_usage(path)
    return "45% Used"

def formater_log(niveau, message):
    """Retourne un message de log formaté."""
    return f"[{get_timestamp()}] [{niveau.upper()}] {message}"

# -----------------------------------------------------------------------------
# Bloc "if __name__ == '__main__'"
# -----------------------------------------------------------------------------
# Ce bloc ne s'exécute QUE si on lance ce fichier directement (python utils.py).
# Il NE s'exécute PAS si on l'importe (import utils).
# C'est l'endroit idéal pour tester ses fonctions.

if __name__ == "__main__":
    print("Test du module utils.py :")
    print(formater_log("info", "Ceci est un test"))
