import abc


class Animal(abc.ABC):
    __metaclass__ = abc.ABCMeta

    def name(self):
        return "Animal"

    @abc.abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def name(self):
        return super().name() + "-->" + " Dog"

    def sound(self):
        return "Woof"


print(Dog().name())
print(Dog().sound())
