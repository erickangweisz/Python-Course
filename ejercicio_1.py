# Escribir un programa que pregunte al usuario su nombre, y luego
# lo salude.

def main():
    get_user_input()
    print_name()

def get_user_input():
    global name
    name = input('Hello!, What`s your name?\n')

def print_name():
    print ('Hello ' + name)

main()