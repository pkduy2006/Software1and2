class Car:
    def __init__(self, registration_number, maximum_speed, current_speed = 0, travelled_distance = 0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

print("Please fill in the details of the new car.")
regis_num = input("First, enter the registration number of the new car: ")
max_speed = int(input("Then enter the maximum speed of the car in kilometers per hour: "))
new_car = Car(regis_num, max_speed)

print("Details of the registered car: ")
print(f"- Registration number: {new_car.registration_number}")
print(f"- Maximum speed: {new_car.maximum_speed} km/h.")
print(f"- Current speed: {new_car.current_speed} km/h.")
print(f"- Travelled distance: {new_car.travelled_distance} km.")