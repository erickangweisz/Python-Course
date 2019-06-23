# Calcular la media de tres números pedidos por teclado.

def calculate_and_print_average():
    inputs = [float(raw_input('Enter the first number:\n')),
              float(raw_input('Enter the second number:\n')),
              float(raw_input('Enter the thirst number:\n'))]

    average = (inputs[0] + inputs[1] + inputs[2]) / len(inputs)
    
    print average

calculate_and_print_average()