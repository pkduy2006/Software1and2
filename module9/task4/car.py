class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_of_speed):
        self.current_speed += change_of_speed
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += hours * self.current_speed

    def emergency_brake(self):
        self.accelerate(-200)

    def print_details(self):
        print(f"""Details of the registered car:
Registration number = {self.registration_number}
Maximum speed = {self.maximum_speed} km/h
Current speed = {self.current_speed} km/h
Travelled distance = {self.travelled_distance} km""")
