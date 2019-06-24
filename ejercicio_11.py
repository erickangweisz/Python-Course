# coding=utf-8
# Pide al usuario dos números y muestra la “distancia” entre ellos 
# (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).

def get_distance_between_two_numbers():
    try:
        number_1 = float(input('Enter the first number:\n'))
        number_2 = float(input('Enter the second number:\n'))

        print (abs(number_1 - number_2))
    except:
        print ('Must be a number')

get_distance_between_two_numbers()