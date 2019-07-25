# Calcular el perímetro y área de un rectángulo dada su base y su altura.

def main():
    get_user_input()
    calculate_and_print_perimeter_and_area_of_rectangle()
    print_petimeter_and_area()

def get_user_input():
    global base
    global height
    base = float(input('Enter the base of the rectangle\n'))
    height = float(input('Enter the height of the rectangle\n'))

def calculate_and_print_perimeter_and_area_of_rectangle():
    global perimeter
    global area
    perimeter = (2*height)+(2*base)
    area = height*base

def print_petimeter_and_area():
    print ('Perimeter:', perimeter)
    print ('Area:', area)

main()