# Author: KEDAR BHARTIYA[appsec-samurai]
# Description: This program checks given string is Palindrome or not
# Summary: A palindrome is a string that is the same read forward or backward.
# For example, "dad" is the same in forward or reverse direction.

def check_palindrome(string):
    """This function checks the string for palindrome"""
    revString = string[::-1]
    if string == revString:
        print('String is Palindrome')
    else:
        print('String is not Palindrome')


if __name__ == '__main__':
    userInput = str(input('Enter a string to check for Palindrome: '))
    check_palindrome(userInput)
