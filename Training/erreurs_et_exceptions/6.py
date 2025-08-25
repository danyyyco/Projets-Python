file = input("Enter a file name: ")

try:
    with open(file, "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("Erreur: File not found")