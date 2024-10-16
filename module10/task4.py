import random
from prettytable import PrettyTable

class Car:
    def __init__(self, registration_number, maximum_speed, current_speed = 0, travelled_distance = 0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self, change_of_speed):
        if int(change_of_speed) >= 0:
            self.current_speed = min(self.current_speed + int(change_of_speed), self.maximum_speed)
        else:
            self.current_speed = max(self.current_speed + int(change_of_speed), 0)
        return

    def drive(self, hours = 1):
        self.travelled_distance += self.current_speed * hours
        return

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            change_of_speed = random.randrange(-10, 15)
            car.accelerate(change_of_speed)
            car.drive()

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

Auto = []
cnt = 0
for i in range(10):
    random_max_speed = random.randrange(100, 200)
    cnt += 1
    regis_num = "ABC-" + str(cnt)
    Auto.append(Car(regis_num, random_max_speed))

GrandDemolitionDerby = Race("Grand Demolition Derby", 8000, Auto)
while GrandDemolitionDerby.race_finished() == False:
    GrandDemolitionDerby.hour_passes()
    GrandDemolitionDerby.print_status()