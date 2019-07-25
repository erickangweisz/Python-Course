import math

# Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

def main():
    get_user_input()
    calculate_hipotenusa()
    print_hipotenusa()

def get_user_input():
    global cateto_a, cateto_b
    cateto_a = float(input('Enter cateto A:\n'))
    cateto_b = float(input('Enter cateto B:\n'))

def calculate_hipotenusa():
    global hipotenusa
    hipotenusa = math.sqrt((cateto_a**2) + (cateto_b**2))

def print_hipotenusa():
    print ('Hipotenusa:', hipotenusa)

main()