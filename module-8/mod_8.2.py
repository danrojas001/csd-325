# Dan Rojas
# 20 Nov 2025
# Mod 8.2
##############

# Reads data from students.json file, and prints it. Then appends my_info to the end of the file before printing the
# newly updated data. Then writes the new data to the json file and asks if the changes should be saved. Depending on
# the answer, it will either leave the json file with change in place or use the backup file to revert the change
# then delete the backup.

import sys
import os
import json
import shutil
import tkinter
from tkinter import messagebox

REQUIRED_MAJOR = 3
REQUIRED_MINOR = 13

filename = "students.json"
filepath = os.path.abspath(filename)
backup = "students_backup.json"
original = " == Original Student List =="
updated = "== Updated Student List =="
json_updated = "== JSON file updated =="


def main():
    check_python_version()
    shutil.copy(filename, backup)
    data = read_file(filename)
    notify(original)
    print_students(data)
    my_info = {"F_Name": "Daniel", "L_Name": "Rojas", "Student_ID": 77777, "Email": "rojasd@fake.com"}
    data.append(my_info)
    notify(updated)
    print_students(data)
    write_file(filename, data)
    notify(json_updated)
    message_box()
    cleanup()


def print_students(data):
    for student in data:
        print('{}, {} : ID = {}, Email = {}'.format(student['L_Name'], student['F_Name'], student['Student_ID'],
                                                    student['Email']))


def read_file(file):
    with open(file) as json_file:
        data = json.load(json_file)
        return data


def write_file(file, data):
    with open(file, 'w') as json_file:
        json.dump(data, json_file, indent=4)


def notify(notification):
    print(f"\n{notification}\n")


def message_box():
    root = tkinter.Tk()
    root.withdraw()
    response = messagebox.askyesno(title=None,
                                   message=f"{filepath}\n\nThis file has been modified. Do you want to save changes?")
    if response:
        root.destroy()
    elif not response:
        bak_file = read_file(backup)
        write_file(filepath, bak_file)
        root.destroy()


def cleanup():
    if os.path.exists(backup):
        os.remove(backup)


# Python version check
def check_python_version():
    current_major = sys.version_info.major
    current_minor = sys.version_info.minor

    if current_major != REQUIRED_MAJOR or current_minor < REQUIRED_MINOR:
        print(
            f"Python version mismatch: This script was written with Python {REQUIRED_MAJOR}.{REQUIRED_MINOR}"
            f", but you are running {current_major}.{current_minor}."
        )
        print("Please consider upgrading your Python version for full compatibility.")
        print()
    else:
        print(f"Python version {current_major}.{current_minor} is compatible.")
        print()


if __name__ == "__main__":
    main()
