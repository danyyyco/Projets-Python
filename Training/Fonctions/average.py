def average(*grades):
    if len(grades) == 0:
        return 0
    else:
        return sum(grades) / len(grades)

print(average())
print(average(90, 80, 70))
