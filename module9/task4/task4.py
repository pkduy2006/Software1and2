import random
from prettytable import PrettyTable
from car import Car

def check():
    for car in cars:
        if car.travelled_distance >= 10000:
            return False
    return True

cars = []

for i in range(10):
    car_maximum_speed = random.randint(100, 200)
    car_registration_number = "ABC-" + str(i + 1)
    cars.append(Car(car_registration_number, car_maximum_speed))

while True:
    for i in range(10):
        random_change_speed = random.randint(-10, 15)
        cars[i].accelerate(random_change_speed)
        cars[i].drive(1)
    if not check():
        break

car_table = PrettyTable(["Registration Number", "Maximum Speed", "Current Speed", "Travelled Distance"])
for i in range(10):
    car_table.add_row([cars[i].registration_number, cars[i].maximum_speed, cars[i].current_speed, cars[i].travelled_distance])

print(car_table)

