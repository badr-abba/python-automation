"""
02_monitor.py
PROJET : Surveillance de Prix (Simulation)
DESCRIPTION : Vérifie le prix d'un produit et alerte s'il est sous un seuil.
NOTE : Comme nous n'avons pas de vrai site e-commerce stable à scraper, nous simulons la réponse HTML.
"""

from bs4 import BeautifulSoup
import time
import datetime

# --- CONFIGURATION ---
SEUIL_PRIX = 500.00
PRODUIT_CIBLE = "Console de Jeux NextGen"

# Simulation de HTML récupéré via requests.get(url).text
MOCK_HTML_expensive = """
<div class="product">
    <h1 class="title">Console de Jeux NextGen</h1>
    <span class="price">549.99€</span>
    <span class="stock">En stock</span>
</div>
"""

MOCK_HTML_cheap = """
<div class="product">
    <h1 class="title">Console de Jeux NextGen</h1>
    <span class="price">499.00€</span> <!-- Promo ! -->
    <span class="stock">En stock</span>
</div>
"""

def check_price(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    
    # Extraction
    try:
        title = soup.find("h1", class_="title").text
        price_str = soup.find("span", class_="price").text
        
        # Nettoyage du prix (enlever le € et convertir en float)
        # "549.99€" -> 549.99
        price_clean = float(price_str.replace("€", "").strip())
        
        print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {title} : {price_clean}€")
        
        if price_clean < SEUIL_PRIX:
            send_alert(title, price_clean)
        else:
            print("   -> Prix au-dessus du seuil. On attend...")
            
    except AttributeError:
        print("❌ Impossible de parser la page (Structure HTML changée ?)")

def send_alert(produit, prix):
    print("--------------------------------------------------")
    print(f"🚨 ALERTE BONNE AFFAIRE !")
    print(f"Le {produit} est à {prix}€ (Seuil: {SEUIL_PRIX}€)")
    print("Envoyer email... [Simulation: Email envoyé]")
    print("--------------------------------------------------")

if __name__ == "__main__":
    print(f"--- Surveillance Démarrée (Seuil : {SEUIL_PRIX}€) ---\n")
    
    print("Tentative 1 (Prix normal)...")
    check_price(MOCK_HTML_expensive)
    
    print("\nAttente de 2 secondes...")
    time.sleep(2)
    
    print("\nTentative 2 (Promo !)...")
    check_price(MOCK_HTML_cheap)
