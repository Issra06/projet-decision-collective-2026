# main.py
from data_loader import charger_donnees, obtenir_parametres
from methode_agregation import calculer_somme_ponderee
from methode_surclassement import calculer_surclassement_dynamique
from methode_even_swap import evenswap_automatique

print("   LANCEMENT DU SYSTÈME D'AIDE À LA DÉCISION (AMD)    ")

# 1. Chargement des données et des préférences
donnees_brutes = charger_donnees('destinations.csv')
parametres_decision = obtenir_parametres()

if donnees_brutes is not None and parametres_decision is not None:

    # MÉTHODE 1 : SOMME PONDÉRÉE (Agrégation)

    resultats_agregation = calculer_somme_ponderee(donnees_brutes, parametres_decision)
    print("\n" + "="*50)
    print(" 1. RÉSULTATS : SOMME PONDÉRÉE (Méthode Compensatoire)")
    print("="*50)
    print(resultats_agregation[["Alternative", "Score_Global"]])
    gagnant_somme = resultats_agregation.iloc[0]["Alternative"]
    print(f"\n Gagnant (Somme Pondérée) : {gagnant_somme}")


    # MÉTHODE 2 : ELECTRE (Surclassement)

    print("\n" + "="*50)
    print(" 2. RÉSULTATS : ELECTRE (Méthode de Surclassement)")
    print("="*50)
    C, D, S, seuil_final = calculer_surclassement_dynamique(donnees_brutes, parametres_decision)
    print(f"\nMatrice de surclassement finale (Seuil durci à {seuil_final:.2f}) :")
    print(S)
   
    # On calcule le score de flux net : (Nombre de villes surclassées) - (Nombre de fois où elle est surclassée)
    # Le -1 permet de retirer la diagonale (une ville se surclasse elle-même)
    victoires = S.sum(axis=1) - 1
    defaites = S.sum(axis=0) - 1
    score_electre = victoires - defaites
    
    # On trie pour trouver le meilleur score
    classement_electre = score_electre.sort_values(ascending=False)
    gagnant_electre = classement_electre.index[0]
    
    print(f"\nGagnant (Electre) : {gagnant_electre}")
    print(f"Détail : {gagnant_electre} a un score net de {score_electre[gagnant_electre]} duels gagnés")

    # MÉTHODE 3 : EVEN SWAP (Échanges uniformes)

    print("\n" + "="*50)
    print(" 3. RÉSULTATS : EVEN SWAP (Compensation intelligente)")
    print("="*50)
    resultats_evenswap = evenswap_automatique(donnees_brutes, parametres_decision)