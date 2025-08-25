password = "Rai"

nb_test = 0

while nb_test < 3:
    try_password = input("Enter the password: ")
    if password == try_password:
        print("Connection successful")
        break
    nb_test = nb_test + 1

if nb_test == 3:
    print("blocked account")