# coding=utf-8
# Pide al usuario dos pares de números x1,y1 y x2,y2, que representen dos puntos en el plano. 
# Calcula y muestra la distancia entre ellos.

class Point():
    x = 0
    y = 0
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print('New Point Created')

user_inputs = []
x_y = ['x', 'y']

def main():
    create_points_with_user_inputs()

def create_points_with_user_inputs():
    __set_user_inputs()
    point_1 = Point(user_inputs[0], user_inputs[1])
    __set_user_inputs()
    point_2 = Point(user_inputs[2], user_inputs[3])

    __calculate_diference_between_two_points(point_1, point_2)

def __set_user_inputs():
    try:
        for index in range(2):
            user_input = float(input('Enter ' + x_y[index] + ' value:\n'))
            user_inputs.append(user_input)
    except Error:
        print (Error)

def __calculate_diference_between_two_points(point_1, point_2):
    x_diference = abs(point_1.x - point_2.x)
    y_diference = abs(point_1.y - point_2.y)

    __print_diference_between_points(x_diference, y_diference)

def __print_diference_between_points(x_diference, y_diference):
    print('Diference in x: ' + str(x_diference) + '\nDiference in y: ' + str(y_diference))

main()