# crete a consistent method resolution
class A:
    def do_this(self):
        print(" From A")


class C(A):
    def do_this(self):
        print("From C")


class B(A):
    def do_this(self):
        print(" From B")


class D(C, B):
    def do_this(self):
        print(" From C")


print(D.__mro__)
