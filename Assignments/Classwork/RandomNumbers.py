import random

correct_guess = random.randint(0, 100)
count = 0
while count < 5:
    guess = int(input("Guess a number between 0 and 100: "))
    if guess < 0 or guess > 100:
        print("the game is not meant for idiots")
        break



    if guess > correct_guess:
        print("Your guess is to high")
    elif guess < correct_guess:
        print("your guess is too low")
    else:
        print("finally you made it")
        break

        count += 1

else:
    print("u cant make it in life")
    print("The correct guess is" + correct_guess)
