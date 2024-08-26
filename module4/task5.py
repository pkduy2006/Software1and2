username = input("Enter your username: ")
password = input("Enter your password: ")

attempts = 1

while username != 'python' or password != 'rules':
    if attempts == 5:
        print("Access denied.")
        break
    else:
        attempts += 1
        print("Incorrect username or password. Try again.")
        username = input("Enter your username: ")
        password = input("Enter your password: ")

if username == 'python' and password == 'rules':
    print("Welcome!")


