# print("valentina:""Hello my name is valentina , what's your name!!: ")
# name = input()
# print("valentina: "" Hello " +name+ " Have a nice day")

name = input("hello what's your name: ")
print(name, "it's nice to meet you")
gender = input("are you male or female: ")
print("the", gender, " gender is a nice gender")
age = int(input("may i know how old are you: "))
options1 = "for your age these are the range of things you can do with this app\n1. sing\n2. Make videos  "
options2 = ("Since you are above legal age , these are things you can do with the app\n1. make adult videos\n2. "
            "make record songs")

if age < 18:
    print(options1)
else:
    print(options2)
advice = input(options1)

