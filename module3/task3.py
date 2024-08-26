gender = input("First enter your biological gender: ")
hemoglobin_value = int(input("Then enter your hemoglobin value: "))

if gender == "female":
    if hemoglobin_value > 155:
        print("High.")
    elif 117 <= hemoglobin_value <= 155:
        print("Normal.")
    else:
        print("Low.")
else:
    if hemoglobin_value > 167:
        print("High.")
    elif 134 <= hemoglobin_value <= 167:
        print("Normal.")
    else:
        print("Low.")

