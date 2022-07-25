# create an application that allows the user to in put his/her health information
import json

# create a dictionary to store the health information
import sys

health_info = {}

print("================================================================")
print()
print("               WELCOME TO SEMICOLON HEALTH AFRICA")
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
    # login the user
    if username == "admin" and password == "admin":
        print("Welcome to the admin page")
        print()
        print("1. Add a new user")
        print("2. Add a new patient")
        print("Welcome to the system")
        print(health_info)
    else:
        print("Invalid username or password")
        sys.exit()
elif choice == 2:
    print("Enter your username : ", end="")
    username = input()
    print("Enter your password : ", end="")
    password = input()
    print("Enter your name : ", end="")
    name = input()
    print("Enter your email : ", end="")
    email = input()
    print("Please input your health information:")
    # ask the user to input the name
    name = input("Name: ")
    # ask the user to input the age
    age = input("Age: ")
    # ask the user to input the height
    height = input("Height: ")
    # ask the user to input the weight
    weight = input("Weight: ")
    # ask the user to input the blood type
    blood_type = input("Blood type: ")
    # ask the user to input the allergies
    allergies = input("Allergies: ")
    # ask the user to input the medical conditions
    medical_conditions = input("Medical conditions: ")
    # ask the user to input the medications
    medications = input("Medications: ")
    # ask the user to input the medical history
    medical_history = input("Medical history: ")
    # ask the user to input the physical activity
    physical_activity = input("Physical activity: ")
    # ask the user to input the diet
    diet = input("Diet: ")
    # ask the user to input the sleep
    sleep = input("Sleep: ")
    # ask the user to input the exercise
    exercise = input("Exercise: ")
    # ask the user to input the stress
    stress = input("Stress: ")
    # ask the user to input the weight loss
    weight_loss = input("Weight loss: ")
    # ask the user to input the weight gain
    weight_gain = input("Weight gain: ")
    # ask the user to input the weight maintenance
    weight_maintenance = input("Weight maintenance: ")
    print()
    print()
    print()
    print()

    # print the health information in a report format
    print("================================================================")
    print()
    print("               WELCOME TO SEMICOLON HEALTH AFRICA")
    print()
    print("================================================================")
    print("Where all your health issues are solved..........")
    print("\n")
    print("Name: " + name)
    print("Age: " + age)
    print("Height: " + height)
    print("Weight: " + weight)
    print("Blood type: " + blood_type)
    print("Allergies: " + allergies)
    print("Medical conditions: " + medical_conditions)
    print("Medications: " + medications)
    print("Medical history: " + medical_history)
    print("Physical activity: " + physical_activity)
    print("Diet: " + diet)
    print("Sleep: " + sleep)
    print("Exercise: " + exercise)
    print("Stress: " + stress)
    print("Weight loss: " + weight_loss)
    print("Weight gain: " + weight_gain)
    print("Weight maintenance: " + weight_maintenance)
    print("\n")

    # store the health information in the dictionary
    health_info[name] = [name, age, height, weight, blood_type, allergies, medical_conditions, medications,
                         medical_history, physical_activity, diet, sleep, exercise, stress, weight_loss, weight_gain,
                         weight_maintenance]
    user_info = [username, password]
    # save the patient's health information to a json file
    with open('health_info.json', 'w') as f:
        json.dump(health_info, f)
    print("Your health information has been saved successfully")
    print("\n")
    # save username and password to a json file
    with open('user_info.json', 'w') as f:
        json.dump(user_info, f)
    print("Your username and password has been saved successfully")
