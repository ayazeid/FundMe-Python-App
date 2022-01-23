import ast
import re
from classes.user import User


def register():
    firstname = input("First Name:   ")
    lastname = input("last Name:   ")
    email = input("Email:   ")
    while not re.match(r"[a-z]+\@[a-z]+\.[a-z]", email):
        print("Not valid email, please try again\n")
        email = input("Email:   ")
    password = input("Password:   ")
    c_password = input("Confirm password:   ")
    while password != c_password:
        print("Confirm password doesn't match\n")
        password = input("Password:   ")
        c_password = input("Confirm password:   ")
    mobile = input("Mobile Number:   ")
    while not any(re.match(pattern, mobile) for pattern in [r"011+[0-9]{8}", r"012+[0-9]{8}", r"015+[0-9]{8}"]):
        print("Not Valid, please  enter local Egyptian mobile number\n")
        mobile = input("Mobile Number:   ")
    newuser = User(firstname, lastname, email, password, mobile)
    newuser.add_new_user()


def login():
    authed = False
    username = ""
    email = ""
    password = ""
    while email == "":
        email = input("Email:   ")
    while password == "":
        password = input("Password:   ")
    with open("data/users", "r") as users:
        for user in users:
            res = ast.literal_eval(user)
            if res["email"] == email:
                # print("match found")
                if res["password"] == password:
                    username = res["firstname"] + res["lastname"]
                    authed = True
                    break
                else:
                    continue

    if not authed and username == "":
        return False
    else:
        return {"authed": authed, "username": username}


