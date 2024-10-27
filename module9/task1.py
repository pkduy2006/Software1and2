from car import Car

print("Please fill in the details of the new car.")
car_registration_number = input("First, enter the registration number of the new car: ")
car_maximum_speed = int(input("Then enter the maximum speed of the car in kilometers per hour: "))
car = Car(car_registration_number, car_maximum_speed)

car.print_details()