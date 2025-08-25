print("1-Coffee")
print("2-Tea")
print("3-Chocolate")

choice = int(input("Choose a drink: "))
coin = float(input("Enter a coin: "))

if choice == 1 and coin >= 0.5:
    print("You can take the coffee")
else:
    print("You can't take the coffee")

if choice == 2 and coin >= 1:
    print("You can take the Tea")
else:
    print("You can't take the Tea")

if choice == 3 and coin >= 2:
    print("You can take the Chocolate")
else:
    print("You can't take the Chocolate")