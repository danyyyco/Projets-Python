fruits = ['apple','banana','orange','pineapple', 'strawberry']
print(fruits)
print(fruits[2])

fruits.append('tomato')
print(fruits)

fruits.remove('banana')
print(fruits)

del fruits[4]
print(fruits)

popped_fruits = fruits.pop()
print(popped_fruits)

popped_fruits = fruits.pop(2)
print(popped_fruits)

print(fruits)