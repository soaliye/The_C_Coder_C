
number = 5

guess = int(input("Guess the number: "))

if guess == number:
    print("Nice guess!")
else:
    print("Incorrect!")
    guess = int(input("Guess the number: "))
    if guess == number:
        print("Nice guess!")
    else:
        print("Incorrect!")

