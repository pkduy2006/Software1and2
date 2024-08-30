import math

x = int(input("Enter a number: "))
y = int(math.sqrt(x))
check = True

for i in range(2, y + 1):
    if x % i == 0:
        check = False
        break

if check and x >= 2:
    print("It is a prime number.")
else:
    print("It is not a prime number.")
