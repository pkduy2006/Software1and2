from random import randint, random

three_digit_code = str(random())

a = randint(1, 6)
b = randint(1, 6)
c = randint(1, 6)
d = randint(1, 6)
four_digit_code = str(a) + str(b) + str(c) + str(d)

print(f"3-digit code: {three_digit_code[2:5]}")
print(f"4-digit code: {four_digit_code}")