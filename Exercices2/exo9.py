import random

r = random.randint(1,10)

nb_user = int(input("Guess the number between 1 and 10: "))

if nb_user == r:
    print("You guessed right!")
else:
    print("Sorry, You loose!")