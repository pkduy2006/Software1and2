t = float(input('Enter talents:\n'))
p = float(input('\nEnter pounds:\n'))
l = float(input('\nEnter lots:\n'))

grams = l * 13.3
grams += p * 32 * 13.3
grams += t * 20 * 32 * 13.3
kilograms = int(grams // 1000)
grams %= 1000

print(f"\nThe weight in modern units:\n{kilograms} kilograms and {grams:<.2f} grams.")

