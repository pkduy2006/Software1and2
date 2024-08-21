number1_str = input("Enter the first number: ")
number2_str = input("Enter the second number: ")
number3_str = input("Enter the third number: ")

number1 = int(number1_str)
number2 = int(number2_str)
number3 = int(number3_str)

print(f"Sum: {number1 + number2 + number3}")
print(f"Product: {number1 * number2 * number3}")
print(f"Average: {(number1 + number2 + number3) / 3:<.1f}")