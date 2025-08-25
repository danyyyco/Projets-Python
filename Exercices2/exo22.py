def count_frequency(string):
    frequency = {}

    for character in string:
        if character in frequency:
            frequency[character] += 1
        else:
            frequency[character] = 1

    return frequency


string = input("Enter a string: ")
result = count_frequency(string)

print("Character frequency:", result)
