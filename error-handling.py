while True:
    try:
        user_input = int(input("Enter any number to continue: "))
    except ValueError:
        print("Input must be a number from 1-9: ")
    else:
        print("Thank you, entry successful!")