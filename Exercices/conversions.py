def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
def celsius_to_kelvin(celsius):
    return celsius + 273.15
def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15
def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15 ) * 9/5 + 32

def show_menu():
    print("\n=== MENU CONVERSION ===")
    print("1- celsius to fahrenheit")
    print("2- fahrenheit to celsius")
    print("3- celsius to kelvin")
    print("4- fahrenheit to kelvin")
    print("5- kelvin to celsius")
    print("6- kelvin to fahrenheit")
    print("7- exit")
    
while True:
    show_menu()
    
    try:
        choice = int(input("\nEnter the conversion your choice: "))
    except ValueError:
        print("\nError: invalid choice, please enter between 1,2,3,4,5,6 or 7")
        continue
    
    if choice == 1:
        try:
            number_to_convert = float(input("\nEnter the number you want to convert: "))
            r = celsius_to_fahrenheit(number_to_convert)
            print(f" {number_to_convert}°C = {r}°F ")
        except ValueError:
            print("\nError: the number you enter is not a float number")
        
    elif choice == 2:
        try:
            number_to_convert = float(input("\nEnter the number you want to convert: "))
            r = fahrenheit_to_celsius(number_to_convert)
            print(f" {number_to_convert}°F = {r}°C ")
        except ValueError:
            print("\nError: the number you enter is not a float number")
        
    elif choice == 3:
        try:
            number_to_convert = float(input("\nEnter the number you want to convert: "))
            r = celsius_to_kelvin(number_to_convert)
            print(f" {number_to_convert}°C = {r} K ")
        except ValueError:
            print("\nError: the number you enter is not a float number")
        
    elif choice == 4:
        try:
            number_to_convert = float(input("\nEnter the number you want to convert: "))
            r = fahrenheit_to_kelvin(number_to_convert)
            print(f" {number_to_convert}°F = {r} K ")
        except ValueError:
            print("\nError: the number you enter is not a float number")
        
    elif choice == 5:
        try:
            number_to_convert = float(input("\nEnter the number you want to convert: "))
            r = kelvin_to_celsius(number_to_convert)
            print(f" {number_to_convert} K = {r}°C ")
        except ValueError:
            print("\nError: the number you enter is not a float number")
        
    elif choice == 6:
        try:
            number_to_convert = float(input("\nEnter the number you want to convert: "))
            r = kelvin_to_fahrenheit(number_to_convert)
            print(f" {number_to_convert} K = {r}°F ")
        except ValueError:
            print("\nError: the number you enter is not a float number")
        
    elif choice == 7:
        print("\nGood Bye!")
        break
    
    else:
        print("\nInvalid Choice!")