# Author: KEDAR BHARTIYA[appsec-samurai]
# Description: This program calculates L.C.M of two numbers entered by the user

def find_LCM(number1, number2):
    """This function calculates LCM of two numbers given by the user"""
    max_num = max(number1, number2)
    i = max_num
    while True:
        if (i % number1 == 0  and i % number2 == 0):
            lcm = i
            break
        i += max_num

    return lcm


if __name__ == '__main__':
    userInput1 = int(input('Enter first number: '))
    userInput2 = int(input('Enter second number: '))
    print('LCM of {} and {} is {}'.format(userInput1, userInput2, find_LCM(userInput1, userInput2)))
