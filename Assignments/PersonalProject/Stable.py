for i in range(1, 13):
    for j in range(1, 13):
        print("{:>5d}  - {:>3d} = {:>2d}".format(i, j, i - j))
    print()
