# 💾 Module 4 : Manipulation Système et Fichiers

C'est ici que Python remplace vos scripts Bash. Nous allons interagir avec le système de fichiers, lire/écrire des données et exécuter des commandes système.

## 🎯 Objectifs
- Naviguer dans les dossiers (`os`, `pathlib`).
- Manipuler des fichiers Texte, JSON et CSV.
- Lancer des commandes Shell depuis Python (`subprocess`).

## 📂 Contenu du Module

### 1. Navigation et OS (`01_os_path.py`)
- Différence entre le vieux `os.path` et le moderne `pathlib`.
- Créer, supprimer et lister des fichiers/dossiers.

### 2. Lecture et Écriture (`02_fichiers.py`)
- Le context manager `with open(...)` (Indispensable !).
- Modes d'ouverture : `r` (lecture), `w` (écriture/écrasement), `a` (ajout).

### 3. Données Structurées (`03_data.py`)
- **JSON** : Le standard du web.
- **CSV** : Le standard de la Data.
- Parsing et génération.

### 4. Exécution de Commandes (`04_cmd.py`)
- Oubliez `os.system`.
- Utilisez `subprocess.run` pour lancer `ls`, `ping`, `git`, etc. et récupérer le résultat proprement.

## ⚠️ Attention
Manipuler des fichiers peut écraser des données. Faites toujours des sauvegardes avant de lancer vos scripts destructeurs !
