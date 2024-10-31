class Car:
    total_car = 0

    def __init__(self, registration_number, maximum_speed, current_speed, travelled_distance = 0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance
        Car.total_car += 1
        self.car_number = Car.total_car

    def drive(self, hours = 1):
        self.travelled_distance += self.current_speed * hours

    def print_information(self):
        print(f"""{self.car_number}. Registration number: {self.registration_number}
Maximum speed: {self.maximum_speed} km/h
Current speed: {self.current_speed} km/h
Travelled distance: {self.travelled_distance} km""")

class ElectricCar(Car):

    def __init__(self, registration_number, maximum_speed, current_speed, battery_capacity):
        self.battery_capacity = battery_capacity
        super().__init__(registration_number, maximum_speed, current_speed)

    def print_information(self):
        super().print_information()
        print(f"Battery capacity: {self.battery_capacity} kWh")

class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed, current_speed, tank_volume):
        self.tank_volume = tank_volume
        super().__init__(registration_number, maximum_speed, current_speed)

    def print_information(self):
        super().print_information()
        print(f"Tank volume: {self.tank_volume} l")

cars = []
cars.append(ElectricCar('ABC-15', 180, 80, 52.5))
cars.append(GasolineCar('ACD-123', 165, 120, 32.3))
for car in cars:
    car.drive(3)
    car.print_information()