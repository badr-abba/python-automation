"""
03_comprehensions.py
La "Pythonic Way" de créer des listes. Concis et puissant.
"""

print("--- List Comprehensions ---\n")

valeurs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Liste originale : {valeurs}")

# -----------------------------------------------------------------------------
# 1. Exemple Classique vs Comprehension
# -----------------------------------------------------------------------------
# Objectif : Créer une liste avec les carrés des nombres (x²)

# Méthode Classique (3-4 lignes)
carres_classique = []
for x in valeurs:
    carres_classique.append(x * x)

# Méthode Comprehension (1 ligne)
# Syntaxe : [ expression for item in iterable ]
carres_comprehension = [x * x for x in valeurs]

print(f"Carrés : {carres_comprehension}")

# -----------------------------------------------------------------------------
# 2. Avec Filtrage (Condition)
# -----------------------------------------------------------------------------
# Objectif : Garder seulement les nombres pairs

# Syntaxe : [ expression for item in iterable if condition ]
pairs = [x for x in valeurs if x % 2 == 0]
print(f"Pairs : {pairs}")

# -----------------------------------------------------------------------------
# 3. Exemple Concret : Nettoyage de données
# -----------------------------------------------------------------------------
raw_users = ["  Alice ", "Bob", "  Charlie  ", "David"]
print(f"\nUtilisateurs bruts : {raw_users}")

# Nettoyer les espaces (strip) et mettre en majuscules (upper)
clean_users = [user.strip().upper() for user in raw_users]
print(f"Utilisateurs propres : {clean_users}")

# -----------------------------------------------------------------------------
# 4. Dictionary Comprehension (Bonus)
# -----------------------------------------------------------------------------
# Créer un dictionnaire {valeur: carré}
dict_carres = {x: x*x for x in range(1, 6)}
print(f"\nDictionnaire de carrés : {dict_carres}")
