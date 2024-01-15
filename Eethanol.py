# Algorithme permettant de calculer la pression d'injection nécessaire selon un pourcentage d'éthanol
# By Lilyan CHAUVEAU 
# 15/01/2024
# Version : 1.0.0

# GNU GENERAL PUBLIC LICENSE

#                        Version 3, 29 June 2007

# Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
# Everyone is permitted to copy and distribute verbatim copies
# of this license document, but changing it is not allowed.
# See the LICENSE file

import math

def pression_carburant(ethanol_percentage=None, pression=None):
    # Fonction y0 pour le pourcentage d'ethanol supplémentaire
    y0 = lambda x: 2.09853E-12*x**6 - 4.97437E-10*x**5 + 4.95509E-08*x**4 - 2.23183E-06*x**3 + 6.72588E-05*x**2 + 8.12361E-04*x + 1.00186E+00
    
    if ethanol_percentage is not None:
        # Calcul de la quantité additionnelle (y0 * 80)
        quantite_additionnelle = y0(ethanol_percentage) * 80
        
        # Fonction y2 pour la pression de carburant
        y2 = lambda x: 0.5083 * (math.exp(0.0219 * x))
        
        # Calcul de la pression de carburant
        pressure = y2(quantite_additionnelle)
        
        return round(pressure, 2)
    
    elif pression is not None:
        # Utilisation de la recherche binaire pour inverser la relation
        min_ethanol, max_ethanol = 0, 100
        tolerance = 1e-6  # Tolérance pour la précision
        
        while max_ethanol - min_ethanol > tolerance:
            mid_ethanol = (min_ethanol + max_ethanol) / 2
            current_pressure = pression_carburant(ethanol_percentage=mid_ethanol)
            
            if current_pressure < pression:
                min_ethanol = mid_ethanol
            else:
                max_ethanol = mid_ethanol
        
        return round(mid_ethanol, 2)
    
    else:
        raise ValueError("Veuillez spécifier le pourcentage d'éthanol ou la pression.")

# Demander à l'utilisateur de choisir entre pourcentage d'éthanol ou pression
choix = input("Choisissez 'e' pour le pourcentage d'éthanol ou 'p' pour la pression : ")

if choix.lower() == 'e':
    ethanol_percentage = float(input("Entrez le pourcentage d'éthanol : "))
    result = pression_carburant(ethanol_percentage=ethanol_percentage)
    print(f"La pression de carburant pour {ethanol_percentage}% d'éthanol est : {result} bars.")
    
elif choix.lower() == 'p':
    pression = float(input("Entrez la pression : "))
    result = pression_carburant(pression=pression)
    print(f"Le pourcentage d'éthanol pour une pression de {pression} bars est : {result}%.")

else:
    print("Choix invalide. Veuillez choisir 'e' ou 'p'.")
