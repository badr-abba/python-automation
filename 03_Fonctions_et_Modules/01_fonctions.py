"""
01_fonctions.py
Bases des fonctions : Définition, paramètres, retours et Type Hinting.
"""

print("--- Les Fonctions ---\n")

# -----------------------------------------------------------------------------
# 1. Fonction Simple
# -----------------------------------------------------------------------------
def dire_bonjour(nom):
    """Affiche un message de bienvenue simple."""
    print(f"Bonjour, {nom} !")

dire_bonjour("Alice")

# -----------------------------------------------------------------------------
# 2. Valeur de Retour et Type Hinting
# -----------------------------------------------------------------------------
# Le Type Hinting (-> int) n'est pas obligatoire mais RECOMMANDÉ pour la clarté.
def additionner(a: int, b: int) -> int:
    """
    Retourne la somme de deux nombres entiers.
    """
    return a + b

resultat = additionner(10, 5)
print(f"10 + 5 = {resultat}")

# -----------------------------------------------------------------------------
# 3. Arguments par Défaut
# -----------------------------------------------------------------------------
# Utile pour donner des valeurs standard (timeout, port, etc.)
def connecter_db(host: str, port: int = 3306, timeout: int = 10):
    print(f"Connexion à {host}:{port} (Timeout: {timeout}s)...")
    # Simulation de connexion...
    return True

# Appel avec valeur par défaut
connecter_db("192.168.1.50")

# Appel en surchargeant la valeur par défaut
connecter_db("localhost", port=5432)

# -----------------------------------------------------------------------------
# 4. Portée des Variables (Scope)
# -----------------------------------------------------------------------------
GLOBAL_VAR = "Je suis visible partout"

def test_scope():
    local_var = "Je suis visible uniquement ici"
    print(GLOBAL_VAR) 
    # print(local_var) # Fonctionne ici

test_scope()
# print(local_var) # ❌ Erreur ! local_var n'existe pas en dehors de la fonction
