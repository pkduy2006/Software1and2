import random

a = random.randint(0, 9)
b = random.randint(0, 9)
c = random.randint(0, 9)
three_digit_code = str(a) + str(b) + str(c)

a = random.randint(1, 6)
b = random.randint(1, 6)
c = random.randint(1, 6)
d = random.randint(1, 6)
four_digit_code = str(a) + str(b) + str(c) + str(d)

print(f"3-digit code: {three_digit_code}")
print(f"4-digit code: {four_digit_code}")