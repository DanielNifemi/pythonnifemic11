import math


# lists = [1 * 1, 2 * 1, 3 * 1, 4 * 1, 5 * 1, 6 * 1, 7 * 1, 8 * 1]
# for numbers in range(1, 13):
#     print(numbers)
#     print(numbers.conjugate()

for i in range(1, 13):
    for j in range (1 , 13):
        print("{:>5d}  x {:>3d} = {:>2d}".format(j, i, j * i))
    print()




