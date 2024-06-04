
grade = float(input("Enter your grade: "))

if grade < 10:
    print("Not validated!")
elif grade >= 10 and grade < 12:
    print("Passable!")
elif grade >= 12 and grade < 14:
    print("Quite good!")
elif grade >= 14 and grade < 16:
    print("Good!")
elif grade >= 16 and grade < 18:
    print("Very Good!")
elif grade >= 18 and grade <= 20:
    print("Excellent!")

