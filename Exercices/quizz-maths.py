import random

def quizz_maths():
    n1 = random.randint(1,10)
    n2 = random.randint(1,10)
    
    operation = random.choice(["+", "-", "*", "/"])
    
    if operation == "+":
         n1 + n2
    
    elif operation == "-":
         n1 - n2
    
    elif operation == "*":
         n1 * n2
    
    else:
         n1 / n2
    
    return n1, n2, 
    
def question():
    pass
    
print ("=== Bienvenue au quizz de maths ===")
print("Des operations mathematiques vous seront affichées et vous vous devez de trouver la réponse correcte")

manche = 5
i = 1

while manche > 0:
   