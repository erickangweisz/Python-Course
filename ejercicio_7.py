import math

# Realiza un programa que reciba una cantidad de minutos y
# muestre por pantalla a cuantas horas y minutos corresponde.

def calculate_and_print_minutes_and_hours_from_minutes():
    input_minutes = float(raw_input('Enter the minutes:\n'))

    hours = (input_minutes / 60)
    rhours = math.floor(hours)
    minutes = (hours - rhours) * 60
    rminutes = round(minutes)

    print str(input_minutes) + ' minutes = ' + str(rhours) + ' hour(s) and ' + str(rminutes) + ' minute(s).'

calculate_and_print_minutes_and_hours_from_minutes()