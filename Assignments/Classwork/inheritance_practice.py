class Animal:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def speak(self):
        print("i am barking")


class Dog(Animal):
    def __init__(self, name, breed, colour="brown"):
        self.colour = colour
        super().__init__(name, breed)


class Cat(Animal):
    def __init__(self, name, breed, colour="black"):
        self.colour = colour
        super().__init__(name, breed)
