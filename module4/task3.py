x = input('Enter a number: ')
largest_num = float(x)
smallest_num = float(x)

while x != '':
    if largest_num < float(x):
        largest_num = float(x)
    if smallest_num > float(x):
        smallest_num = float(x)
    x = input('Enter a number: ')

print(f'The largest number is {largest_num}')
print(f'The smallest number is {smallest_num}')

