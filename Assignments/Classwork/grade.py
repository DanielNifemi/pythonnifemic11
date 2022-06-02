grade = int(input("Enter your score to know your grade: "))
user_input = grade
if 70 > grade <= 100:
    print("A")

elif 69 <= grade >= 60:
    print("B")

elif 50 >= grade <= 59:
    print("C")

elif 45 >= grade <= 49:
    print("D")

elif 44 <= grade >= 40:
    print("E")

elif grade < 40:
    print("F")
