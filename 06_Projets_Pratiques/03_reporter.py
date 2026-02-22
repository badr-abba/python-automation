"""
03_reporter.py
PROJET : Générateur de Rapports
DESCRIPTION : Lit des données brutes (CSV), calcule des statistiques et génère un rapport.
"""

import csv
from pathlib import Path

DATA_FILE = "ventes.csv"
REPORT_FILE = "rapport_ventes.txt"

def generer_fake_data():
    """Crée un CSV pour l'exercice."""
    data = [
        ["Date", "Produit", "Quantité", "PrixUnitaire"],
        ["2023-10-01", "Laptop", "2", "800"],
        ["2023-10-01", "Souris", "10", "20"],
        ["2023-10-02", "Clavier", "5", "45"],
        ["2023-10-03", "Laptop", "1", "800"],
        ["2023-10-03", "Ecran", "3", "150"]
    ]
    with open(DATA_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
    print(f"✅ Données brutes générées : {DATA_FILE}")

def analyser_donnees():
    total_ventes = 0.0
    produits_vendus = {}
    
    # Lecture
    with open(DATA_FILE, "r") as f:
        reader = csv.DictReader(f)
        rows = list(reader) # On charge tout en mémoire (ok pour petits fichiers)
        
    print(f"\nAnalyse de {len(rows)} transactions...")
    
    for row in rows:
        qte = int(row["Quantité"])
        prix = float(row["PrixUnitaire"])
        montant = qte * prix
        produit = row["Produit"]
        
        # Total global
        total_ventes += montant
        
        # Stats par produit
        if produit in produits_vendus:
            produits_vendus[produit] += qte
        else:
            produits_vendus[produit] = qte

    return total_ventes, produits_vendus

def generer_rapport(total, par_produit):
    lignes = []
    lignes.append("==============================")
    lignes.append("      RAPPORT DE VENTES       ")
    lignes.append("==============================")
    lignes.append(f"Chiffre d'Affaires Total : {total:.2f} €")
    lignes.append("\n--- Détails par Produit ---")
    
    # Trier par quantité décroissante
    sorted_products = sorted(par_produit.items(), key=lambda x: x[1], reverse=True)
    
    for prod, qte in sorted_products:
        lignes.append(f"- {prod} : {qte} unités")
        
    lignes.append("==============================")
    
    print("\n".join(lignes)) # Afficher console
    
    # Sauvegarder fichier
    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lignes))
    
    print(f"\n✅ Rapport sauvegardé sous {REPORT_FILE}")

if __name__ == "__main__":
    generer_fake_data()
    ca, stats = analyser_donnees()
    generer_rapport(ca, stats)
    
    # Nettoyage
    # import os
    # os.remove(DATA_FILE)
