def math_operations(a,b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b

    return addition, subtraction, multiplication, division

addition, subtraction, multiplication, division = math_operations(1,2)
print(addition)
print(subtraction)
print(multiplication)
print(division)