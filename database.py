"""This file allows users to input their data and track information they've already inputted."""
from os import system
from time import sleep


def clear():
    """This definition is to add a mechanism to clear the screan."""
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def wiblywobly():
    print(
        "-------------------------                                                               SCAMMER GOT SCAMMED LOSER                                                              ---------------------------"
    )
    quit()


questions = True
print_data = True
age = False
user_desc = {}
number_of_users = 0
"""Represents user data to store it as a variable."""


class Users:

    def __init__(self, name, age, hobby):
        """__init__ allows me to collect information as variables so I can call them back later in the code."""
        self.name = name
        self.age = age
        self.hobby = hobby


def data_print():
    while print_data is True:
        print("Whos user data would you like to see? (Input users name)")
        u = input()
        u = u.replace("'", "")
        u = u.lower()
        try:
            print(
                f"Your name is {u.title()}, You are {user_desc[u].age} years old, and your favourite hobby is {user_desc[u].hobby}"
            )
            sleep(2)
            user_num()
        except KeyError:
            print("Please enter a name you've put into our database")
            sleep(1)
            clear()
            data_print()


def user_num():
    if number_of_users >= 1:
        print("Would you like to see another users data? (Y/N)")
        data = input()
        if data == "Y":
            data_print()
        elif data == "N":
            print("Okay, thank you for letting us steal your information:)")
            sleep(1.5)
            clear()
            wiblywobly()
        else:
            print("Please enter Y/N")
            user_num()
    else:
        print("Okay, thank you for letting us steal your information:)")
        sleep(1)
        clear()
        wiblywobly()


while questions is True:
    print("Helloo!! Thank you for taking our survey!!")
    print("Tell me about yourself")
    name = input("What is your name?\n").lower()
    age = True
    while age is True:
        try:
            age = int(input("How old are you?\n"))
        except ValueError:
            print("Please enter a number")
            age = True
    hobby = input("What is your favourite hobby?\n").lower()
    user_desc[name] = Users(name, age, hobby)
    print(
        "Is there more user information you would like us to store in our database? (Y/N)"
    )
    extra_user = input()
    while extra_user not in ("Y", "N"):
        print("Please enter Y/N")
        print(
            "Is there more user information you would like us to store in our database (Y/N)"
        )
        extra_user = input()

    if extra_user == "Y":
        print("Loading new user interface...")
        number_of_users = +1
        sleep(0.8)
        clear()
        questions = True
    elif extra_user == "N":
        print("Okay, thank you for inputting your data...")
        sleep(1)
        clear()
        print(user_desc.keys())
        data_print()