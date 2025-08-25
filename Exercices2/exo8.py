grade = float(input("Enter the grade: "))

if 90 <= grade <= 100:
    print("Grade: A")
elif 80 <= grade <= 89:
    print("Grade: B")
elif 70 <= grade <= 79:
    print("Grade: C")
elif 60 <= grade <= 69:
    print("Grade: D")
else:
    print("Grade: F")