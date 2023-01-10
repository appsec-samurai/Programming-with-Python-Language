# Author: KEDAR BHARTIYA[appsec-samurai]
# Description: This program calculates H.C.F or G.C.D of two numbers
# Summary: The highest common factor (H.C.F) or greatest common divisor (G.C.D) of two numbers is the largest positive
# integer that perfectly divides the two given numbers.


# Scenario 1:
"""Using Loops"""
def find_HCF(x, y):

# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf


if __name__ == "__main__":
    userInput1 = int(input("Enter first number: "))
    userInput2 = int(input("Enter first number: "))
    print("The H.C.F. of {0} and {1} is {2}".format(userInput1, userInput2, find_HCF(userInput1, userInput2)))

# Scenario 2:
# Using the Euclidean Algorithm

def find_HCF(x, y):
   while(y):
       x, y = y, x % y
   return x

if __name__ == "__main__":
    userInput1 = int(input("Enter first number: "))
    userInput2 = int(input("Enter first number: "))
    print("The H.C.F. of {0} and {1} is {2}".format(userInput1, userInput2, find_HCF(userInput1, userInput2)))
