# data_loader.py
import pandas as pd
import parametres

def charger_donnees(chemin_fichier='destinations.csv'):
    """
    Charge les données depuis le fichier CSV.
    """
    try:
        df = pd.read_csv(chemin_fichier, sep=',', encoding='utf-8')
        print("Données chargées avec succès.")
        return df
    except FileNotFoundError:
        print(f"Erreur : Le fichier {chemin_fichier} est introuvable. Vérifiez le nom et l'emplacement.")
        return None
    except Exception as e:
        print(f"Erreur inattendue lors du chargement : {e}")
        return None

def obtenir_parametres():
    """
    Retourne un dictionnaire contenant tous les paramètres de décision.
    Vos camarades pourront utiliser cette fonction pour récupérer les poids et les seuils.
    """
    return {
        "poids": parametres.POIDS,
        "a_minimiser": parametres.A_MINIMISER,
        "seuils_q": parametres.SEUILS_INDIFF_Q,
        "seuils_p": parametres.SEUILS_PREF_P,
        "seuils_v": parametres.SEUILS_VETO_V
    }

if __name__ == "__main__":
    # Test d'exécution en local
    print("Test du module data_loader...")
    donnees = charger_donnees()
    if donnees is not None:
        print("\nAperçu des données :")
        print(donnees.head())
        
        params = obtenir_parametres()
        print("\nPoids chargés depuis parametres.py :", params["poids"])
