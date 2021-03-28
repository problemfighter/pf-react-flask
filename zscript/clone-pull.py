import os
import subprocess

directories = ["source-module", "app-module"]


def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)


def create_directories(directory_list: list):
    for directory in directory_list:
        create_directory(directory)


def execute_command(home, command):
    subprocess.run(command, shell=True, cwd=home)


def pull_project(home):
    git_directory = home + "/.git"
    if os.path.exists(git_directory):
        execute_command(home, "git pull")


def clone_project(root, project, url):
    if url != "":
        command = "git clone " + url + " " + project
        execute_command(root, command)


def setup_project(home):
    execute_command(home, "python setup.py develop")


def clone_and_setup(root, project, url, path):
    if not os.path.exists(path):
        clone_project(root, project, url)
        setup_project(path)


def pull_setup_project(home):
    pull_project(home)
    setup_project(home)


def clone_pull_setup(projects: dict):
    root = projects['dir']
    create_directory(root)
    repositories: dict = projects['repositories']
    repository_names = repositories.keys()
    for name in repository_names:
        print("\n\n\n\n-------------------------------------------------------------------------------------")
        print("Working with repository: " + name + ", source: " + root)
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        path = os.path.join(root, name)
        repository = repositories.get(name)
        clone_and_setup(root, name, repository, path)
        pull_setup_project(path)
        print("-------------------------------------------------------------------------------------")


source_projects = {
    "dir": "source-module",
    "repositories": {
        "flask-pf-common": "https://github.com/problemfighter/flask-pf-common.git",
        "flask-pf-sqlalchemy": "https://github.com/problemfighter/flask-pf-sqlalchemy.git",
        "flask-pf-marshmallow-swagger": "https://github.com/problemfighter/flask-pf-marshmallow-swagger.git",
    }
}


def start():
    clone_pull_setup(source_projects)
    pull_project("./")


if __name__ == '__main__':
    start()
