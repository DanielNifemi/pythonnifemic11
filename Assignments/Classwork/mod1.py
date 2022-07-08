
__all__ = ['add', 'sub']
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiply(a, b):
    return a*b



print("Mod2", __name__)

if __name__ == '__main__':
    print("i am invisible")
    print("Mod1", __name__)

    print(add(4, 7))
