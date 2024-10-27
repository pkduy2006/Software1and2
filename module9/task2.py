from car import Car

print("Please fill in the details of the new car.")
car_registration_number = input("First, enter the registration number: ")
car_maximum_speed = int(input("Then, enter the maximum speed in kilometers per hour: "))
car = Car(car_registration_number, car_maximum_speed)
car.print_details()

car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
car.emergency_brake()
print(f"Final speed: {car.current_speed} km/h.")
