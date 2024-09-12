print("Press '1' if you want to enter a new airport.")
print("Press '2' if you want to fetch the information of an existing airport.")
print("Press 'Enter' if you want to quit.")

airport = {}

choice = input("Enter your choice: ")
while choice == "1" or choice == "2":
    if choice == "1":
        ICAO_code = input("First, enter the ICAO code: ")
        name = input("Then, enter the name of the airport: ")
        airport[ICAO_code] = name
        print("The data saved.")
    else:
        existed_ICAO_code = input("Enter the ICAO code of the airport: ")
        if existed_ICAO_code in airport:
            print(f"The name of the airport: {airport[existed_ICAO_code]}.")
        else:
            print("Error. The airport does not exist.")
    choice = input("Enter your choice: ")
print("The programme stopped.")