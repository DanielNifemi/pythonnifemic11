import doctest


def add(x, y):
    """
    >>> add(2, 3)
    5
    >>> add(3, "Hi")
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'

    """
    return x + y


# if __name__ == '__main__':
#     doctest.testmod()
