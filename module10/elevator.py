class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        self.current_floor += 1
        print(f"Current floor: {self.current_floor}")

    def floor_down(self):
        self.current_floor -= 1
        print(f"Current floor: {self.current_floor}")

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            print("Invalid floor")
            return

        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()