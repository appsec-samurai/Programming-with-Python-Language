# Author: KEDAR BHARTIYA[appsec-samurai]
# Description: This program calculates the factorial of given number
# Note: Factorial of a non-negative integer, is multiplication of all integers smaller than or equal to n.
# For example factorial of 6 is 6*5*4*3*2*1

# Scenario 1:
"""Calculate the factorial of number in Recursive manner"""

def factorial_with_recursion(num):
    # single line to find factorial
    if (num == 1 or num == 0):
        return 1
    else:
        return num * factorial_with_recursion(num - 1);

# Driver Code
userInput = int(input("Enter the number to find its factorial: "));
print("Factorial of", userInput, "is", factorial_with_recursion(userInput), "in a Recurssive manner.")

# Scenario 2:
"""Calculate the factorial of number in Iterative manner"""

def factorial_with_iteration(num):
    if num < 0:
        return 0
    elif num ==0 or num == 1:
        return 1
    else:
        fact = 1
        while(num > 1):
            fact *= num
            num -= 1
        return fact

#Driver code
userInput = int(input("Enter the number to find its factorial: "))
print("Factorial of", userInput, "is", factorial_with_iteration(userInput), "in an Iterative manner.")
