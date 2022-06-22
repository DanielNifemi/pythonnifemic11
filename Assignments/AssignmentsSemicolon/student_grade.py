# class Student:
#     def __init__(self):
#         self.maths = None
#         self.chemistry = None
#         self.physics = None
#         self.name = None
#         self.rollno = None
#         self.percentage = None
#
#     def getStudentDetails(self):
#         self.rollno = input("Enter Roll Number : ")
#         self.name = input("Enter Name : ")
#         self.physics = int(input("Enter Physics Marks : "))
#         self.chemistry = int(input("Enter Chemistry Marks : "))
#         self.maths = int(input("Enter Math Marks : "))
#
#     def printResult(self):
#         self.percentage = int((self.physics + self.chemistry + self.maths) / 300 * 100)
#         print(self.rollno, self.name, self.percentage)
#
#
# S1 = Student()
# S1.getStudentDetails()
#
# print("Result : ")
# S1.printResult()
#
# S1.physics += 9
#
# print("result after adding grace marks...")
# S1.printResult()

print("#################################################################")
print()
print("               WELCOME TO SEMICOLON AFRICA")
print()
print("#################################################################")

student1 = input("enter student one's name: ")
student2 = input("enter student two's name: ")
student3 = input("enter student three's name: ")
print()
student1a = input("Enter score for student one in maths: ")
student1b = input("Enter score for student one in english: ")
student1c = input("Enter score for student one in biology: ")
print()
student2a = input("Enter score student two in maths: ")
student2b = input("Enter score for student two in english: ")
student2c = input("Enter score for student two in biology: ")
print()
student3a = input("Enter score student two in maths: ")
student3b = input("Enter score for student two in english: ")
student3c = input("Enter score for student two in biology: ")
print()
print("Student one score for maths is : ", student1a)
print("Student one score for english is :", student1b)
print("Student one score for biology is : ", student1c)
print()
print("Student two score for maths is : ", student2a)
print("Student one score for english is :", student2b)
print("Student one score for biology is : ", student2c)
print()
print("Student one score for maths is : ", student3a)
print("Student one score for english is :", student3b)
print("Student one score for biology is : ", student3c)
print()
