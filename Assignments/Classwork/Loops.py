import string
#     print('x' , end="")


# list_of_numbers = [2 ,5 , 6 , 7 , 9]
# total: int = 0
#
#
#
# for x in list_of_numbers:
#     total +=1
#     print(list_of_numbers)


# lst = [2, 5, 7, 8, 9]
# sum(lst)
import abc
from idlelib.pyparse import trans

import cipher as cipher

S = 'hello to the fucking world'
print(S.upper())
print(S.lower())
print(S.capitalize())
print(S.title())
dir(S)
print(S.strip())
print(S.rstrip())
print(S.lstrip())
print(S.rfind("l", 3))
print(S.rfind("o", 1, 3))
print(S.index("w"))
print(S.strip())
print(S.swapcase())
print(S.count("l"))
print(S.zfill(10))
print(S.replace("l", "f"))
s = "hello"
abc = string.ascii_lowercase
s = "hello"
s.translate(str.maketrans(abc, trans))
cipher = user.translate()
