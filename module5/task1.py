import random

n = int(input('Enter the number of dice you want to roll: '))
total = 0

for i in range(1, n + 1, 1):
    x = random.randint(1, 6)
    total += x

print(f"The total: {total}")