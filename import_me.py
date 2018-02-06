def password():
    print("What is Your Name?")
    username = input("Username: ")
    if username == "Rowan":
        print("What is your password?")
        password = input("Password: ")
        if password == "Jackson":
            print("Welcome")
        else:
            print("Incorrect")
    else:
        print("Access Denied")