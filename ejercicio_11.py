# coding=utf-8
# Pide al usuario dos números y muestra la “distancia” entre ellos 
# (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).

def main():
    get_user_input()

def get_user_input():
    try:
        number_1 = float(input('Enter the first number:\n'))
        number_2 = float(input('Enter the second number:\n'))
    except:
        print ('Must be a number')

def calculate_distance_between_two_numbers():
    global final_number
    final_number = abs(number_1 - number_2)

def print_calculate_distance_between_two_numbers():
    print (final_number)

main()