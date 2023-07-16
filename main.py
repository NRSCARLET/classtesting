from os import system, name
questions = True
class Users:
    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby

while questions is True:
    print("Tell me about yourself")
    user_name=input("What is your name?\n>> ").title()
    age=input("How old are you?\n>> ")
    hobby=input("What is your favourite hobby?\n>> ").lower()
    user_desc[name] = Users(name, age, hobby)

print(user_desc).keys()
    
    
    