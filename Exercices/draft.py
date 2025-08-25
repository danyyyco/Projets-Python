"""with open("test.text", "r") as file:
    content = file.readlines()
    print(content)

    file.write("Hello here!")
    file.writelines(["Alphonse", "Berthold", "Martin"])"""

    #try:
        #with open("sample.txt", "r") as file:
            #content = file.read()
    #except FileNotFoundError:
        #print("File Not Found!")

chemin = r"C:\Users\dimit\Documents\fichi.txt"

f = open (chemin, "r")
print(f)
f.close()

with open(chemin, "r") as f:
    contenu = repr(f.read())
    print(contenu)

with open(chemin, "r") as f:
    contenu = f.read().splitlines()
    print(contenu)

with open(chemin, "r") as f:
    f.write("no")

with open(chemin, "a") as f:
    f.write("no")
