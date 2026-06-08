# parametres.py

# Poids des critères associés aux colonnes exactes du CSV
POIDS = {
    'Cout': 3.0, 
    'Classement_QS': 2.5, 
    'Distance': 1.5, 
    'Climat': 1.0, 
    'Vie_Etudiante': 2.0
}

# Objectifs : True si le critère doit être minimisé, False s'il doit être maximisé
A_MINIMISER = {
    'Cout': True, 
    'Classement_QS': True, 
    'Distance': True, 
    'Climat': False, 
    'Vie_Etudiante': False
}

# Seuils pour la méthode de surclassement (Electre - Membre 2)
# 0 signifie qu'aucun seuil n'est défini pour ce critère
SEUILS_INDIFF_Q = {'Cout': 50, 'Classement_QS': 10, 'Distance': 0, 'Climat': 0, 'Vie_Etudiante': 0}
SEUILS_PREF_P = {'Cout': 150, 'Classement_QS': 30, 'Distance': 0, 'Climat': 0, 'Vie_Etudiante': 0}
SEUILS_VETO_V = {'Cout': 1600, 'Classement_QS': 0, 'Distance': 8000, 'Climat': 0, 'Vie_Etudiante': 0}
