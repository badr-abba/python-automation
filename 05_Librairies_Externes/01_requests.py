"""
01_requests.py
Interagir avec le Web via le module 'requests'.
C'est le module standard de facto pour le HTTP en Python.
"""

import requests
import json

print("--- Requêtes HTTP avec Requests ---\n")

# URL de test (API gratuite JSONPlaceholder)
url = "https://jsonplaceholder.typicode.com/todos/1"

try:
    print(f"Connexion à {url}...")
    response = requests.get(url, timeout=5)
    
    # Vérification du code d'état HTTP
    if response.status_code == 200:
        print("✅ Succès (200 OK)")
        
        # Parsing automatique du JSON
        data = response.json()
        
        print("\n--- Données Reçues ---")
        print(f"ID : {data['id']}")
        print(f"Titre : {data['title']}")
        print(f"Complété : {data['completed']}")
        print("----------------------")
        
    else:
        print(f"❌ Erreur HTTP {response.status_code}")

except requests.exceptions.ConnectionError:
    print("❌ Erreur de connexion (Pas d'internet ?)")
except requests.exceptions.Timeout:
    print("❌ Le serveur met trop de temps à répondre.")
except Exception as e:
    print(f"❌ Erreur inattendue : {e}")

# -----------------------------------------------------------------------------
# Simulation de POST (Envoi de données)
# -----------------------------------------------------------------------------
print("\n--- Simulation d'envoi de données (POST) ---")
post_url = "https://jsonplaceholder.typicode.com/posts"
payload = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

try:
    # On envoie un dictionnaire, requests le convertit en JSON automatiquement
    resp_post = requests.post(post_url, json=payload)
    
    if resp_post.status_code == 201: # 201 Created
        print(f"✅ Objet créé ! ID retourné : {resp_post.json()['id']}")
    else:
        print(f"⚠️ Code retour : {resp_post.status_code}")

except Exception as e:
    print(f"Erreur durant le POST : {e}")
