# imports
from modules.auth import register, login
from modules.project_module import create_project, view_projects, search_project, delete_project
import os


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
    # check data directory users , projects files exist
    cmd = "if ! [ -d data ]; then mkdir data; touch data/projects data/users; fi; if ! [ -f data/projects ]; then " \
          "touch data/projects; fi; if ! [ -f data/users ]; then touch data/users; fi; "
    os.system(cmd)
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
