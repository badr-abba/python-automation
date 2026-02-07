# 📦 Module 5 : Librairies Externes et Web

Python brille par son écosystème. Il y a une librairie pour TOUT. Ce module vous apprend à sortir de la librairie standard.

## 🎯 Objectifs
- Gérer les paquets avec `pip` et les environnements virtuels (`venv`).
- Interagir avec des APIs web (`requests`).
- Extraire des données de pages HTML (`BeautifulSoup`).

## 🛠️ Installation Requise
Avant de lancer les scripts, installez les dépendances :

```bash
# 1. (Optionnel mais recommandé) Créer un environnement virtuel
python -m venv venv
# Windows :
venv\Scripts\activate
# Linux/Mac :
source venv/bin/activate

# 2. Installer les paquets
pip install -r requirements.txt
```

## 📂 Contenu du Module

### 1. Requêtes HTTP (`01_requests.py`)
- Oubliez `urllib`. Utilisez `requests`.
- Faire des appels API (GET, POST).
- Gérer le JSON retourné.

### 2. Web Scraping (`02_scraping.py`)
- Analyser du HTML avec `BeautifulSoup`.
- Cibler des éléments par ID, Classe ou Balise.
- Extraire du texte et des liens.

## ⚠️ Éthique du Scraping
Ne scrapez pas des sites de manière abusive. Respectez le `robots.txt` et ne surchargez pas les serveurs.
