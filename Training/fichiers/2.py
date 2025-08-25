path = r"C:\Users\dimit\Documents\villes.txt"

town1 = input("Enter a town name: ")
town2 = input("Enter a town name: ")
town3 = input("Enter a town name: ")

with open(path, "a+") as file:
    file.write(f"{town1}")
    file.write(f"\n{town2}")
    file.write(f"\n{town3}")
    file.seek(0)
    content = file.read()
    print(content)