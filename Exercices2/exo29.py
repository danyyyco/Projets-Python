def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed"


num1 = 2
num2 = 5

print("Addition", add(num1, num2))
print("Soustraction", substract(num1, num2))
print("Multiplication", multiply(num1, num2))
print("Division", divide(num1, num2))