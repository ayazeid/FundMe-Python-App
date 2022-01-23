import ast
import os


class Project:
    project_id = 0

    def __init__(self, title, details, total_target, start_date, end_date, project_raiser):
        self.title = title
        self.details = details
        self.total_target = total_target
        self.start_date = start_date
        self.end_date = end_date
        self.project_raiser = project_raiser
        self.project_id

    def create_project(self):
        self.project_id = Project.project_id
        Project.project_id += 1
        with open("data/projects", "a") as projects:
            projects.write(f"{self.__dict__}\n")

    @classmethod
    def view_projects(cls):
        with open("data/projects", "r") as projects:
            for project in projects:
                res = ast.literal_eval(project)
                title = res["title"]
                details = res["details"]
                total_target = res["total_target"]
                start_date = res["start_date"]
                end_date = res["end_date"]
                print(
                    f"Title: {title}\nDetails: {details}\nTotal Target: {total_target}\nFunding period: from {start_date} to {end_date}\n--------------")

    @classmethod
    def search_project(cls, query, search_type):
        with open("data/projects", "r") as projects:
            for project in projects:
                res = ast.literal_eval(project)
                if search_type == "1":
                    title = res["title"]
                    if title == query:
                        details = res["details"]
                        total_target = res["total_target"]
                        start_date = res["start_date"]
                        end_date = res["end_date"]
                        print(
                            f"Title: {title}\nDetails: {details}\nTotal Target: {total_target}\nFunding period: from {start_date} to {end_date}\n--------------")
                elif search_type == "2":
                    start_date = res["start_date"]
                    end_date = res["end_date"]
                    if query == start_date or query == end_date:
                        title = res["title"]
                        details = res["details"]
                        total_target = res["total_target"]
                        print(
                            f"Title: {title}\nDetails: {details}\nTotal Target: {total_target}\nFunding period: from {start_date} to {end_date}\n--------------")

    @classmethod
    def delete_project(cls, username, title):
        with open("data/projects", "r+") as projects:
            for project in projects:
                res = ast.literal_eval(project)
                if res["title"] == title:
                    if res["project_raiser"] == username:
                        cmd = f'sed -i -r "/{title}/d" data/projects; rm data/projects-r;'
                        os.system(cmd)
                        print(f"Project {title} deleted successfully.")
                    else:
                        print("Failed, Only project raiser can delete the project")
                        return False
