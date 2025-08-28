coordinates = (10,20,30)
x,y,z = coordinates
print(x,y,z)

print(coordinates + (40,))

ingredients = {"flour", "sugar", "butter"}
print(ingredients)

ingredients.add("eggs")
ingredients.remove("sugar")
print(ingredients)

n1 = {1,2,3,4,5}
n2 = {3,7,8,9}

print(n1 | n2)
print(n1 & n2)
print(n1 - n2)
