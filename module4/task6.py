total = int(input("Enter the number of random points that you want to generate: "))

n = 0
N = 0

while N < total:
    x = float(input("Enter the value of x_coordinate: "))
    y = float(input("Enter the value of y_coordinate: "))
    N += 1
    if x ** 2 + y ** 2 < 1:
        n += 1

print(f"The approximation of pi is {4 * n / N:.2f}")
