numbers = []

def calculate_sum(y):
    total = 0
    for i in y:
        total += i

    return total


x = input("Enter a number or press 'Enter' to calculate the sum: ")
while x != "":
    numbers.append(int(x))
    x = input("Enter a number or press 'Enter' to calculate the sum: ")

print(f"The sum of the list: {calculate_sum(numbers)}")