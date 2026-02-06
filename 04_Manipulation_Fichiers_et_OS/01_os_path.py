"""
01_os_path.py
Interaction avec le système de fichiers.
Comparaison entre 'os' (vieux) et 'pathlib' (moderne).
"""

import os
from pathlib import Path

print("--- Navigation Système ---\n")

# -----------------------------------------------------------------------------
# 1. Utilisation de 'os' (Classique)
# -----------------------------------------------------------------------------
current_dir = os.getcwd() # Get Current Working Directory
print(f"[os] Dossier actuel : {current_dir}")

# Lister les fichiers
files = os.listdir(".")
print(f"[os] Fichiers trouvés : {len(files)}")

# Créer un dossier
new_folder = "temp_os"
if not os.path.exists(new_folder):
    os.mkdir(new_folder)
    print(f"[os] Dossier '{new_folder}' créé.")

# -----------------------------------------------------------------------------
# 2. Utilisation de 'pathlib' (Moderne - Recommandé)
# -----------------------------------------------------------------------------
# Pathlib traite les chemins comme des OBJETS, pas juste des chaînes.
path = Path(".")
print(f"\n[pathlib] Dossier actuel : {path.resolve()}")

# Lister et filtrer (très puissant)
py_files = list(path.glob("*.py"))
print(f"[pathlib] Scripts Python trouvés : {len(py_files)}")

for file in py_files:
    print(f"  -> {file.name} ({file.stat().st_size} octets)")

# Créer un dossier
path_temp = Path("temp_pathlib")
path_temp.mkdir(exist_ok=True) # exist_ok=True évite l'erreur si dossier existe déjà
print(f"[pathlib] Dossier '{path_temp}' vérifié.")

# Nettoyage (suppression des dossiers créés pour l'exemple)
import shutil
shutil.rmtree("temp_os", ignore_errors=True)
path_temp.rmdir()
print("\n[Nettoyage] Dossiers temporaires supprimés.")
