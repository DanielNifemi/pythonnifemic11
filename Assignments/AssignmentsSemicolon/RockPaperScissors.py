def rockpaperscissors():
    import random
    choice = int(input("Enter your choice: "))
    print("Rock, Paper, Scissors")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Quit")

    if choice == 1:
        print("You chose Rock")
    elif choice == 2:
        print("You chose Paper")
    elif choice == 3:
        print("You chose Scissors")
    elif choice == 4:
        print("Quitting")
    else:
        print("Invalid choice")
        rockpaperscissors()
    computer = random.randint(1, 3)
    if computer == 1:
        print("Computer chose Rock")
    elif computer == 2:
        print("Computer chose Paper")
    elif computer == 3:
        print("Computer chose Scissors")
    if choice == computer:
        print()
        print("It's a tie")
        rockpaperscissors()
    elif choice == 1 and computer == 2:
        print()
        print("You lose")
        rockpaperscissors()
    elif choice == 1 and computer == 3:
        print()
        print("You win")
        rockpaperscissors()
    elif choice == 2 and computer == 1:
        print()
        print("You win")
        rockpaperscissors()
    elif choice == 2 and computer == 3:
        print()
        print("You lose")
        rockpaperscissors()
    elif choice == 3 and computer == 1:
        print()
        print("You lose")
        rockpaperscissors()
    elif choice == 3 and computer == 2:
        print()
        print("You win")
        rockpaperscissors()
    else:
        print("Invalid choice")
        rockpaperscissors()

        choice = input("enter your choice :")
        print(rockpaperscissors, choice)
