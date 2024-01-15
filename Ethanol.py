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

def fuel_pressure(ethanol_percentage=None, pressure=None, Print=False):
    # y0 function for the additional ethanol percentage
    y0 = lambda x: 2.09853E-12*x**6 - 4.97437E-10*x**5 + 4.95509E-08*x**4 - 2.23183E-06*x**3 + 6.72588E-05*x**2 + 8.12361E-04*x + 1.00186E+00
    
    if ethanol_percentage is not None:
        # Calculation of the additional quantity (y0 * 80)
        additional_quantity = y0(ethanol_percentage) * 80
        if Print:
            print(Fore.GREEN + f"Percentage additional: {round(additional_quantity/80*100-100, 2)}%" + Fore.RESET)
        
        # Function y2 for fuel pressure
        y2 = lambda x: 0.5083 * (math.exp(0.0219 * x))
        
        # Calculate fuel pressure
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

while 1==1:
    # Ask the user to choose between ethanol percentage or pressure
    choice = input("Choose 'e' for ethanol percentage or 'p' for pressure: ")

    if choice.lower() == 'e':
        ethanol_percentage = float(input("Enter the ethanol percentage: "))
        result = fuel_pressure(ethanol_percentage=ethanol_percentage, Print=True)
        print(Fore.GREEN + f"The fuel pressure for {ethanol_percentage}% ethanol is: {result} bars." + Fore.RESET)
        
    elif choice.lower() == 'p':
        pressure = float(input("Enter the pressure: "))
        result = fuel_pressure(pressure=pressure)
        fuel_pressure(ethanol_percentage=result, Print=True)
        print(Fore.GREEN + f"The ethanol percentage for a pressure of {pressure} bars is: {result}%." + Fore.RESET)
        
    else:
        print("Invalid choice. Please choose 'e' or 'p'.")
