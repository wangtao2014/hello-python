import json
import os


def read_file_line_by_line():
    file = open("my_file.txt")
    for line in file:
        print(line)

    # 相同的：
    # with open("my_file.txt") as file:
    # for line in file:
    # print(line)


def read_file_line_number():
    file = open("my_file.txt", "r")
    for i, line in enumerate(file, start=1):
        print("Number %s: %s" % (i, line))


def write_string_to_file():
    contents = {"aa": 12, "bb": 14}
    with open("my_file1.txt", "w+") as file:
        file.write(str(contents))


def read_string_from_file():
    contents = {}
    with open("my_file1.txt", "r+") as file:
        contents = file.read()
    print(contents)


def write_obj_to_file():
    contents = {"aa": 12, "bb": 14}
    with open("my_file1.txt", "w+") as file:
        file.write(json.dumps(contents))


def read_obj_to_file():
    contents = {}
    with open("my_file1.txt", "r+") as file:
        contents = json.load(file)
    print(contents)


def check_and_delete_file():
    if os.path.exists("my_file.txt"):
        os.remove("my_file.txt")
    else:
        print("The file does not exist")


def delete_folder():
    os.rmdir("my_folder")

