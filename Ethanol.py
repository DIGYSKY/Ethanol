# By Lilyan CHAUVEAU 
# 15/01/2024
# Version : 1.2.3
# Python 3

# GNU GENERAL PUBLIC LICENSE

#                        Version 3, 29 June 2007

# Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
# Everyone is permitted to copy and distribute verbatim copies
# of this license document, but changing it is not allowed.
# See the LICENSE file

# Algorithm to calculate the injection pressure required according to an ethanol percentage

import math
from colorama import init, Fore, Back, Style

init()

def fuel_pressure(ethanol_percentage=None, pressure=None, additional_percentage=None, Print=False):
    # y0 function for the additional ethanol percentage
    y0 = lambda x: 2.09853E-12*x**6 - 4.97437E-10*x**5 + 4.95509E-08*x**4 - 2.23183E-06*x**3 + 6.72588E-05*x**2 + 8.12361E-04*x + 1.00186E+00
    
    if ethanol_percentage is not None:
        # Calcul de la quantité additionnelle (y0 * 80)
        additional_quantity = y0(ethanol_percentage) * 80
        if Print:
            print(Fore.GREEN + f"Pourcentage additionnel : {round(additional_quantity/80*100-100, 2)}%" + Fore.RESET)

        # Fonction y2 pour la pression de carburant
        y2 = lambda x: 0.5083 * (math.exp(0.0219 * x))
        
        # Calcul de la pression de carburant
        pressure = y2(additional_quantity)
        
        return round(pressure, 2)
        
    elif additional_percentage is not None:
        # Calcul du pourcentage d'éthanol correspondant à la quantité additionnelle
        additional_quantity = (additional_percentage + 100) / 100 * 80
        ethanol_percentage = additional_quantity / y0(1)  # Utilise y0(1) pour inverser le calcul
    
        # Fonction y2 pour la pression de carburant
        y2 = lambda x: 0.5083 * (math.exp(0.0219 * x))
        
        # Calcul de la pression de carburant
        pressure = y2(additional_quantity)
        
        return round(pressure, 2)
    
    elif pressure is not None:
        # Use binary search to inverse the relationship
        min_ethanol, max_ethanol = 0, 100
        tolerance = 1e-6  # Tolerance for precision
        
        while max_ethanol - min_ethanol > tolerance:
            mid_ethanol = (min_ethanol + max_ethanol) / 2
            current_pressure = fuel_pressure(ethanol_percentage=mid_ethanol)
            
            if current_pressure < pressure:
                min_ethanol = mid_ethanol
            else:
                max_ethanol = mid_ethanol
        
        return round(mid_ethanol, 2)
    
    else:
        raise ValueError("Please specify the ethanol percentage or pressure.")


print(Fore.RED + Style.BRIGHT + f"By Lilyan CHAUVEAU (DIGYSKY)")
print(Fore.RED + f"Version : 1.2.4")
print(Fore.RED + f" ")
print(Fore.RED + f"GNU GENERAL PUBLIC LICENSE")
print(Fore.RED + f" ")
print(Fore.RED + f"                       Version 3, 29 June 2007")
print(Fore.RED + f" ")
print(Fore.RED + f"Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>")
print(Fore.RED + f"Everyone is permitted to copy and distribute verbatim copies")
print(Fore.RED + f"of this license document, but changing it is not allowed.")
print(Fore.RED + f"See the LICENSE file")
print(Fore.RED + f" ")
print(Fore.GREEN + f"Algorithm to calculate the injection pressure required according to an ethanol percentage")
print(Fore.RESET + Style.RESET_ALL + f" ")

while 1==1:
    # Ask the user to choose between ethanol percentage or pressure
    choice = input("Choose 'e' for ethanol percentage or 'p' for pressure or 'a' for percentage addional | 'q' to exit: ")

    if choice.lower() == 'e':
        ethanol_percentage = float(input("Enter the ethanol percentage: "))
        result = fuel_pressure(ethanol_percentage=ethanol_percentage, Print=True)
        print(Fore.GREEN + f"The fuel pressure for {ethanol_percentage}% ethanol is: {result} bars." + Fore.RESET)
        
    elif choice.lower() == 'p':
        pressure = float(input("Enter the pressure: "))
        result = fuel_pressure(pressure=pressure)
        fuel_pressure(ethanol_percentage=result, Print=True)
        print(Fore.GREEN + f"The ethanol percentage for a pressure of {pressure} bars is: {result}%." + Fore.RESET)

    elif choice.lower() == 'a':
        additional_percentage = float(input("Entrez le pourcentage d'injection additionnel (ex: +25) : "))
        result = fuel_pressure(additional_percentage=additional_percentage, Print=True)
        print(Fore.GREEN + f"The corresponding fuel pressure is : {result} bars." + Fore.RESET)

    elif choice.lower() == 'q':
        break
        
    else:
        print("Invalid choice. Please choose 'e' or 'p'.")
