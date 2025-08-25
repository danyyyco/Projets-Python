#double = lambda n: n*2
#result = double(3)
#print(result)

#number = int(input("Enter a number: "))
#result = double(number)
#print(result)

numbers = []
for i in range(6):
    number = int(input("Enter a number: "))
    numbers.append(number)
print(numbers)

sup10 = list(filter(lambda i: i > 10, numbers))
print(sup10)

map_list = list(map(lambda i: i*2, sup10))
print(map_list)