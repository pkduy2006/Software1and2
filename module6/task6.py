import math

def cal_price(d, p):
    price = p / (d * d * math.pi * 10000)
    return price

d1 = float(input("Enter the diameter of the first pizza in centimeters: "))
p1 = float(input("Enter the price of the first pizza in euros: "))
d2 = float(input("Enter the diameter of the second pizza in centimeters: "))
p2 = float(input("Enter the price of the second pizza in euros: "))

st = cal_price(d1, p1)
nd = cal_price(d2, p2)

if st > nd:
    print("The second pizza provides better value for money.")
elif st < nd:
    print("The first pizza provides better value for money.")
else:
    print("Both pizza provide the same value for money.")
