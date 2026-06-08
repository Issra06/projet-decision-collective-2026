# parametres.py

# Poids des critères associés aux colonnes exactes du CSV
POIDS = {
    'Coût de la vie mensuel (€) ↓': 3.0, 
    'Classement_QS ↓': 2.5, 
    'Distance depuis Paris (km) ↓': 1.5, 
    'Climat (1 à 5) ↑': 1.0, 
    'Qualité de vie étudiante (1 à 5) ↑': 2.0
}

# Objectifs : True si le critère doit être minimisé, False s'il doit être maximisé
A_MINIMISER = {
    'Coût de la vie mensuel (€) ↓': True, 
    'Classement_QS ↓': True, 
    'Distance depuis Paris (km) ↓': True, 
    'Climat (1 à 5) ↑': False, 
    'Qualité de vie étudiante (1 à 5) ↑': False
}

# Seuils pour la méthode de surclassement (Electre - Membre 2)
# 0 signifie qu'aucun seuil n'est défini pour ce critère
SEUILS_INDIFF_Q = {
    'Coût de la vie mensuel (€) ↓': 50, 
    'Classement_QS ↓': 10, 
    'Distance depuis Paris (km) ↓': 0, 
    'Climat (1 à 5) ↑': 0, 
    'Qualité de vie étudiante (1 à 5) ↑': 0
}

SEUILS_PREF_P = {
    'Coût de la vie mensuel (€) ↓': 150, 
    'Classement_QS ↓': 30, 
    'Distance depuis Paris (km) ↓': 0, 
    'Climat (1 à 5) ↑': 0, 
    'Qualité de vie étudiante (1 à 5) ↑': 0
}

SEUILS_VETO_V = {
    'Coût de la vie mensuel (€) ↓': 1600, 
    'Classement_QS ↓': 0, 
    'Distance depuis Paris (km) ↓': 8000, 
    'Climat (1 à 5) ↑': 0, 
    'Qualité de vie étudiante (1 à 5) ↑': 0
}
