# Dados dos números, mostrar la suma, resta, división y
# multiplicación de ambos.

def calculate_and_print_operations_with_two_numbers()
    number_a = float(raw_input('Enter first number:\n'))
    number_b = float(raw_input('Enter second number:\n'))

    result = number_a + number_b
    print 'Sum result:', result

    result = number_a - number_b
    print 'Subtraction result:', result

    result = number_a / number_b
    print 'Sivision result:', result

    result = number_a * number_b
    print 'Multiplication result:', result

calculate_and_print_operations_with_two_numbers()