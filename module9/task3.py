from car import Car

print("Please fill in the details of the new car.")
car_registration_number = input("First, enter the registration number: ")
car_maximum_speed = int(input("Then, enter the maximum speed in kilometers per hour: "))
car = Car(car_registration_number, car_maximum_speed)

car.print_details()

car.travelled_distance = 2000
car.accelerate(60)
car.drive(1.5)

print(f"Travelled distance: {car.travelled_distance:<.1f} km.")

