# from mod1 import *
# from mod1 import multiply as mul
#
# print(add(4, 1))
# print(mul(4, 1))

# file = open("helloyou.txt", mode="w", encoding="utf-8")
#
# file.write("I love Writing\n")
# file.write("i love reading\n")
# file.writelines(["i am prone to violence", "i am prone to violence"])
# file.close()
#
country_codes = {'Finland': 'fi' , 'England': 'Eng' , 'Nigeria':'Nig'}

print(country_codes)
print(len(country_codes))

if country_codes:
    print("Country codes is not empty")
else:
    print("Country codes is empty")
print(country_codes['Finland'])

months_of_the_year = {'January' : '25' , 'February':'4' , 'July' : '27'}

for months , days in months_of_the_year.items():
    print(f"{months} {days} is my birthday")

    # n = 1231
    # n = str(n)
    # print(n == n[::-1])

