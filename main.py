# imports
import re
import ast
import os


# 1-Authentication screen ( login - register)
# ----> register
# • First name
# • Last name
# • Email [ validate pattern]
# • Password
# • Confirm password
# • Mobile phone [validated against Egyptian phone numbers]
def register():
    user = {}
    exist = False
    user["firstname"] = input("First Name:   ")
    user["lastname"] = input("last Name:   ")
    email = input("Email:   ")
    while not re.match(r"[a-z]+\@[a-z]+\.[a-z]", email):
        print("Not valid email, please try again\n")
        email = input("Email:   ")
    user["email"] = email
    password = input("Password:   ")
    c_password = input("Confirm password:   ")
    while password != c_password:
        print("Confirm password doesn't match\n")
        password = input("Password:   ")
        c_password = input("Confirm password:   ")
    user["password"] = password
    mobile = input("Mobile Number:   ")
    while mobile[0:3] not in ["011", "012", "015"]:
        print("Not Valid, please  enter local Egyptian mobile number\n")
        mobile = input("Mobile Number:   ")
    user["mobile"] = mobile
    with open("users", "r") as users:
        for u in users:
            res = ast.literal_eval(u)
            if res["email"] == user["email"]:
                print("This email exist, if you have an account please login.\n")
                exist = True
                break
    if not exist:
        with open("users", "a") as users:
            users.write(f"{user}\n")
            print("Registered successfully.")


# register()

# ----> login
# email
# password
def login():
    authed = False
    username = ""
    email = ""
    password = ""
    while email == "":
        email = input("Email:   ")
    while password == "":
        password = input("Password:   ")
    with open("users", "r") as users:
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


###################
# 2-projects screen ( create - view - search -delete)
# ----> create project
# • Title
# • Details
# • Total target (i.e 250000 EGP)
# • Set start/end date for the campaign
def create_project(auth):
    project_raiser = auth["username"]
    project = {}
    title = input("Project Title:  ")
    while title == "":
        title = input("Project Title:  ")
    project["title"] = title
    details = input("Project Details:  ")
    while details == "":
        details = input("Project Details:  ")
    project["details"] = details
    total_target = input("Project total target:  ")
    while total_target == "":
        total_target = input("Project total target:  ")
    project["total_target"] = int(total_target)
    start_date = input("Project start date:  ")
    while start_date == "":
        start_date = input("Project start date:  ")
    project["start_date"] = start_date
    end_date = input("Project end date:  ")
    while end_date == "":
        end_date = input("Project end date:  ")
    project["end_date"] = end_date
    project_data = {'project_raiser': project_raiser, 'project': project}
    with open("projects", "a") as projects:
        projects.write(f"{project_data}\n")


# ----> view all projects
def view_projects():
    with open("projects", "r") as projects:
        for project in projects:
            res = ast.literal_eval(project)
            title = res["project"]["title"]
            details = res["project"]["details"]
            total_target = res["project"]["total_target"]
            start_date = res["project"]["start_date"]
            end_date = res["project"]["end_date"]
            print(
                f"Title: {title}\nDetails: {details}\nTotal Target: {total_target}\nFunding period: from {start_date} to {end_date}\n--------------")


# view_projects()
# ----> search for project ( by name or start date)
def search_project():
    search_type = input("Type '1' to search by project title or '2' to search by date\n")
    while search_type not in ["1", "2"]:
        search_type = input("Type '1' to search by project title or '2' to search by date")
    if search_type == "1":
        # search by title
        query = input("Please enter a title:  ")
        while query == "":
            query = input("Please enter a title:  ")
        with open("projects", "r") as projects:
            for project in projects:
                res = ast.literal_eval(project)
                title = res["project"]["title"]
                if title == query:
                    details = res["project"]["details"]
                    total_target = res["project"]["total_target"]
                    start_date = res["project"]["start_date"]
                    end_date = res["project"]["end_date"]
                    print(
                        f"Title: {title}\nDetails: {details}\nTotal Target: {total_target}\nFunding period: from {start_date} to {end_date}\n--------------")

    elif search_type == "2":
        # search by date
        query = input("Please enter a date in format yyyy-mm-dd:  ")
        while query == "":
            query = input("Please enter a date in format yyyy-mm-dd:  ")
        with open("projects", "r") as projects:
            for project in projects:
                res = ast.literal_eval(project)
                start_date = res["project"]["start_date"]
                end_date = res["project"]["end_date"]
                if query == start_date or query == end_date:
                    title = res["project"]["title"]
                    details = res["project"]["details"]
                    total_target = res["project"]["total_target"]
                    print(
                        f"Title: {title}\nDetails: {details}\nTotal Target: {total_target}\nFunding period: from {start_date} to {end_date}\n--------------")


# search_project()
# ----> delete project (owner user only)
def delete_project(auth):
    username = auth["username"]
    title = input("Please enter a project title to delete:  ")
    while title == "":
        title = input("Please enter a project title to delete:  ")
    with open("projects", "r+") as projects:
        for project in projects:
            res = ast.literal_eval(project)
            if res["project"]["title"] == title:
                if res["project_raiser"] == username:
                    cmd = f'sed -i -r "/{title}/d" projects; rm projects-r;'
                    os.system(cmd)
                    print(f"Project {title} deleted successfully.")
                else:
                    print("Faild, Only project raiser can delete the project")
                    return False


# project menu
def project_menu(loged):
    print(f"Loged username: {loged['username']}")
    selection = input(
        "Enter a number from the following menu to select.\n1 - Create  a new project funding.\n2 - "
        "View all projects.\n3 - Search for a project.\n4 - Delete a project.\n5 - Logout\n")
    while selection not in ["1", "2", "3", "4", "5"]:
        selection = input(
            "Enter a number from the following menu to select.\n1 - Create  a new project funding.\n2 - View "
            "all projects.\n3 - Search for a project.\n4 - Delete a project.\n5 - Logout.\n")

    if selection == "1":
        create_project(loged)
        project_menu(loged)
    elif selection == "2":
        view_projects()
        project_menu(loged)
    elif selection == "3":
        search_project()
        project_menu(loged)
    elif selection == "4":
        delete_project(loged)
        project_menu(loged)
    elif selection == "5":
        return False


######################
# app screen function
def app():
    print("---------Welcome to FundMe App----------\n")
    authsys = input("Enter a number from the following menu to select.\n1 -Register.\n2 - Login.\n3 - Exit\n")
    while authsys not in ["1", "2", "3"]:
        authsys = input("Enter a number from the following menu to select.\n1 -Register.\n2 - Login.\n3 - Exit\n")
    if authsys == "1":
        register()
        app()
    elif authsys == "2":
        loged = login()
        if not loged:
            print("No user with this credentials is found")
            app()
        while loged:
            menu = project_menu(loged)
            if not menu:
                loged = False
                app()

    elif authsys == "3":
        return False


app()
