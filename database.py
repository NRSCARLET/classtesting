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
    print("-------------------------                                                               SCAMMER GOT SCAMMED LOSER                                                              ---------------------------")
questions = True
print_data = True
user_desc = {}
number_of_users = 0
"""Represents user data to store it as a variable."""
class Users:  
    def __init__(self, name, age, hobby):
        """__init__ allows me to collect information as variables so I can call them back later in the code.""" 
        self.name = name
        self.age = age
        self.hobby = hobby


while questions is True:
    print("Tell me about yourself")
    name = input("What is your name?\n").lower()
    age = int(input("How old are you?\n"))
    hobby = input("What is your favourite hobby?\n").lower()
    user_desc[name] = Users(name, age, hobby)
    print("Is there more user information you would like us to store in our database? (Y/N)")
    extra_user = input()
    while extra_user not in ("Y", "N"):
        print("Please enter Y/N")
        print("Is there more user information you would like us to store in our database (Y/N)")
        extra_user = input()

    if extra_user == "Y":
        print("Loading new user interface...")
        number_of_users =+1
        sleep(0.5)
        clear()
        questions = True
    elif extra_user == "N":
        print("Okay, thank you for inputting your data...")
        sleep(0.7)
        clear()
        break
print(user_desc.keys())
while print_data is True:
    print("Whos user data would you like to see? (Input users name)")
    u = input()
    u = u.replace("'", "")
    u = u.lower()
    if = user_desc.keys():
    print(f"Your name is {u.title()}, You are {user_desc[u].age} years old, and your favourite hobby is {user_desc[u].hobby}"
    )
    if number_of_users >= 1:
        print("Would you like to see another users data? (Y/N)")
        data = input()
        if data == "Y":
            print_data = True
        elif data == "N":
            print("Okay, thank you for letting us steal your information:)")
            print_data = False
            sleep(1)
            clear()
            wiblywobly()
        else:
            print("Please enter Y/N")
            print("Would you like to see another users data? (Y/N)\n")
            data = input()
    else:
        print_data = False
        print("Okay, thank you for letting us steal your information:)")
        sleep(1)
        clear()
        wiblywobly()
