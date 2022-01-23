import ast
import os

class User:
    def __init__(self, firstname, lastname, email, password, mobile):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.mobile = mobile

    def add_new_user(self):
        if not check_user_email(self.email):
            with open("data/users", "a") as users:
                users.write(f"{self.__dict__}\n")
                print("Registered successfully.")
        else:
            print("This email exist, if you have an account please login.\n")


def check_user_email(email):
    # check if email exist
    with open("data/users", "r") as users:
        for u in users:
            res = ast.literal_eval(u)
            if res["email"] == email:
                return True


