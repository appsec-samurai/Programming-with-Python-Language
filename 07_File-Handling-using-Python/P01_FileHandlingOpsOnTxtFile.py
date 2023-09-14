# Author: KEDAR BHARTIYA[appsec-samurai]
# Description: This program illustrate the File handling functionality on simple Txt file in Python.
# Note: Use each method at one time to get actual output of the program.
import os


# Create a New file
def create_file(filename):
    try:
        with open(filename, 'w') as f:
            f.write('Hello, world!\n')
        print("File " + filename + " is created successfully.")
    except IOError:
        print("Error: could not create a file " + filename)


# Read the content of a file
def read_file(filename):
    try:
        with open(filename, 'r') as f:
            contents = f.read()
            print(contents)
    except IOError:
        print("Error: could not read file " + filename)


# Append new text to the existing file
def append_file(filename, text):
    try:
        with open(filename, 'a') as f:
            f.write(text)
        print("Text appended to file " + filename + " successfully.")
    except IOError:
        print("Error: could not append to file " + filename)


# Rename the file
def rename_file(filename, new_filename):
    try:
        os.rename(filename, new_filename)
        print("File " + filename + " renamed to " + new_filename + " successfully.")
    except IOError:
        print("Error: could not rename file " + filename)


# Delete the file
def delete_file(filename):
    try:
        os.remove(filename)
        print("File " + filename + " deleted successfully.")
    except IOError:
        print("Error: could not delete file " + filename)


if __name__ == '__main__':
    filename = "demo.txt"
    new_filename = "new_demo.txt"

    create_file(filename)
    read_file(filename)
    append_file(filename, "This is some additional text appending to the file.\n")
    read_file(filename)
    rename_file(filename, new_filename)
    read_file(new_filename)
    delete_file(new_filename)
