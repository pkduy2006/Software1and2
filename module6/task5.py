numbers = []

def eliminate_all_uneven_numbers(a):
    for i in a:
        if i % 2 == 1:
            a.remove(i)

    return a

x = input("Enter a number or press 'Enter' to quit: ")
while x != '':
    numbers.append(int(x))
    x = input("Enter a number or press 'Enter' to quit: ")

print(numbers)
print(eliminate_all_uneven_numbers(numbers))