def areAnagrams(a, b):
    a = str(a)
    b = str(b)
    if sorted(a) == sorted(b):
        return True
    else:
        return False


a = 240
b = 204

if areAnagrams(a, b):
    print("Yes")
else:
    print("No")
