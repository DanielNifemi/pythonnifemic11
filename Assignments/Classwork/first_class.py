class Person:
    def __init__(self, name: str) -> None:
        self.__name = name

        @property
        def name(self):
            print("You are calling the name property")
            return self._name

        @name.setter
        def name(self, name):
            print("You are setting the name property")
            if "f" in name:
                print("Fuck off")
                return
            self._name = name

        @classmethod
        def get_number_of_people(cls):
            return cls.__number_of_people

        person1 = Person("Nifemi")
        person1.name = "Nifemi"
        print(person1.name)
