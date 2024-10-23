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

print("Please fill in the details of the new car.")
car_registration_number = input("First, enter the registration number: ")
car_maximum_speed = int(input("Then, enter the maximum speed in kilometers per hour: "))
car = Car(car_registration_number, car_maximum_speed)
print("Details of the registered car: ")
print(f"- Registration number: {car.registration_number}")
print(f"- Maximum speed: {car.maximum_speed} km/h.")
print(f"- Current speed: {car.current_speed} km/h.")
print(f"- Travelled distance: {car.travelled_distance} km.")

change = input("Enter the change of speed in kilometers per hour: ")
while change != 0:
    car.accelerate(change)
    if car.current_speed == 0:
        print("The car is stopped.")
        break
    print(f"The current speed of the car is {car.current_speed} km/h.")
    change = input("Enter the change of speed: ")
print(f"The final speed of the car is {car.current_speed} km/h.")
