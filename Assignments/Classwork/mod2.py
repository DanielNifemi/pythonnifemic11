# from mod1 import *
# from mod1 import multiply as mul
#
# print(add(4, 1))
# print(mul(4, 1))

file = open("hello.txt", mode="w", encoding="utf-8")

file.write("I love Writing\n")
file.write("i love reading\n")
file.writelines(["i am prone to violence", "i am prone to violence"])
file.close()