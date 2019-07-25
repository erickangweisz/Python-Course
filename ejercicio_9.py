# coding=utf-8
# Una tienda ofrece un descuento del 15% sobre el total de la compra y 
# un cliente desea saber cuanto deberá pagar finalmente por su compra.

PERCENTAGE = 15

def main():
    get_input_user()
    calculate_15_percent_discount_of_purchase()
    print_15_percent_discount_of_purchase()

def get_input_user():
    global total_price
    total_price = float(input('Enter total price of purchase:\n'))

def calculate_15_percent_discount_of_purchase():
    global final_price
    discount = ((total_price * PERCENTAGE) / 100)
    final_price = total_price - discount
    
def print_15_percent_discount_of_purchase():
    print (final_price)

main()