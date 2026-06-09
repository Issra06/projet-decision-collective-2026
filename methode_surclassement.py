try:
    import pandas as pd  
except ImportError as exc:
    raise ImportError("Pandas is required to run this script. Install it with 'pip install pandas'.") from exc

import numpy as np
from data_loader import charger_donnees, obtenir_parametres

def calculer_matrices_electre(df, params, seuil_concordance):
    """Calcule les matrices C, D et S pour un seuil donné, de manière ultra-optimisée."""
    poids = params["poids"]
    a_min = params["a_minimiser"]
    seuils_q = params["seuils_q"]
    seuils_p = params["seuils_p"]
    seuils_v = params["seuils_v"]

    colonnes_criteres = list(poids.keys())
    somme_poids = sum(poids.values())
    n = len(df)

    matrice_C_np = np.zeros((n, n))
    matrice_D_np = np.zeros((n, n), dtype=bool)

    for critere in colonnes_criteres:
        V = df[critere].values
        w = poids[critere]
        q, p, v = seuils_q[critere], seuils_p[critere], seuils_v[critere]

        if a_min[critere]:
            diff = V[:, None] - V
        else:
            diff = V - V[:, None]

        if p == q:
            c_j = np.where(diff <= q, 1.0, 0.0)
        else:
            c_j = np.where(diff <= q, 1.0, 
                           np.where(diff >= p, 0.0, (p - diff) / (p - q)))

        matrice_C_np += w * c_j

        if v > 0:
            matrice_D_np = np.logical_or(matrice_D_np, diff > v)

    matrice_C_np /= somme_poids
    np.fill_diagonal(matrice_C_np, 1.0)
    np.fill_diagonal(matrice_D_np, False)

    matrice_S_np = (matrice_C_np >= seuil_concordance) & (~matrice_D_np)
    
    return matrice_C_np, matrice_D_np, matrice_S_np

def calculer_surclassement_dynamique(df, params, seuil_initial=0.60, pas=0.02):
    """
    Augmente le seuil de concordance automatiquement tant qu'il y a des indifférences
    (surclassements mutuels entre deux alternatives).
    """
    seuil = seuil_initial
    noms = df["Alternative"].tolist()
    
    while seuil <= 1.0:
        C, D, S = calculer_matrices_electre(df, params, seuil)
        
        
        S_off_diag = S.copy()
        np.fill_diagonal(S_off_diag, False)
        
        
        indifference_mutuelle = S_off_diag & S_off_diag.T
        
        if not np.any(indifference_mutuelle):
            print(f"Stabilité atteinte : aucun surclassement mutuel au seuil de concordance = {seuil:.2f}")
            break
            
        print(f"Indifférence détectée au seuil {seuil:.2f}. Durcissement des critères...")
        seuil += pas
        
    df_C = pd.DataFrame(C.round(3), index=noms, columns=noms)
    df_D = pd.DataFrame(D.astype(int), index=noms, columns=noms)
    df_S = pd.DataFrame(S.astype(int), index=noms, columns=noms)

    return df_C, df_D, df_S, seuil

if __name__ == "__main__":
    df = charger_donnees('Destinations.csv')
    params = obtenir_parametres()
    
    if df is not None and params is not None:
        C, D, S, seuil_final = calculer_surclassement_dynamique(df, params)
        
        print(f"\n--- MATRICE DE SURCLASSEMENT FINALE (Seuil: {seuil_final:.2f}) ---")
        print(S)