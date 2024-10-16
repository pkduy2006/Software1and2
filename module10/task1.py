class Elevator:
    def __init__ (self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor

    def floor_up(self, current_floor):
        if current_floor + 1 == 1:
            print("You are in the 1st floor.")
        elif current_floor + 1 == 2:
            print("You are in the 2nd floor.")
        elif current_floor + 1 == 3:
            print("You are in the 3rd floor.")
        else:
            print(f"You are in the {current_floor + 1}th floor.")
        return current_floor + 1

    def floor_down(self, current_floor):
        if current_floor - 1 == 1:
            print("You are in the 1st floor.")
        elif current_floor - 1 == 2:
            print("You are in the 2nd floor.")
        elif current_floor - 1 == 3:
            print("You are in the 3rd floor.")
        else:
            print(f"You are in the {current_floor - 1}th floor.")
        return current_floor - 1

    def go_to_floor(self, current_floor, wanted_floor):
        while current_floor < wanted_floor:
            current_floor = self.floor_up(current_floor)
        while current_floor > wanted_floor:
            current_floor = self.floor_down(current_floor)

x = Elevator(1, 5)
print(f"You are in the bottom floor.")
w_floor = int(input("Enter the floor you want to go: "))
x.go_to_floor(x.bottom_floor, w_floor)
x.go_to_floor(w_floor, x.bottom_floor)
