# Author: KEDAR BHARTIYA[appsec-samurai]
# Description: This program converts decimal number to its equivalent binary form

def decimal_to_binary(n):
    """Function to print binary number for the input decimal using recursion"""
    if n > 1:
        decimal_to_binary(n//2)
    print(n % 2, end="")


if __name__ == '__main__':
    userInput = int(input('Enter the decimal number to find its binary equivalent: '))
    decimal_to_binary(userInput)
    print()
