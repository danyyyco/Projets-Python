myList = list()
for i in range(3):
    fruit = input("Entre un fruit: ")
    myList.append(fruit)
myList.sort()
print(myList)
myList.remove("ananas")
print(myList)