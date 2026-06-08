# parametres.py

# Poids des critères dans l'ordre : [Coût, Classement, Distance, Climat, Vie Etudiante]
# Total = 10
POIDS = [3.0, 2.5, 1.5, 1.0, 2.0]

# Objectifs : True si le critère doit être minimisé, False s'il doit être maximisé
A_MINIMISER = [True, True, True, False, False]

# Seuils pour la méthode de surclassement (Electre)
# 0 signifie qu'aucun seuil n'est défini pour ce critère
SEUILS_INDIFF_Q = [50, 10, 0, 0, 0]
SEUILS_PREF_P = [150, 30, 0, 0, 0]
SEUILS_VETO_V = [1600, 0, 8000, 0, 0]
