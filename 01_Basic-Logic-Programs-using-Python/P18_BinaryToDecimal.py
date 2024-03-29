# Author: KEDAR BHARTIYA[appsec-samurai]
# Description: This program converts binary number to its equivalent decimal form

def binary_to_decimal(binary):
    """This function calculates the decimal equivalent of given binary number"""
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    print('Decimal equivalent of {} is {}'.format(binary1, decimal))


if __name__ == '__main__':
    userInput = int(input('Enter the binary number [like: 1010] to check its decimal equivalent: '))
    binary_to_decimal(userInput)
