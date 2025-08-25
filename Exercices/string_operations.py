def reverseString(string):
    return string[::-1]


def reverseString2(string):
    str_list = list(string)
    str_list.reverse()
    return "".join(str_list)


def count_vowels(sentence):
    vowels = "aeiou"
    vowelsCount = 0
    words = sentence.split()

    for word in words:
        for char in word.lower():
            if char in vowels:
                vowelsCount += 1

    return vowelsCount


def is_palindrome(word):
    word = word.lower()
    if word == word[::-1]:
        return True
    else:
        return False


def is_palindrome(text):
    text = "".join(char.lower() for char in text if char.isalnum())
    return text == text [ : :- 1]

input_text = input("Enter a string: ")
if is_palindrome(input_text) :
    print(f'"{input_text}" is a palindrome. ')
else:
    print(f'"{input_text}" is not a palindrome. ')