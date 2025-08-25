def calcul_average(n1,n2,n3):
    return (n1 + n2 + n3) / 3

def is_admitted(average, min_average, min_grade):
    return average >= min_average and g1>=min_grade  and g2>=min_grade and g3>=min_grade

g1 = float(input("Enter your first grade : "))
g2 = float(input("Enter your second grade : "))
g3 = float(input("Enter your third grade : "))

min_average = 10.0
min_grade = 7.0

average = calcul_average(g1, g2, g3)
if is_admitted(average, min_average, min_grade):
    print(f"You are admitted with an average of {average:.2f}. !")
else:
    print(f"You are NOT admitted with an average of {average:.2f}. !")