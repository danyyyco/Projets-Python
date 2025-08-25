numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

try:
    #print(numbers.index(3))
    print(numbers[17])
except IndexError:
    print("Erreur: Index out of range")