class Elevator:
    def __init__ (self, bottom_floor, current_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = current_floor

    def floor_up(self):
        return self.current_floor + 1

    def floor_down(self):
        return self.current_floor - 1

    def go_to_floor(self, mark_of_elevator, wanted_floor):
        while self.current_floor < wanted_floor:
            self.current_floor = self.floor_up()
            print(f"Elevator {mark_of_elevator + 1} is on the floor {self.current_floor}.")
        while self.current_floor > wanted_floor:
            self.current_floor = self.floor_down()
            print(f"Elevator {mark_of_elevator + 1} is on the floor {self.current_floor}.")

class Building:
    def __init__(self, bottom_floor, top_floor, number_of_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.number_of_elevators = number_of_elevators
        self.elevators = []
        for i in range(number_of_elevators):
            self.elevators.append(Elevator(self.bottom_floor, self.bottom_floor, self.top_floor))

    def run_elevator(self, mark_of_elevator, destination_floor):
        print(f"Elevator {mark_of_elevator + 1} is in the floor {self.elevators[mark_of_elevator].current_floor}.")
        self.elevators[mark_of_elevator].go_to_floor(mark_of_elevator, destination_floor)

    def fire_alarm(self):
        print("Fire alarm is on. All elevators will be closed and gone to the bottom floor.")
        for i, elevator in enumerate(self.elevators):
            elevator.go_to_floor(i, self.bottom_floor)
            print(f"Elevator {i + 1} is in the bottom floor.")

Karaportti2 = Building(1, 7, 3)
Karaportti2.run_elevator(2, 5)
Karaportti2.run_elevator(0, 6)
Karaportti2.run_elevator(1, 7)
Karaportti2.fire_alarm()

