"""
04_cmd.py
Exécuter des commandes système de manière robuste avec subprocess.
"""

import subprocess
import sys

print("--- Commandes Système ---\n")

# -----------------------------------------------------------------------------
# 1. Commande Simple (subprocess.run)
# -----------------------------------------------------------------------------
# Commande 'ping' (cross-platform : -n sous windows, -c sous linux)
param = "-n" if sys.platform == "win32" else "-c"
cmd = ["ping", param, "1", "google.com"]

print(f"Exécution de : {' '.join(cmd)}")

result = subprocess.run(
    cmd,
    capture_output=True, # Capture stdout et stderr
    text=True # Retourne des str (pas des bytes)
)

if result.returncode == 0:
    print("✅ Ping réussi !")
    # print(result.stdout) # Décommenter pour voir la sortie
else:
    print("❌ Echec du ping.")
    print(result.stderr)

# -----------------------------------------------------------------------------
# 2. Gestion des Erreurs
# -----------------------------------------------------------------------------
print("\nTentative de commande inconnue...")
try:
    subprocess.run(["commande_qui_n_existe_pas"], check=True)
except FileNotFoundError:
    print("✅ Erreur attrapée : La commande n'existe pas (Normal).")
except subprocess.CalledProcessError as e:
    print(f"❌ La commande a échoué avec le code {e.returncode}")
