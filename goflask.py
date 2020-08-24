#!/usr/bin/env python3
import glob
import os
import readline
import venv

def get_directory(text, state):
    if "~" in text:
        text = os.path.expanduser("~")  # Go to user's home directory
    if os.path.isdir((glob.glob(text + "*"))[state]):
        return (glob.glob(text + "*"))[state] + "/"  # Add '/' if location is a dir.
    return (glob.glob(text + "*"))[state]


def make_dir(new_path, app_name):
    os.chdir(new_path)
    try:
        os.mkdir(f"{app_name}_app")
        os.chdir(f"{app_name}_app")
        new_venv = venv.EnvBuilder()
        new_file = open(f"{app_name}.py", "w")
        os.mkdir("static")
        os.mkdir("templates")
    except FileExistsError:
        print("A directory with that name already exists.")


def create_venv(venv_name):
    pass


if __name__ == "__main__":
    readline.set_completer_delims(" \t\n;")  # Override default delimiters
    readline.parse_and_bind("tab: complete")
    readline.set_completer(get_directory)
    print(f"\n\U0001F4CD PWD is {os.getcwd()}/")
    path = input("\U0001F4C1 Root dir. for your project:  ")
    project_name = input("\U0001F4DB Project name:  ")
    confirm = input(
        f"\U00002753 Create '{project_name}_app' in folder {path} (Y/N)?  "
    ).lower()
    if confirm == "y":
        make_dir(path, project_name)
    else:
        print("Goodbye!")
