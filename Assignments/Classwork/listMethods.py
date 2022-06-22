# # import random
# #
# # random.seed(45)
# # rng = list(range(1, 100, 5))
# # print(rng)
# #
# # rng.append([1, 2, 3])
# # print(rng)
# #
# # rng.insert(-1, 99)
# # print(rng)
# #
# # popped = rng.pop(2)
# # print(popped)
# # print(rng)
# #
# # rng.remove(41)
# # print(rng)
# #
# # rng.copy()
# # print(rng)
# #
# # random.shuffle(rng)
# # print(rng)
# #
# # print(random.choice(rng))
# # rng.reverse()
# # print(rng)
#
# fruit = ["mango", "banana", "water melon", "Pineapple", "cherry", "cucumber", "apple"]
# fruit.sort()
# print(fruit)
#
# "{{()[]}}"
# '[({))]'
# "generate a list of prime numbers from 1 to 100"
# for numbers in range(1 , 101):
#     print()
#
# lower = int(input("Enter the small value:"))
# upper = int(input("Enter the high value:"))
# for number in range(lower, upper + 1):
#     if number > 1:
#         for i in range(2, number):
#             if (number % i) == 0:
#                 break
#         else:
#             print(number)

# lst = [int(input(f"Enter student {i}'s score :")) for i in range(1, 6)]
# print(lst)
# print("Total score is", sum)
# print("Max = ", max(lst))
# print("Min  = ", min(lst))
# print("Average = ", sum(lst) / len(lst))


# def is_prime(num: int) -> bool:
#     import math
#     max_divisor = math.ceil(math.sqrt(num)) + 1
#     for i in range(2, max_divisor):
#         if num % i == 0:
#             return False

# return True


#  prime = int(input("Enter a number -> "))
# print(is_prime(prime))
# primes = {k: v for k, v in enumerate(range(1, 10)) if is_prime(v)}
# print(type(primes))
# print(primes)


# def rotate(lst_p, rotate_key):
#     ex = rotate_key % len(lst_p)
#     return lst_p[ex:] + lst_p[ex:]
#
#
# key = 2
# lst = [7, -3, 2, 4, 9]
# print("the original list is {}".format(lst))
# print("the rotate list using {} as key is {}".format(key, rotate(lst, key)))
from turtle import st


# def histogram(word: st) -> int:
#     file = open(word, 'a')
#
#     text = file.read()
#
#     return text.count(st)
#
#
# # print(histogram('Alabama is a town', 'a'))
#
# def display():
#     letter = str(input('enter a letter: '))
#     word = str(input('enter a word: '))
#     print(countNum(word, letter))

# def histogram(word, str) -> dict[str, int]:
#     import string
#     abc = string.ascii_lowercase
#
#     map_ = {}
#
#     for char in abc:
#         map_[char] = word.lower().count(char)
#     return map_
#
#
# print(histogram("Java makes me a saddist", str))


# sentence = "Alabama is a town"
# print("the dictionary of the statement is:")
# print(histogram(sentence))


# def histogram_2(word):
#     import string
#     return {char: word.lower().count(char) for char in string.ascii_lowercase}
#
#
# print(histogram("i love python", str))
def multiply(a, b):
    result = a * b
    print(result)
