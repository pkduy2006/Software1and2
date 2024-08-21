t = input('Enter talents:\n')
p = input('\nEnter pounds:\n')
l = input('\nEnter lots:\n')

grams = float(l) * 13.3
grams += float(p) * 32 * 13.3
grams += float(t) * 20 * 32 * 13.3
kilograms = int(grams / 1000)
grams -= kilograms * 1000

print(f"\nThe weight in modern units:\n{kilograms} kilograms and {grams:<.2f} grams.")

