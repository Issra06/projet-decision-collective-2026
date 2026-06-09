import pandas as pd
from data_loader import charger_donnees, obtenir_parametres

def purger_domines(df, a_min, criteres_actifs):
    """Élimine les villes mathématiquement dominées sur les critères restants."""
    domines = set()
    for i, row_a in df.iterrows():
        if i in domines: continue
        for j, row_b in df.iterrows():
            if i == j or j in domines: continue
            
            a_domine_b = True
            strictement_meilleur = False
            
            for c in criteres_actifs:
                if a_min[c]:
                    if row_a[c] > row_b[c]: a_domine_b = False
                    elif row_a[c] < row_b[c]: strictement_meilleur = True
                else:
                    if row_a[c] < row_b[c]: a_domine_b = False
                    elif row_a[c] > row_b[c]: strictement_meilleur = True
            
            if a_domine_b and strictement_meilleur:
                domines.add(j)
                
    if domines:
        villes_eliminees = df.loc[list(domines), 'Alternative'].tolist()
        print(f"\n[!] Villes éliminées par dominance de Pareto : {', '.join(villes_eliminees)}")
        df = df.drop(index=list(domines)).reset_index(drop=True)
    return df

def evenswap_automatique(df, params):
    poids = params['poids']
    a_min = params['a_minimiser']
    
    critere_ref = 'Coût de la vie mensuel (€) ↓'
    
    
    amplitudes = {c: df[c].max() - df[c].min() for c in poids.keys()}
    
    df_courant = df.copy()
    criteres_actifs = list(poids.keys())
    
    for c in criteres_actifs:
        df_courant[c] = df_courant[c].astype(float)
    
    print("=== ÉTAT INITIAL ===")
    print(df_courant.to_string(index=False))
    
    criteres_a_neutraliser = sorted(
        [c for c in criteres_actifs if c != critere_ref], 
        key=lambda x: poids[x]
    )
    
    for c in criteres_a_neutraliser:
        if len(df_courant) <= 1:
            break 
            
        print(f"\n\n>>> NEUTRALISATION DU CRITÈRE : {c} <<<")
        
        pire_val = df_courant[c].max() if a_min[c] else df_courant[c].min()
        print(f"Alignement de toutes les villes sur la pire valeur : {pire_val}")
        
        for idx, row in df_courant.iterrows():
            val_actuelle = row[c]
        
            perte = (pire_val - val_actuelle) if a_min[c] else (val_actuelle - pire_val)
            
            if perte > 0:
                ratio_echelle = amplitudes[critere_ref] / amplitudes[c] if amplitudes[c] != 0 else 0
                ratio_poids = poids[c] / poids[critere_ref]
                compensation = perte * ratio_echelle * ratio_poids
                
                if a_min[critere_ref]:
                    df_courant.loc[idx, critere_ref] -= compensation 
                else:
                    df_courant.loc[idx, critere_ref] += compensation
                
            
            df_courant.loc[idx, c] = pire_val
            
        df_courant = df_courant.drop(columns=[c])
        criteres_actifs.remove(c)
        df_courant[critere_ref] = df_courant[critere_ref].round(1)
        
        print("\nMatrice après compensation :")
        print(df_courant.to_string(index=False))
        
        df_courant = purger_domines(df_courant, a_min, criteres_actifs)
        
    print("\n\n=== RÉSULTAT FINAL EVEN SWAP ===")
    print(df_courant.to_string(index=False))
    return df_courant

if __name__ == "__main__":
    df = charger_donnees('Destinations.csv')
    params = obtenir_parametres()
    if df is not None and params is not None:
        evenswap_automatique(df, params)