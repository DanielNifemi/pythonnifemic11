class MyCustomList(list):

    def __getitem__(self, item):
        print("getitem")
        super().__getitem__(item)

    def __setitem__(self, key, value):
        if value < 1:
            print("not adding it")
            return
        super().__setitem__(key, value)

    def append(self, item) -> None:
        if item < 1:
            print("not adding it")
            return
        super().append(item)


c = MyCustomList()
print(c)
c.append(9)
print(c[0])
c[1] = -6
print(c)


# have a dictionary that will inherit from the dict class
# it should also save the dictionary
# my_dist["name"] = "Nifemi"
# config.txt


class MyDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.save_dict()

    def save_dict(self):
        with open("config.txt", "w") as f:
            for key, value in self.items():
                f.write("{} = {}\n".format(key, value))


my_dict = MyDict()
my_dict["name"] = "Nifemi"
my_dict["age"] = 20
print(my_dict)
my_dict.save_dict()
