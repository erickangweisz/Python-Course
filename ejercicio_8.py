# coding=utf-8
# Un vendedor recibe un sueldo base mas un 10% extra por la
# comisión de sus ventas. El vendedor desea saber cuanto dinero
# obtendrá por concepto de comisiones por las tres ventas que
# realiza en el mes y el total que recibirá en el mes tomando en
# cuenta su sueldo base y comisiones.
PERCENTAGE = 10

def main():
    get_user_input()
    calculate_comissions_to_pay_and_total_amount()
    print_comissions_to_pay_and_total_amount()

def get_user_input():
    global base_salary, number_of_comissions
    base_salary = float(input('Enter base salary:\n'))
    number_of_comissions = float(input('Enter number of comissions:\n'))

def calculate_comissions_to_pay_and_total_amount():
    global comissions_to_pay
    comissions_to_pay = ((base_salary * PERCENTAGE) / 100) * number_of_comissions
    
def print_comissions_to_pay_and_total_amount():
    print ('Comissions to pay: ' + str(comissions_to_pay) + '€')
    print ('Total (base salary + comissions): ' + str(base_salary + comissions_to_pay) + '€')

main()