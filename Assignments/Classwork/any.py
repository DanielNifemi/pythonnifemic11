from datetime import datetime

lst = [1, 2, 3, 4, 5, 8]
print(all(i for i in lst if i >= 7))
print(all(True if i >= 7 else False for i in lst))
print(max(lst))
print(max(['i', 'love', 'Love'], key=len))



