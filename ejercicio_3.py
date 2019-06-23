import math

# Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

def calculate_and_print_hipotenusa():
    cateto_a = float(raw_input('Enter cateto A:\n'))
    cateto_b = float(raw_input('Enter cateto B:\n'))

    hipotenusa = math.sqrt((cateto_a**2) + (cateto_b**2))

    print 'Hipotenusa:', hipotenusa

calculate_and_print_hipotenusa()