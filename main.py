from os import system, name
from time import sleep

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


questions = True
user_desc = {}


class Users:

    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby


while questions is True:
    print("Tell me about yourself")
    user_name = input("What is your name?\n>> ").title()
    age = int(input("How old are you?\n>> "))
    hobby = input("What is your favourite hobby?\n>> ").lower()
    user_desc[name] = Users(name, age, hobby)
    print(
        "Is there more user information you would like us to store in our database? (Y/N)\n>> "
    )
    extra_user = input()
    while extra_user not in ("Y", "N"):
        print("Please enter Y/N\n>> ")
        print(
            "Is there more user information you would like us to store in our database? (Y/N)>>"
        )
        extra_user = input()

    if extra_user == "Y":
        print("Loading new user interface...")
        sleep(0.5)
        clear()
        questions = True
    elif extra_user == "N":
        print("Okay, thank you for inputting your data")
        break
print("Would you like to see the user data that has been inputted? (Y/N)\n>>")
u = input()
u = u.lower()
if u not in ("Y", "N"):
    print("Please enter Y/N\n>> ")
    print("Would you like to see the user data that has been inputted? (Y/N)\n>> ")

if u == "Y":
    print(f"Your name is {u.title()}, You are {user_desc[u].age} years old, and your favourite hobby is {user_desc[u].hobby}")