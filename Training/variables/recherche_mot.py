sentence = input("Enter a sentence: ")
words = sentence.split()
search_word = input("Enter a word to search: ")
trouve = 0

for word in words:
    if search_word.lower() in word.lower():
        trouve = 1

if trouve:
    print("True")
else:
    print("False")
