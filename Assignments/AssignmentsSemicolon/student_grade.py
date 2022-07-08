
# write a program that outputs the report card of a student.

print("================================================================")
print()
print("               WELCOME TO SEMICOLON AFRICA")
print()
print("================================================================")
print()
print("1. Login")
print("2. Register")
print("3. Exit")
print()
print("Enter your choice : ", end="")
choice = int(input())
print()
if choice == 1:
    print("Enter your username : ", end="")
    username = input()
    print("Enter your password : ", end="")
    password = input()
    if username == "admin" and password == "admin":
        print("Welcome to the system")
    else:
        print("Invalid username or password")
elif choice == 2:
    print("Enter your username : ", end="")
    username = input()
    print("Enter your password : ", end="")
    password = input()
    print("Enter your name : ", end="")
    name = input()
    print("Enter your email : ", end="")
    email = input()
    print("Enter your phone number : ", end="")
    phone = input()
    print("Enter your address : ", end="")
    address = input()
    print("Enter your date of birth : ", end="")
    dob = input()
    print("Enter your age : ", end="")
    age = int(input())
    print("Enter your blood group : ", end="")
    blood_group = input()
    print("Enter your height : ", end="")
    height = float(input())
    print("Enter your weight : ", end="")
    weight = float(input())
    print("Enter your religion : ", end="")
    religion = input()

print("enter score for subject 1 : ", end="")
s1 = int(input())
print("enter score for subject 2 : ", end="")
s2 = int(input())
print("enter score for subject 3 : ", end="")
s3 = int(input())


print()
print()
print()
print()
print()
print()
print()

# print out the report card
print("================================================================")
print()
print("               WELCOME TO SEMICOLON AFRICA")
print()
print("================================================================")
print()
print("Name : ", name)
print("Email : ", email)
print("Phone number : ", phone)
print("Address : ", address)
print("Date of birth : ", dob)
print("Age : ", age)
print("Blood group : ", blood_group)
print("Height : ", height)
print("Weight : ", weight)
print("Religion : ", religion)

print("Subject 1 : ", s1)
print("Subject 2 : ", s2)
print("Subject 3 : ", s3)
print("Total : ", s1 + s2 + s3)
print("Average : ", (s1 + s2 + s3) / 3)
print("Grade : ", end="")
if (s1 + s2 + s3) / 3 >= 80:
    print("A+")
elif (s1 + s2 + s3) / 3 >= 70:
    print("A")
elif (s1 + s2 + s3) / 3 >= 60:
    print("B")
elif (s1 + s2 + s3) / 3 >= 50:
    print("C")
elif (s1 + s2 + s3) / 3 >= 40:
    print("D")
else:
    print("F")
print("================================================================")
print()
print("               WELCOME TO SEMICOLON AFRICA")
print()
print("================================================================")
print()

# import module
from tabulate import tabulate

# assign data
mydata = [
	[name,s1 , s2 , s3 ],
]

# create header
head = ["Name", "Maths", "English", "Science"]

# display table
print(tabulate(mydata, headers=head, tablefmt="grid"))


