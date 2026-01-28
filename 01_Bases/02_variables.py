"""
02_variables.py
Les types de données fondamentaux et les f-strings.
"""

print("--- Variables et Types ---")

# -----------------------------------------------------------------------------
# 1. Types de base
# -----------------------------------------------------------------------------
nom = "Serveur_Web_01"      # str (chaîne de caractères)
cpu_usage = 45.5            # float (nombre décimal)
ram_gb = 16                 # int (nombre entier)
is_active = True            # bool (booléen)

# Affichage des types
print(f"Type de 'nom': {type(nom)}")
print(f"Type de 'cpu_usage': {type(cpu_usage)}")

# -----------------------------------------------------------------------------
# 2. Casting (Conversion de type)
# -----------------------------------------------------------------------------
# Parfois, on reçoit une chaîne "10" mais on veut faire des maths avec.
valeur_str = "50"
valeur_int = int(valeur_str)
resultat = valeur_int + 10

print(f"\nCasting : '50' + 10 = {resultat}")

# -----------------------------------------------------------------------------
# 3. f-strings (Formatage de chaînes)
# -----------------------------------------------------------------------------
# La méthode moderne (Python 3.6+) pour insérer des variables dans du texte.
print("\n--- f-strings ---")
print(f"Serveur : {nom}")
print(f"CPU : {cpu_usage}% | RAM : {ram_gb} GB")
print(f"Statut : {'Actif' if is_active else 'Inactif'}") # On peut même mettre de la logique !

# Manipulation de chaînes simple
chemin = "/var/log/nginx/access.log"
print(f"\nChemin : {chemin}")
print(f"En majuscules : {chemin.upper()}")
print(f"Remplacer : {chemin.replace('nginx', 'apache')}")
print(f"Dossiers : {chemin.split('/')}")
