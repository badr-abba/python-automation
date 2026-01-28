"""
01_syntaxe.py
Introduction à la syntaxe de base de Python.
"""

# -----------------------------------------------------------------------------
# 1. Commentaires
# -----------------------------------------------------------------------------
# Ceci est un commentaire sur une seule ligne.

"""
Ceci est un commentaire sur plusieurs lignes (Docstring).
Il est souvent utilisé pour documenter ce que fait un script ou une fonction.
"""

print("--- 1. Commentaires & Print ---")
print("Bienvenue dans le cours d'automatisation Python !")

# -----------------------------------------------------------------------------
# 2. Indentation
# -----------------------------------------------------------------------------
print("\n--- 2. Indentation ---")
# En Python, les blocs de code sont définis par l'indentation (généralement 4 espaces).
# Il n'y a pas d'accolades {} comme en C, Java ou JS pour les blocs.

utilisateur_connecte = True

if utilisateur_connecte:
    # Ce bloc est exécuté si la condition est vraie
    print("✅ L'utilisateur est connecté.")
    print("   On peut exécuter plusieurs lignes dans ce bloc.")
else:
    # Ce bloc est exécuté si la condition est fausse
    print("❌ L'utilisateur n'est pas connecté.")

# -----------------------------------------------------------------------------
# 3. Convention de nommage (Snake Case)
# -----------------------------------------------------------------------------
# En Python, on utilise le snake_case pour les variables et les fonctions.
# MAJUSCULES pour les constantes.

MA_CONSTANTE = 42
ma_variable_locale = "test"

print(f"\nUne constante : {MA_CONSTANTE}")
