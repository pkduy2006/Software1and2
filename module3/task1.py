l = float(input("Enter the length of a zander: "))

if l < 42:
    print("Release the fish.")
    if 40 < l:
        print(f"The caught fish was {42 - l:<.2f} centimeter below the size limit.")
    else:
        print(f"The caught fish was {42 - l:<.2f} centimeters below the size limit.")
else:
    print("Pocket the fish.")

'''def check_fish(fish_l):
    if fish_l < 42:
        return 'Release'
    return 'Keep'

print(check_fish(l) + ' the fish')
'''