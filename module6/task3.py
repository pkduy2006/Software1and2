def convert_gallons_to_litres(x):
    result = x * 3.785411784
    return result

x = float(input("Enter the volume in gallons or a negative value to quit: "))
while x >= 0:
    print(f"The volume in litre: {convert_gallons_to_litres(x):<.2f}")
    x = float(input("Enter the volume in gallons or a negative value to quit: "))
