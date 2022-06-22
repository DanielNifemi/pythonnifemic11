# This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.

score = int(input("enter a number:"))
if score % 2 == 1:
    print(score * 8)
else:
    print(score*9)

