from car import Car

print("Please fill in the details of the new car.")
car_registration_number = input("First, enter the registration number: ")
car_maximum_speed = int(input("Then, enter the maximum speed in kilometers per hour: "))
car = Car(car_registration_number, car_maximum_speed)
print(f"""Details of the registered car: 
Registration number: {car_registration_number}
Maximum speed: {car_maximum_speed} km/h
Current speed: {car.current_speed} km/h
Travelled distance: {car.travelled_distance} km""")

change = input("Enter the change of speed in kilometers per hour or press 'Enter' to stop change: ")
while change != "":
    car.accelerate(int(change))
    print(f"The current speed of the car is {car.current_speed} km/h.")
    change = input("Enter the change of speed or press 'Enter' to stop change: ")
print(f"The final speed of the car is {car.current_speed} km/h.")

num_of_hours = float(input("Enter the number of hours that you want to drive in the current speed: "))
car.drive(num_of_hours)
print(f"The travelled distance of the car is {car.travelled_distance:<.1f} km.")

