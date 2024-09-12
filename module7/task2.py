names = set({})

name = input("Enter a name or press 'Enter' to quit: ")

while name != '':
    if name in names:
        print("Existing name.")
    else:
        print("New name.")
        names.add(name)
    name = input("Enter a name or press 'Enter' to quit: ")

for x in names:
    print(x)