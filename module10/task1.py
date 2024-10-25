from elevator import Elevator

elevator1 = Elevator(1, 5)
print(f"Current floor: {elevator1.current_floor}")
wanted_floor = int(input("Enter the floor you want to go: "))
elevator1.go_to_floor(wanted_floor)
elevator1.go_to_floor(elevator1.bottom_floor)
