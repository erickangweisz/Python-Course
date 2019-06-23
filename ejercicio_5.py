# Escribir un programa que convierta un valor dado en grados
# Fahrenheit a grados Celsius. Recordar que la fórmula para la
# conversión es:
# C = (F-32)*5/9

def convert_and_print_fahrenheit_to_celsius_gradees():
    fahrenheit = float(raw_input('Enter fahrenheit degrees:\n'))
    celsius = (fahrenheit-32)*5/9

    print 'Celsius degrees:', celsius

convert_and_print_fahrenheit_to_celsius_gradees()