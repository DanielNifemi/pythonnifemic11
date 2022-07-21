import json
import pickle
from pathlib import Path

file_path = Path("/json/twitter_users.txt").resolve()
twitter_users = [{'username': '@nifemi.py', 'password': 'password', 'email': 'nifemidaniel50@gmail.com'},
                 {'username': '@nifemidaniel2', 'password': 'password2', 'email': 'nifemidaniel167@yahoo.com'}]

x = json.dumps(twitter_users)
print(x)
print(type(x))
y = json.loads(x)
print(y)
print(type(y))

pickled_obj = pickle.dumps(twitter_users)
print(pickled_obj)


