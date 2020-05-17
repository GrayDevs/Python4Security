# -*-coding:UTF-8 -*
# !/usr/bin/env python

""" Project tool-box """

import os
from tkinter import filedialog, Tk


#########################
#                       #
#       FILE UTILS      #
#                       #
#########################

def touch(path):
    with open(path, 'a'):
        os.utime(path, None)


def file_check(filename):
    if not os.path.isfile(filename):
        print("[-] Wordlist:", filename, "does not exist.")
        exit(1)
    if not os.access(filename, os.R_OK):
        print("[-] Wordlist:", filename, "access denied")
        exit(1)
    return True


def file_open(filename, right='r'):
    try:
        fh = open(filename, right)
    except Exception as e:
        print("[-] Error while reading file:", e)
        exit(1)
    return fh


def file_save():
    root = Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    return filedialog.asksaveasfilename(title="Select file", filetypes=("all files", "*.*"))


def file_wipe(file):
    """ Erase file content if it already exists
    :param file: <str>
    :return: file: <str> - wiped file
    """
    with open(file, encoding='utf-8', mode='w') as file_to_wipe:
        file_to_wipe.write("")
    return file


def file_open_gui():
    """ Open a Tkinter filedialog
    :return: <str> - file path
    """
    root = Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    return filedialog.askopenfilename(title="Select file to Encrypt",
                                      filetypes=(("Text Files", "*.txt"), ("all files", "*.*")))


def file_hex(file_name="tests/idea_test.txt"):
    """ Getting the content of a file
    :param: file_name: <str> - file name
    :return: content_as_bytes : <str> - content in hex
    """
    with open(file_name, 'rb') as file_alias:
        content_as_bytes = file_alias.read()

    hex_content = bytes.hex(content_as_bytes)
    return hex_content


def file_operation(file='', operation='', right='r'):
    if operation == "check":
        file_check(file)
    elif operation == "open":
        file_check(file)
        return file_open(file, right)
    elif operation == "save":
        file_save()
    elif operation == "wipe":
        file_check(file)
        file_wipe(file)
    else:
        print("[-] This file operation is not supported or does not exist.")


# TEST ZONE
if __name__ == "__main__":
    pass
