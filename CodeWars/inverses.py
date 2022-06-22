# Given a number, return the additive inverse of it. Each positive becomes negatives, and the negatives
# become positives.

num = int(input("enter a number : "))
if num < 0:
    print(num-num*2)
else:
    print(-num)
