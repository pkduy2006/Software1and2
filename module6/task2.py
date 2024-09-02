import random

sides = int(input("Enter the number of sides: "))

def random_dice_roll():
    result = random.randint(1, sides)
    return result

x = random_dice_roll()

while x != sides:
    print(x)
    x = random_dice_roll()

print(x)
