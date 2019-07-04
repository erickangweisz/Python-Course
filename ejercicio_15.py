# coding=utf-8
# Dadas dos variables numéricas A y B, que el usuario debe teclear,
# se pide realizar un algoritmo que intercambie los valores de
# ambas variables y muestre cuanto valen al final las dos variables.

def main():
    get_user_input()
    __change_value_of_variables(variable_a, variable_b)

def get_user_input():
    global variable_a
    global variable_b
    try:
        variable_a = int(input('Enter a value of variable "A": '))
        variable_b = int(input('Enter a value of variable "B": '))
    except ValueError:
        print("That's not an integer!")

def __change_value_of_variables(var_a, var_b):
    variable_a = var_b
    variable_b = var_a
    print ('variable A: ' + str(variable_a) + '\nvariable B: ' + str(variable_b))

main()