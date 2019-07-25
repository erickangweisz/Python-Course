# coding=utf-8
# Dos vehículos viajan a diferentes velocidades (speed_vehicle_1 y speed_vehicle_2) y están
# distanciados por una distancia d. El que está detrás viaja a una
# velocidad mayor. Se pide hacer un algoritmo para ingresar la
# distancia entre los dos vehículos (km) y sus respectivas
# velocidades (km/h) y con esto determinar y mostrar en que
# tiempo (minutos) alcanzará el vehículo más rápido al otro.

def main():
    get_speed_of_vehicles()
    get_distance_between_vehicles()
    calculate_time_to_reach_the_slowest_vehicle()
    print_the_time_to_reach_the_slowest_vehicle()

def get_speed_of_vehicles():
    global speed_vehicle_1, speed_vehicle_2
    try:
        speed_vehicle_1 = float(input('Enter speed of vehicle A: '))
        speed_vehicle_2 = float(input('Enter speed of vehicle B: '))
    except ValueError:
        print("That's not a number!")

def get_distance_between_vehicles():
    global distance
    distance = float(input('Enter distance between vehicles (km): '))

def calculate_time_to_reach_the_slowest_vehicle():
    global time
    time = distance / (speed_vehicle_1 - speed_vehicle_2)
    time = time * 60

def print_the_time_to_reach_the_slowest_vehicle_in_minutes():
    print ('Reaches it in', round(time, 2), 'minutes.')

main()