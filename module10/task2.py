class Elevator:
    def __init__ (self, bottom_floor, current_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = current_floor

    def floor_up(self):
        if self.current_floor + 1 == 1:
            print("You are in the 1st floor.")
        elif self.current_floor + 1 == 2:
            print("You are in the 2nd floor.")
        elif self.current_floor + 1 == 3:
            print("You are in the 3rd floor.")
        else:
            print(f"You are in the {self.current_floor + 1}th floor.")
        return self.current_floor + 1

    def floor_down(self):
        if self.current_floor - 1 == 1:
            print("You are in the 1st floor.")
        elif self.current_floor - 1 == 2:
            print("You are in the 2nd floor.")
        elif self.current_floor - 1 == 3:
            print("You are in the 3rd floor.")
        else:
            print(f"You are in the {self.current_floor - 1}th floor.")
        return self.current_floor - 1

    def go_to_floor(self, wanted_floor):
        while self.current_floor < wanted_floor:
            self.current_floor = self.floor_up()
        while self.current_floor > wanted_floor:
            self.current_floor = self.floor_down()

class Building:
    def __init__(self, bottom_floor, top_floor, number_of_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.number_of_elevators = number_of_elevators
        self.elevators = []
        for i in range(number_of_elevators):
            self.elevators.append(Elevator(self.bottom_floor, self.bottom_floor, self.top_floor))

    def run_elevator(self, mark_of_elevator, destination_floor):
        self.elevators[mark_of_elevator].go_to_floor(destination_floor)

Karaportti2 = Building(1, 7, 3)
Karaportti2.run_elevator(2, 5)

