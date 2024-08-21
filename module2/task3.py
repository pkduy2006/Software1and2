l = input("Please enter the length of the rectangle: ")
w = input("Please enter the width of the rectangle: ")

#p = float(l) + float(w)
#p *= 2;
#print(f"Perimeter: {p}")
#print("Perimeter: " + str(p))

print(f"Perimeter: {(float(l) + float(w)) * 2:<.1f}")
print(f"Area: {float(l) * float(w):<.1f}")