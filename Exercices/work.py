from op import *

num1 = 5
num2 = 3

addition = add(num1, num2)
subtraction = sub(num1, num2)
multiplication = mul(num1, num2)
division = div(num1, num2)

print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {mul(num1, num2)}")
print(f"{num1} / {num2} = {div(num1, num2)}")