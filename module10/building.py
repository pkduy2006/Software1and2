from elevator import Elevator

class Building:
    def __init__(self, bottom_floor, top_floor, number_of_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.number_of_elevators = number_of_elevators
        self.elevators = []
        for i in range(self.number_of_elevators):
            self.elevators.append(Elevator(self.bottom_floor, self.top_floor))

    def run_elevator(self, num, destination_floor):
        if num < 0 or num > self.number_of_elevators:
            print("Invalid elevator number")
            return
        print(f"The elevator {num} will run.")
        self.elevators[num - 1].go_to_floor(destination_floor)

    def fire_alarm(self):
        print("Fire alarm is on. All elevators will move to the bottom floor.")
        for i, elevator in enumerate(self.elevators):
            print(f"The elevator {i + 1} will move from floor {elevator.current_floor}.")
            elevator.go_to_floor(self.bottom_floor)