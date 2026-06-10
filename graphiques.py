# generer_graphique.py
import matplotlib.pyplot as plt
import pandas as pd

# Données issues de vos exécutions réelles
villes = ['Montréal', 'Barcelone', 'Londres', 'Tokyo', 'Milan', 'Munich', 'Prague']
scores_sp = [0.6726, 0.6618, 0.6333, 0.6149, 0.5335, 0.5349, 0.4751]
scores_el = [1, 2, 1, 0, 1, -2, -4]
couts_es = [-244.0, -204.6, -100.0, -32.7, 423.2, 747.8, 157.8] 

df = pd.DataFrame({
    'Ville': villes,
    'Somme Pondérée': scores_sp,
    'ELECTRE (Score net)': scores_el,
    'Even Swap (Coût virtuel)': couts_es
})

# Configuration de la figure de style académique (1 ligne, 3 colonnes)
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))

# Panneau 1 : Somme Pondérée (À maximiser)
df_sp = df.sort_values(by='Somme Pondérée', ascending=True)
ax1.barh(df_sp['Ville'], df_sp['Somme Pondérée'], color='#1f77b4', edgecolor='black')
ax1.set_title('1. Somme Pondérée (MAUT)\n[Plus grand = Meilleur]', fontsize=11, fontweight='bold')
ax1.grid(axis='x', linestyle='--', alpha=0.5)

# Panneau 2 : ELECTRE (Score net de duels)
df_el = df.sort_values(by='ELECTRE (Score net)', ascending=True)
ax2.barh(df_el['Ville'], df_el['ELECTRE (Score net)'], color='#2ca02c', edgecolor='black')
ax2.set_title('2. ELECTRE (Flux Net)\n[Plus grand = Meilleur]', fontsize=11, fontweight='bold')
ax2.grid(axis='x', linestyle='--', alpha=0.5)

# Panneau 3 : Even Swap (Coût virtuel final)
df_es = df.sort_values(by='Even Swap (Coût virtuel)', ascending=False) # Inversé pour avoir le coût minimal en haut
ax3.barh(df_es['Ville'], df_es['Even Swap (Coût virtuel)'], color='#d62728', edgecolor='black')
ax3.set_title('3. Even Swap (Coût compensé)\n[Plus bas/négatif = Meilleur]', fontsize=11, fontweight='bold')
ax3.grid(axis='x', linestyle='--', alpha=0.5)

plt.suptitle('Comparaison de la structure de performance selon le paradigme d\'aide à la décision', fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()

# Sauvegarde de l'image
plt.savefig('comparaison_methodes.png', dpi=300, bbox_inches='tight')
print("Le graphique 'comparaison_methodes.png' a été généré avec succès dans votre dossier !")