# create a banking app that allows the user to create an account, deposit, withdraw, and check balance


# import the necessary modules
import os
import sys
import json
import time
import datetime
import random
import string
import argparse

# create a parser object to parse the command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-c", "--create", help="create a new account", action="store_true")
parser.add_argument("-d", "--deposit", help="deposit money into an account", action="store_true")
parser.add_argument("-w", "--withdraw", help="withdraw money from an account", action="store_true")
parser.add_argument("-b", "--balance", help="check the balance of an account", action="store_true")
parser.add_argument("-a", "--all", help="display all accounts", action="store_true")
parser.add_argument("-l", "--list", help="display a list of all accounts", action="store_true")
parser.add_argument("-s", "--search", help="search for an account", action="store_true")
parser.add_argument("-q", "--quit", help="quit the program", action="store_true")
args = parser.parse_args()

# create a dictionary to store the accounts
accounts = {}

# create a function to create a new account
def create_account():
    # create a random account number
    acct_num = "".join(random.choice(string.digits) for _ in range(10))
    # create a random account type
    acct_type = random.choice(["savings", "current"])
    # create a random account balance
    acct_balance = random.randint(1000, 100000)
    # create a random account age
    acct_age = random.randint(13, 65)
