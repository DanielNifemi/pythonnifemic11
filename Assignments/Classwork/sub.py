# def sub(a: int = 0, b: int = 0) -> int:
#     """calculate the difference of two numbers"""
#     return b - a
#
#
# print(sub(b=10, a=15))
# print(sub.__annotations__)
# print(sub.__doc__)
# help()
# # print(sub.__name__)
# # print(sub.__qualname__)
# # print(sub.__module__)
# # print(sub.__defaults__)
# # print(sub.__code__)
# # print(sub.__closure__)
# # print(sub.__globals__)
# # print(sub.__dict__)
# # print(sub.__kwdefaults__)
# # print(sub.__annotations__)
# # print(sub.__kwonlydefaults__)
# # print(sub.__kwonlyargs__)
# # print(sub.__signature__)
# # print(sub.__annotations__)
# # print(sub.__closure__)
# # print(sub.__code__)
# # print(sub.__globals__)
# # print(sub.__dict__)


def avg(*numbers):
    from statistics import mean
    # return sum(numbers) / len(numbers)
    return mean(numbers)


print(avg(1, 2, 3, 4))
print(avg(1, 2, 3))

lst = []


def add(a, *args, b=0, **kwargs):
    print(a)
    print(args)
    print(b)
    print(kwargs)
    add(6, 7, 8, b=9, c=0, f=8, y=4)
# print(d)
# print(add(**d))
