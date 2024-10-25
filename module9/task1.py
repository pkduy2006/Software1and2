from car import Car

print("Please fill in the details of the new car.")
car_registration_number = input("First, enter the registration number of the new car: ")
car_maximum_speed = int(input("Then enter the maximum speed of the car in kilometers per hour: "))
car = Car(car_registration_number, car_maximum_speed)

print(f"""Details of the registered car: 
Registration number: {car.registration_number}
Maximum speed: {car.maximum_speed} km/h
Current speed: {car.current_speed} km/h
Travelled distance: {car.travelled_distance} km""")