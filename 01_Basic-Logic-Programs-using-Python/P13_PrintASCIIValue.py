# Author: KEDAR BHARTIYA[appsec-samurai]
# Description: This program prints ASCII Value of Character
# Summary: ASCII stands for American Standard Code for Information Interchange.

def get_ASCII(value):
    print("The ASCII value of '" + value + "' is", ord(value))


if __name__ == "__main__":
    userInput = input("Enter the character to get ASCII value of it: ")
    get_ASCII(userInput)
