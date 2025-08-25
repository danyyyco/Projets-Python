def ask_for_number():
    while True:
        try:
            number = float(input("Please enter a number: "))
            return number
        except ValueError:
            print("That's not a valid number. Please try again.")

entered_number = ask_for_number()
print(f"You entered the number: {entered_number}")
