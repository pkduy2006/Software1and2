numbers = []

while True:
    x = input("Enter a number or press 'Enter' to quit: ")
    if x == '':
        break
    numbers.append(int(x))

numbers.sort(reverse = True)
print(f"The 5 greatest numbers: {numbers[0:5]}.")
