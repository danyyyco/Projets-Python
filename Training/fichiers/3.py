path = r"C:\Users\dimit\Documents\prod.csv"

with open(path, "a+") as file:
    file.write("Nom" "Prix" "Quantité")
    file.seek(0)
    content = file.read()
    print(content)