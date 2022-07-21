# build a function in python that creates a secure password
# the password should be at least 8 characters long
# the password should contain at least one number
# the password should contain at least one uppercase letter
# the password should contain at least one lowercase letter
# the password should contain at least one special character


import random
import string


def secure_password():
    password = ""
    while len(password) < 8:
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)
    return password


print(secure_password())

# build a function in python that creates a secure password
# the password should be at least 8 characters long
# the password should contain at least one number
# the password should contain at least one uppercase letter
# the password should contain at least one lowercase letter
# the password should contain at least one special character
# the password should not contain any of the following:
# "123456", "password", "qwerty", "12345678", "abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz"
# the password should not contain any of the following:
