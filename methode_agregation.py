# methode_agregation.py
import pandas as pd

def calculer_somme_ponderee(df, params):
    """
    Applique la normalisation Min-Max et calcule la somme pondérée.
    Retourne un DataFrame avec les scores normalisés et le classement final.
    """
    df_res = df.copy()
    
    poids = params["poids"]
    a_minimiser = params["a_minimiser"]
    
    colonnes_criteres = list(poids.keys())
    somme_poids = sum(poids.values())
    
    # 1. Étape de Normalisation Min-Max
    for critere in colonnes_criteres:
        val_min = df[critere].min()
        val_max = df[critere].max()
        denominateur = val_max - val_min
        
        if denominateur == 0:
            df_res[f"Norm_{critere}"] = 1.0
            continue
            
        if a_minimiser[critere]:
            df_res[f"Norm_{critere}"] = (val_max - df[critere]) / denominateur
        else:
            df_res[f"Norm_{critere}"] = (df[critere] - val_min) / denominateur

    # 2. Étape d'Agrégation (Somme Pondérée)
    df_res["Score_Global"] = 0.0
    for critere in colonnes_criteres:
        df_res["Score_Global"] += df_res[f"Norm_{critere}"] * poids[critere]
        
    df_res["Score_Global"] = df_res["Score_Global"] / somme_poids

    print("\n--- MATRICE NORMALISÉE (Étape intermédiaire) ---")
    colonnes_norm = ["Alternative"] + [col for col in df_res.columns if col.startswith("Norm_")]
    print(df_res[colonnes_norm].round(3))
    
    # 3. Tri pour afficher le classement
    df_res = df_res.sort_values(by="Score_Global", ascending=False).reset_index(drop=True)
    
    return df_res
