
math = float(input("Enter your Math grade: "))
physics = float(input("Enter your Physics grade: "))

mean = (math + physics)/2

print(mean)
if mean >= 10:
    print("Congrats! You validated this course.")