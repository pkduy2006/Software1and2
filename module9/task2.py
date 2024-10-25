from car import Car

print("Please fill in the details of the new car.")
car_registration_number = input("First, enter the registration number: ")
car_maximum_speed = int(input("Then, enter the maximum speed in kilometers per hour: "))
car = Car(car_registration_number, car_maximum_speed)
print(f"""Details of the registered car:
Registration number = {car.registration_number}
Maximum speed = {car.maximum_speed} km/h
Current speed = {car.current_speed} km/h
Travelled_distance = {car.travelled_distance} km""")

change = input("Enter the change of speed in kilometers per hour or press 'Enter' to stop change: ")
while change != "":
    car.accelerate(int(change))
    print(f"The current speed of the car is {car.current_speed} km/h.")
    change = input("Enter the change of speed or press 'Enter' to stop change: ")
print(f"The final speed of the car is {car.current_speed} km/h.")
