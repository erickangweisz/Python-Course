# Dados dos números, mostrar la suma, resta, división y
# multiplicación de ambos.

def main():
    get_user_input()
    calculate_operations()
    print_results()

def get_user_input():
    global number_a, number_b
    number_a = float(input('Enter first number:\n'))
    number_b = float(input('Enter second number:\n'))

def calculate_operations():
    global sum_result, substraction_result, division_result, multiplication_result
    sum_result = number_a + number_b
    substraction_result = number_a - number_b
    division_result = result = number_a / number_b
    multiplication_result = number_a * number_b

def print_results():
    print ('Sum result:', sum_result)
    print ('Subtraction result:', substraction_result)
    print ('Division result:', division_result)
    print ('Multiplication result:', multiplication_result)

main()