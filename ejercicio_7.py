import math

# Realiza un programa que reciba una cantidad de minutos y
# muestre por pantalla a cuantas horas y minutos corresponde.

def main():
    get_user_input()
    calculate_minutes_and_hours_from_minutes()
    print_minutes_and_hours_from_minutes()

def get_user_input():
    global input_minutes
    input_minutes = float(input('Enter the minutes:\n'))

def calculate_minutes_and_hours_from_minutes():
    global hours, rhours, minutes, rminutes
    hours = (input_minutes / 60)
    rhours = math.floor(hours)
    minutes = (hours - rhours) * 60
    rminutes = round(minutes)

def print_minutes_and_hours_from_minutes():
    print (str(input_minutes) + ' minutes = ' + str(rhours) + ' hour(s) and ' + str(rminutes) + ' minute(s).')

main()