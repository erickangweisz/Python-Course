# coding=utf-8
# Dado un número de dos cifras, diseñe un algoritmo que permita
# obtener el número invertido. Ejemplo, si se introduce 23 que
# muestre 32.

def main():
    get_user_input()
    if __there_are_two_digits(user_input):
        __change_digits_to_position(user_input)
    else:
        print ('you must enter a number with two digits:')

def get_user_input():
    global user_input 
    user_input = str(input('Enter a number:'))

def __there_are_two_digits(number):
    if len(number) != 2:
        return False
    else:
        return True

def __change_digits_to_position(user_input):
    print (user_input[1] + user_input[0])

main()