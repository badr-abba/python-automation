"""
03_structures.py
Les structures de données essentielles : Listes, Dictionnaires, Tuples, Sets.
"""

print("--- Structures de Données ---\n")

# -----------------------------------------------------------------------------
# 1. Listes (Lists)
# -----------------------------------------------------------------------------
# Ordonnées, modifiables, autorisent les doublons.
serveurs = ["srv-01", "srv-02", "srv-03"]
print(f"Liste initiale : {serveurs}")

# Ajouter
serveurs.append("srv-04")
# Accéder (Index 0)
print(f"Premier serveur : {serveurs[0]}")
# Dernier élément
print(f"Dernier serveur : {serveurs[-1]}")
# Slicing (Sous-liste)
print(f"Les deux premiers : {serveurs[0:2]}")

# -----------------------------------------------------------------------------
# 2. Dictionnaires (Dictionaries)
# -----------------------------------------------------------------------------
# Stockage Clé-Valeur. Très utilisé pour les configurations, JSON, etc.
config = {
    "hostname": "nginx-prod",
    "ip": "192.168.1.10",
    "port": 80,
    "active": True
}

print(f"\nConfig IP : {config['ip']}")

# Méthode .get() plus sûre (évite une erreur si la clé n'existe pas)
version = config.get("version", "default-1.0")
print(f"Version (défaut) : {version}")

# Ajouter/Modifier
config["port"] = 443
print(f"Config mise à jour : {config}")

# -----------------------------------------------------------------------------
# 3. Tuples
# -----------------------------------------------------------------------------
# Comme des listes, mais IMMUABLES (non modifiables).
# Idéal pour des constantes ou des retours de fonctions multiples.
coords_gps = (48.8566, 2.3522)
# coords_gps[0] = 49.0 # Ceci provoquerait une erreur !
print(f"\nTuple GPS : {coords_gps}")

# -----------------------------------------------------------------------------
# 4. Ensembles (Sets)
# -----------------------------------------------------------------------------
# Non ordonnés, PAS de doublons. Idéal pour dédoublonner des listes.
ips_logs = ["10.0.0.1", "10.0.0.2", "10.0.0.1", "10.0.0.3"]
ips_uniques = set(ips_logs)
print(f"\nIPs uniques : {ips_uniques}")
