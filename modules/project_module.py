import re
from classes.project import Project


# 2-projects screen ( create - view - search -delete)
# ----> create project
# • Title
# • Details
# • Total target (i.e 250000 EGP)
# • Set start/end date for the campaign
def create_project(auth):
    project_raiser = auth["username"]
    title = input("Project Title:  ")
    while title == "":
        title = input("Project Title:  ")
    details = input("Project Details:  ")
    while details == "":
        details = input("Project Details:  ")
    total_target = input("Project total target:  ")
    while not re.match(r"^[0-9]*$", total_target):
        total_target = input("Project total target:  ")
    start_date = input("Project start date:  ")
    while start_date == "":
        start_date = input("Project start date:  ")
    end_date = input("Project end date:  ")
    while end_date == "":
        end_date = input("Project end date:  ")
    newproject = Project(title, details, total_target, start_date, end_date, project_raiser)
    newproject.create_project()


# ----> view projects
def view_projects():
    Project.view_projects()


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
    elif search_type == "2":
        # search by date
        query = input("Please enter a date in format yyyy-mm-dd:  ")
        while query == "":
            query = input("Please enter a date in format yyyy-mm-dd:  ")
    Project.search_project(query, search_type)


# search_project()
# ----> delete project (owner user only)
def delete_project(auth):
    username = auth["username"]
    title = input("Please enter a project title to delete:  ")
    while title == "":
        title = input("Please enter a project title to delete:  ")
    Project.delete_project(username, title)
