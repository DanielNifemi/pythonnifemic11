lst= [1 , 2, 3 ,4 , 5, 6, 7, 8, 9, 10]    # list of numbers
try:
    s= lst[20]
    print("i did good")
except IndexError as e:
    print(f"index error: {e}")
except TypeError as t:
    print(f"type error: {t}")
finally:
    print("i am finally")   # this will always be executed