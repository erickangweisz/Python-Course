# Calcular la media de tres números pedidos por teclado.

def main():
    get_user_input()
    calculate_average()
    print_average()
    
def get_user_input():
    global inputs
    inputs = [float(input('Enter the first number:\n')),
              float(input('Enter the second number:\n')),
              float(input('Enter the thirst number:\n'))]

def calculate_average():
    global average
    average = (inputs[0] + inputs[1] + inputs[2]) / len(inputs)

def print_average():
    print (average)

main()