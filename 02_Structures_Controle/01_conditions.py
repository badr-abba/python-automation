"""
01_conditions.py
Maîtriser les décisions avec if, elif, else et les opérateurs logiques.
"""

print("--- Conditions et Décisions ---\n")

# -----------------------------------------------------------------------------
# 1. Conditions Multiples (elif)
# -----------------------------------------------------------------------------
status_code = 404

if status_code == 200:
    print("✅ Requête réussie (200 OK)")
elif status_code == 404:
    print("❌ Ressource introuvable (404 Not Found)")
elif status_code == 500:
    print("🔥 Erreur serveur (500 Internal Server Error)")
else:
    print(f"⚠️ Code inconnu : {status_code}")

# -----------------------------------------------------------------------------
# 2. Opérateurs Logiques (and, or, not)
# -----------------------------------------------------------------------------
user_is_admin = True
maintenance_mode = False

# Si l'utilisateur est admin OU que le site n'est PAS en maintenance
if user_is_admin or not maintenance_mode:
    print("\nAccès autorisé au panneau de configuration.")
else:
    print("\nAccès refusé.")

# -----------------------------------------------------------------------------
# 3. Vérification de présence (in)
# -----------------------------------------------------------------------------
allowed_users = ["alice", "bob", "charlie"]
current_user = "david"

if current_user in allowed_users:
    print(f"Bienvenue {current_user}")
else:
    print(f"\nAlert : {current_user} n'est pas autorisé !")

# -----------------------------------------------------------------------------
# 4. Valeurs "Truthiness"
# -----------------------------------------------------------------------------
# En Python, les listes vides, chaînes vides, 0, et None sont considérés comme False.
liste_vide = []
nom_vide = ""

if not liste_vide:
    print("\nLa liste est vide (Pythonic way to check).")

if nom_vide:
    print("Ce message ne s'affichera pas.")
else:
    print("Le nom est vide.")
