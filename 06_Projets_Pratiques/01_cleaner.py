"""
01_cleaner.py
PROJET : Nettoyeur de Dossier Automatique
DESCRIPTION : Trie les fichiers d'un dossier source vers des sous-dossiers basés sur l'extension.
"""

import os
import shutil
from pathlib import Path

# --- CONFIGURATION ---
SOURCE_DIR = Path("dossier_a_trier") # Créez ce dossier et mettez y des fichiers pour tester !
EXTENSIONS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Scripts": [".py", ".sh", ".js", ".html"]
}

def setup_simulation():
    """Crée des fichiers bidons pour le test."""
    if not SOURCE_DIR.exists():
        SOURCE_DIR.mkdir()
    
    fichiers_test = ["vacances.jpg", "cv.pdf", "data.zip", "test.py", "rapport.docx"]
    for f in fichiers_test:
        (SOURCE_DIR / f).touch()
    print(f"✅ Fichiers de test créés dans {SOURCE_DIR}")

def trier_fichiers():
    print(f"\n--- Démarrage du tri dans {SOURCE_DIR} ---")
    
    # Vérifier si le dossier source existe
    if not SOURCE_DIR.exists():
        print(f"❌ Le dossier {SOURCE_DIR} n'existe pas.")
        return

    # Parcourir les fichiers
    for file_path in SOURCE_DIR.iterdir():
        if file_path.is_dir():
            continue # Ignorer les dossiers déjà présents
            
        file_ext = file_path.suffix.lower()
        moved = False
        
        # Trouver la catégorie correspondante
        for category, exts in EXTENSIONS.items():
            if file_ext in exts:
                # Créer le dossier cible s'il n'existe pas
                target_dir = SOURCE_DIR / category
                target_dir.mkdir(exist_ok=True)
                
                # Déplacer le fichier
                destination = target_dir / file_path.name
                shutil.move(str(file_path), str(destination))
                print(f"📦 {file_path.name} -> {category}/")
                moved = True
                break
        
        if not moved:
            # Optionnel : Déplacer les autres fichiers dans 'Autres'
            other_dir = SOURCE_DIR / "Autres"
            other_dir.mkdir(exist_ok=True)
            shutil.move(str(file_path), str(other_dir / file_path.name))
            print(f"❓ {file_path.name} -> Autres/")

if __name__ == "__main__":
    setup_simulation() # Pour que le script soit testable immédiatement
    trier_fichiers()
    print("\n✅ Tri terminé.")
