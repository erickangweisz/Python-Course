# coding=utf-8
# Una tienda ofrece un descuento del 15% sobre el total de la compra y 
# un cliente desea saber cuanto deberá pagar finalmente por su compra.

PERCENTAGE = 15

def get_15_percent_discount_of_purchase():
    total_price = float(raw_input('Enter total price of purchase:\n'))
    discount = ((total_price * PERCENTAGE) / 100)
    final_price = total_price - discount
    
    print final_price

get_15_percent_discount_of_purchase()

