# 🧩 Module 3 : Fonctions et Modularité

Le copier-coller est l'ennemi du développeur. Ce module vous apprend à encapsuler votre code et à l'organiser proprement.

## 🎯 Objectifs
- Créer des fonctions réutilisables et documentées.
- Comprendre les arguments flexibles (`*args`, `**kwargs`).
- Organiser votre projet en modules (`.py`).

## 📂 Contenu du Module

### 1. Les Fonctions (`01_fonctions.py`)
- Définition avec `def`.
- Typage statique (Type Hinting) pour la clarté.
- Arguments par défaut (ex: `timeout=5`).
- Les Docstrings pour la documentation automatique.

### 2. Arguments Avancés (`02_args_kwargs.py`)
- `*args` : Pour passer un nombre illimité d'arguments positionnels.
- `**kwargs` : Pour passer un nombre illimité d'arguments nommés (clé=valeur).
- Indispensable pour créer des wrappers ou des décorateurs.

### 3. Modularité (`utils.py` & `main.py`)
- Séparer la logique métier du script principal.
- Importer ses propres fichiers avec `import`.
- Le bloc magique `if __name__ == "__main__":`.

## 💡 Note sur l'Organisation
Au début, tout mettre dans un seul fichier est tentant. Dès que votre script dépasse 100 lignes, pensez à le découper en modules !
