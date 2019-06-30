# coding=utf-8
# Realizar un algoritmo que lea un número que muestre su raíz
# cuadrada y su raíz cúbica. Python3 no tiene ninguna función
# predefinida que permita calcular la raíz cúbica, ¿Cómo se puede
# calcular?

import math

def main():
    get_user_input()
    __calculate_square_root(user_input)
    __calculate_cube_root(user_input)

def get_user_input():
    global user_input 
    user_input = int(input('Enter a number to calculate square and cube root:'))

def __calculate_square_root(number):
    user_input = math.sqrt(number)
    print (user_input)

def __calculate_cube_root(number):
    user_input = number**(1/3)
    print (user_input)

main()