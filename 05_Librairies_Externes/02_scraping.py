"""
02_scraping.py
Introduction au Web Scraping avec BeautifulSoup.
Pour cet exemple, on parse du HTML local pour éviter de dépendre d'un site web externe changeant.
"""

from bs4 import BeautifulSoup

print("--- Web Scraping (BeautifulSoup) ---\n")

# Simulation d'une page HTML
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Ma Page de Test</title>
</head>
<body>
    <h1>Bienvenue sur le scraper</h1>
    <div class="container">
        <p class="description">Ceci est un paragraphe de description.</p>
        <ul id="items-list">
            <li class="item">Ordinateur - 900€</li>
            <li class="item">Souris - 20€</li>
            <li class="item">Clavier - 50€</li>
        </ul>
        <a href="https://www.python.org" id="link-python">Site Officiel Python</a>
    </div>
</body>
</html>
"""

# Initialisation de la soupe
soup = BeautifulSoup(html_content, "html.parser")

# 1. Récupérer le titre
titre = soup.title.string
print(f"Titre de la page : {titre}")

# 2. Récupérer le H1
h1 = soup.find("h1").text
print(f"H1 : {h1}")

# 3. Récupérer par Classe
print("\n--- Analyse de la classe '.item' ---")
items = soup.find_all("li", class_="item")
for item in items:
    print(f" - Produit trouvé : {item.text}")

# 4. Récupérer un attribut (href d'un lien)
print("\n--- Liens ---")
lien = soup.find("a", id="link-python")
url = lien["href"]
print(f"Lien vers Python : {url}")
