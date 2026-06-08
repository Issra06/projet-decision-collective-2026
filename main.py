# main.py
from data_loader import charger_donnees, obtenir_parametres
from methode_agregation import calculer_somme_ponderee

# Exécution du processus
donnees_brutes = charger_donnees('destinations.csv')
parametres_decision = obtenir_parametres()

if donnees_brutes is not None and parametres_decision is not None:
    # Appel de la fonction qui implémente la somme pondérée
    resultats_finaux = calculer_somme_ponderee(donnees_brutes, parametres_decision)
    
    print("\n--- CLASSEMENT FINAL : SOMME PONDÉRÉE ---")
    print(resultats_finaux[["Alternative", "Score_Global"]])
