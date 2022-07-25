class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person{self.name}  ,  {self.age} "

    def __repr__(self):
        return f"Person{self.name} , {self.age} "

    def __eq__(self, other):
        return self.age == other.age

        Nifemi = Person(name="Nifemi", age=20)
        ucj = Person(name="ucj", age=21)

        print(f"{Nifemi!r}")
        print(Nifemi == ucj)



