import random
from prettytable import PrettyTable

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_of_speed):
        if int(change_of_speed) >= 0:
            self.current_speed = min(self.current_speed + int(change_of_speed), self.maximum_speed)
        else:
            self.current_speed = max(self.current_speed + int(change_of_speed), 0)

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

def check():
    for car in cars:
        if car.travelled_distance >= 10000:
            return False
    return True

cars = []
cnt = 0

for i in range(10):
    car_maximum_speed = random.randrange(100, 200)
    cnt += 1
    car_registration_number = "ABC-" + str(cnt)
    cars.append(Car(car_registration_number, car_maximum_speed))
    #print(f"The current car has the registration number: {cars[i - 1].registration_number} and maximum speed: {cars[i - 1].maximum_speed} km/h.")

while True:
    for i in range(10):
        random_change_speed = random.randrange(-10, 15)
        cars[i].accelerate(random_change_speed)
        cars[i].drive(1)
        #print(f"{i}: {cars[i].current_speed}, {cars[i].travelled_distance}")
    if check() == False:
        break

car_table = PrettyTable(["Registration Number", "Maximum Speed", "Current Speed", "Travelled Distance"])
for i in range(10):
    car_table.add_row([cars[i].registration_number, cars[i].maximum_speed, cars[i].current_speed, cars[i].travelled_distance])

print(car_table)

