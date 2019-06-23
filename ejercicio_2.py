# Calcular el perímetro y área de un rectángulo dada su base y su altura.

def calculate_and_print_perimeter_and_area_of_rectangle():
    base = float(raw_input('Enter the base of the rectangle\n'))
    height = float(raw_input('Enter the height of the rectangle\n'))

    perimeter = (2*height)+(2*base)
    area = height*base

    print 'Perimeter:', perimeter
    print 'Area:', area

calculate_and_print_perimeter_and_area_of_rectangle()