import random

computer_num = random.randint(1, 10)
player_num = int(input('Enter a number between 1 and 10: '))
while True:
    if player_num > computer_num:
        print("Too high")
    elif player_num < computer_num:
        print("Too low")
    else:
        print("Correct")
        break
    player_num = int(input('Enter a number between 1 and 10: '))

