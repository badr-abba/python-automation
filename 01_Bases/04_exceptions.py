"""
04_exceptions.py
Comment gérer les erreurs proprement avec try/except.
"""

print("--- Gestion des Exceptions ---\n")

# -----------------------------------------------------------------------------
# 1. Exemple simple (Division par zéro)
# -----------------------------------------------------------------------------
valeur_a = 10
valeur_b = 0

try:
    print(f"Tentative de division : {valeur_a} / {valeur_b}")
    resultat = valeur_a / valeur_b
    print(f"Résultat : {resultat}")
except ZeroDivisionError:
    print("❌ Erreur : Division par zéro impossible !")
except Exception as e:
    # Attrape toutes les autres erreurs
    print(f"❌ Erreur inattendue : {e}")

# -----------------------------------------------------------------------------
# 2. Exemple avec Conversion et Finally
# -----------------------------------------------------------------------------
print("\n--- Saisie Utilisateur (Simulation) ---")
user_input = "vingt" # Imaginons que l'utilisateur a tapé ceci au lieu de 20

try:
    nombre = int(user_input)
    print(f"Le nombre est : {nombre}")
except ValueError:
    print(f"❌ Erreur : '{user_input}' n'est pas un nombre valide.")
finally:
    # Le bloc finally s'exécute TOUJOURS, erreur ou pas.
    # Utile pour fermer des fichiers ou des connexions DB.
    print("🔄 Fin du bloc de traitement (Clean-up).")
