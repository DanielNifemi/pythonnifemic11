import time
from datetime import datetime
from termcolor import colored
from pyfiglet import Figlet
from state_machine import StateMachine
from db_handler import *
from colors import *

current_user = StateMachine()
header = Figlet(font="larry3d")
twitter_banner = Figlet(font="banner3-D")


def command_engine(command: str):
    if command.lower() == "help":
        help_message()
    elif command.lower() == "exit":
        if current_user.current_user is None:
            print("Logging out...")
            time.sleep(1.2)

        print("Bye 👋!")
        time.sleep(0.75)
        exit()
    elif command.lower() == "login":
        login()
    elif command.lower() == "tweet -c" or command.lower() == "tweet --create":
        tweet(flag="c")
    elif command.lower() == "tweet -d" or command.lower() == "tweet --delete":
        tweet(flag="d")
    elif command.lower() == "logout":
        logout()
    elif command.lower() == "view -p" or command.lower() == "view --profile":
        view(flag="p")
    elif "view -u" in command.lower() or "view --user" in command.lower():
        view(flag="u", user=command.split(" ")[-1])
    elif command.lower() == "view -t" or "view --tweet" in command.lower():
        view(flag="t")
    elif command.lower() == "create":
        create_user()
    else:
        print(f"{red}Invalid command!{reset}")
        command_rerun()


def command_rerun():
    print("\nEnter your next command. Use 'help' to see a list of commands.")
    command = input(f"{yellow}>>> {reset}")
    command_engine(command)


def welcome_message():
    print("""Welcome to the Fakest Twitter on earth!

You can follow users, and create tweets and much more.
Type 'help' to see a list of commands.""")


def help_message():
    print(colored(header.renderText("Twitter Help"), "blue"),
          f"""Available Commands:
{blue}help{reset} - show this help message
{blue}exit{reset} - exit the program
{blue}login{reset} - login to your account
{blue}logout{reset} - logout of your account (requires an active session)
{blue}create{reset} - create a new account
{blue}tweet{reset} - interact with the tweet system
  {bright_yellow}Options:{reset}
    {green}-c, --create{reset}              create a tweet
    {green}-d, --delete{reset}              delete a tweet

{blue}view{reset} - view a profile
  {bright_yellow}Options:{reset}
    {green}-p, --profile{reset}             view your profile
    {green}-u, --user [username]{reset}     view a user's profile
    {green}-t, --tweet{reset}               view all tweets""", sep="\n")
    command_rerun()


def login(invoked=False, username=None, password=None):
    if current_user.current_user is not None:
        print(f"{red}You are already logged in!{reset}")
        print()
        command_rerun()

    print("Login Portal\n")

    if username is None and password is None:
        username = input("Enter your username: ")
        password = input("Enter your secure, secret password: ")

    user = get_user(username)

    if user is None:
        print(f"{red}User not found!{reset}")
        print()
        login()
    elif user["password"] != password:
        print(f"{red}Wrong password!{reset}")
        print()
        login()
    else:
        print("Welcome back, @" + username + "!")
        current_user.change_state(username)
        command_rerun()


def logout():
    current = current_user.current_state()
    if current is None:
        print(f"{red}You are not logged in!{reset}")
        print()
        command_rerun()
    else:
        print("Logging out...")
        current_user.change_state(None)
        time.sleep(1.2)
        print("Bye 👋!")
        time.sleep(0.75)
        print()

        welcome_message()
        command = input(f"{yellow}>>> {reset}")

        command_engine(command)


def tweet(flag="c"):
    print()
    # Add animations later
    user = current_user.current_state()
    if user is None:
        print(f"{red}You are not logged in!{reset}")
        print()
        command_rerun()
    else:
        if flag == "c":
            print("Opening Tweet creation portal..")
            time.sleep(0.5)
            tweet = input("Write your tweets content: ")

            timestamp = time.time()
            date_time = datetime.fromtimestamp(timestamp)

            create_tweet(user, dict(date=date_time.strftime("%d %B, %Y - %H:%M"), tweet=tweet))
            print("Tweet created successfully!")
            print()
            command_rerun()
        elif flag == "d":
            delete_tweet()


def view_tweets(invoked=False):
    user = current_user.current_state()
    if user is None:
        print(f"{red}You are not logged in!{reset}")
        print()
        command_rerun()
    else:
        tweets: list = get_user_tweets(user)

        for i in range(len(tweets)):
            print(f"{i + 1}. {tweets[i]['tweet']}\nCreated at: {tweets[i]['date']}\n", end="\n")

        if not invoked:
            command_rerun()


def delete_tweet():
    view_tweets(invoked=True)
    user = current_user.current_state()
    tweets: list = get_user_tweets(user)

    index = int(input("\nUse the numbers to select the tweet you want to delete: "))
    delete_tweet(user, tweets[index - 1])
    command_rerun()


def view_profile(username: str = None):
    if username is None:
        username = current_user.current_state()

    user = get_user(username)
    if user is None:
        print(f"{red}User not found!{reset}")
        print()
        command_rerun()
    else:
        # print("@" + username + " has " + str(user["tweets"]) + " tweets.")
        # print("@" + username + " is following " + str(user["following"]) + " users.")
        # print("@" + username + " is being followed by " + str(user["followers"]) + " users.")
        # print("@" + username + " is " + ("verified" if user["verified"] else "not verified"))
        print(colored(twitter_banner.renderText(f"{username}"), "blue"),
              f"""Name: {user["name"]}
Username: {user["username"]}
Followers: {user["followers"]}
Following: {user["following"]}
Verified: {True if user["verified"] else False}""", sep="\n")
        print()
        command_rerun()


def view(flag="p", user=None):
    print()
    if user is None:
        user = current_user.current_state()

    if current_user.current_state() is None:
        print(f"{red}You are not logged in!{reset}")
        print()
        command_rerun()
    else:
        if flag == "p":
            view_profile()
        elif flag == "u":
            view_profile(user)
        elif flag == "t":
            view_tweets()
        else:
            print(f"{red}Invalid flag!{reset}")
            print()
            command_rerun()


def get_usernames():
    pass


def create_user():
    if current_user.current_state() is not None:
        print(f"{red}You are already logged in!{reset}")
        print()
        command_rerun()

    print()
    # Add animations later
    print("Opening User creation portal..")
    time.sleep(0.5)

    name = input("Enter your name to get started: ")
    age = input("What's your age: ")
    username = input("What's your username: ")
    names = get_usernames()

    if username in names:
        print(f"{red}Username already taken!{reset}")
        print()
        username = input("What's your username: ")

    password = input("What's your password: ")
    user = dict(name=name, age=age, username=username, password=password, tweets=[], following=0, followers=0,
                verified=False)
    add_to_db(user)
    print("User created!")
    print()
    current_user.change_state(username)
    print("Welcome to the Fakest Twitter on earth, @" + username + "!")
    command_rerun()