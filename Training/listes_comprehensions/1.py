"""result = [i*i for i in range(1,11)]
print(result)

words = ["Hello", "Neverland", "World", "How", "Matrix", "Are", "Really", "You", "?"]
taille = [len(word) for word in words]
print(taille)

chaine = "Bonjour tout le monde!"
ensemble_unique = {caractere for caractere in chaine}
print(ensemble_unique)"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#even_numbers = numbers[::2]
#odd_numbers = numbers[1::2]
#even_numbers = [number%2==0 for number in numbers]
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)
#print(odd_numbers)