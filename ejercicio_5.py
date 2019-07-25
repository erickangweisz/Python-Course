# Escribir un programa que convierta un valor dado en grados
# Fahrenheit a grados Celsius. Recordar que la fórmula para la
# conversión es:
# C = (F-32)*5/9

def main():
    get_user_input()
    convert_fahrenheit_to_celsius_degrees()
    print_celsius_degree()

def get_user_input():
    global fahrenheit 
    fahrenheit = float(input('Enter fahrenheit degrees:\n'))

def convert_fahrenheit_to_celsius_degrees():
    global celsius
    celsius = (fahrenheit-32)*5/9

def print_celsius_degree():
    print ('Celsius degrees:', celsius)

main()