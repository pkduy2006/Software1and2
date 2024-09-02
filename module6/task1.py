import random

def random_dice_roll():
    result = random.randint(1,6)
    return result

x = random_dice_roll()

while x != 6:
    print(x)
    x = random_dice_roll()
print(x)
