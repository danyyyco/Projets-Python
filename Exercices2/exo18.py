sentence = input("Enter a sentence: ")

nb_vowels = 0
for char in sentence:
    if char in 'aeiou':
        nb_vowels += 1

print(nb_vowels)