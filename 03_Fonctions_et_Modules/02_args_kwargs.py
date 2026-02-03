"""
02_args_kwargs.py
Fonctions flexibles avec *args et **kwargs.
Indispensable pour l'écriture de scripts génériques.
"""

print("--- Arguments Avancés ---\n")

# -----------------------------------------------------------------------------
# 1. *args (Arguments Positionnels Multiples)
# -----------------------------------------------------------------------------
# Permet d'accepter un nombre inconnu d'arguments.
# 'args' est un tuple.

def log_messages(prefix, *args):
    print(f"--- Log: {prefix} ---")
    for message in args:
        print(f">> {message}")

# Appel avec 1 message
log_messages("INFO", "Démarrage du script")

# Appel avec 3 messages
log_messages("ERROR", "Fichier introuvable", "Connexion échouée", "Arrêt d'urgence")

# -----------------------------------------------------------------------------
# 2. **kwargs (Arguments Nommés Multiples)
# -----------------------------------------------------------------------------
# Permet d'accepter des arguments clé=valeur inconnus à l'avance.
# 'kwargs' est un dictionnaire.

def creer_utilisateur(username, **kwargs):
    print(f"\nCréation de l'utilisateur : {username}")
    
    # On peut accéder aux infos supplémentaires via kwargs
    if "role" in kwargs:
        print(f"Role défini : {kwargs['role']}")
    
    # Ou tout afficher
    print(f"Métadonnées : {kwargs}")

creer_utilisateur("admin", role="SuperAdmin", active=True, shell="/bin/bash")
creer_utilisateur("guest", active=False)

# -----------------------------------------------------------------------------
# 3. Application : Wrapper de commande
# -----------------------------------------------------------------------------
def executer_commande(cmd, *args, **kwargs):
    print(f"\n[CMD] Exécution de : {cmd}")
    if args:
        print(f"Arguments : {args}")
    if kwargs:
        print(f"Options : {kwargs}")
    
executer_commande("ls", "-l", "-a", color="auto", sort="time")
