import random
from prettytable import PrettyTable
from car import Car

class Race:
    def __init__(self, name, distance, cars):
        self.distance = distance
        self.name = name
        self.cars = []
        for x, y in cars:
            self.cars.append(Car(x, y))

    def hour_passes(self):
        for car in self.cars:
            change_of_speed = random.randrange(-10, 15)
            car.accelerate(change_of_speed)
            car.drive(1)

    def print_status(self):
        status_table = PrettyTable(["Registration Number", "Maximum Speed", "Current Speed", "Travelled Distance"])
        for i in range(len(self.cars)):
            status_table.add_row([self.cars[i].registration_number, self.cars[i].maximum_speed, self.cars[i].current_speed, self.cars[i].travelled_distance])
        print(status_table)

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False