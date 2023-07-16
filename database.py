from os import system
from time import sleep

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


questions = True
print_data = True
user_desc = {}


class Users:

    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby


while questions is True:
    print("Tell me about yourself")
    name = input("What is your name?\n").lower()
    age = int(input("How old are you?\n"))
    hobby = input("What is your favourite hobby?\n").lower()
    user_desc[name] = Users(name, age, hobby)
    print(
        "Is there more user information you would like us to store in our database? (Y/N)"
    )
    extra_user = input()
    while extra_user not in ("Y", "N"):
        print("Please enter Y/N")
        print(
            "Is there more user information you would like us to store in our database? (Y/N)"
        )
        extra_user = input()

    if extra_user == "Y":
        print("Loading new user interface...")
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
    print("Who's user data would you like to see? (Input users name)")
    u = input()
    u = u.replace("'", "")
    u = u.lower()
    print(f"Your name is {u.title()}, You are {user_desc[u].age} years old, and your favourite hobby is {user_desc[u].hobby}")
    print("Would you like to see another users data? (Y/N)")
    data = input()
    if data == "Y":
        print_data = True
    elif data == "N":
        print("Okay, thank you for letting us steal your information:)")
        print_data = False
        break
    else:
        print("Please enter Y/N")
        print("Would you like to see another users data? (Y/N)\n")
        data = input()
