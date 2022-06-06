for numbers in range(1, 101):
    if numbers % 15 == 0:
        print("FizzBuzz")
    if numbers % 3 == 0:
        print("FizzBuzz")
    if numbers % 5 == 0:
        print("Buzz")
    else:
        print(numbers)
