def is_palindrome(word):
    word = word.lower()
    if word == word[::-1]:
        return True
    else:
        return False

input_text = input("Enter a string: ")
if is_palindrome(input_text) :
    print(f'"{input_text}" is a palindrome. ')
else:
    print(f'"{input_text}" is not a palindrome. ')