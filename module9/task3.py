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

    def drive(self, hours):
        self.travelled_distance += hours * self.current_speed
        return

print("Please fill in the details of the new car.")
regis_num = input("First, enter the registration number: ")
max_speed = int(input("Then, enter the maximum speed in kilometers per hour: "))
new_car = Car(regis_num, max_speed)
print("Details of the registered car: ")
print(f"- Registration number: {new_car.registration_number}")
print(f"- Maximum speed: {new_car.maximum_speed} km/h.")
print(f"- Current speed: {new_car.current_speed} km/h.")
print(f"- Travelled distance: {new_car.travelled_distance} km.")

change = input("Enter the change of speed in kilometers per hour or press 'Enter' to stop: ")
while change != '':
    new_car.accelerate(change)
    print(f"The current speed of the car is {new_car.current_speed} km/h.")
    change = input("Enter the change of speed or press 'Enter' to move to the next part: ")
print(f"The final speed of the car is {new_car.current_speed} km/h.")

num_of_hours = float(input("Enter the number of hours that you want to drive in constant speed: "))
new_car.travelled_distance = 2000
new_car.drive(num_of_hours)
print(f"The travelled distance of the car is {new_car.travelled_distance:<.1f} km.")

