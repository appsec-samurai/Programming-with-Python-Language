# Author: KEDAR BHARTIYA[appsec-samurai]
# Description: This program performs addition of two numbers.

# # Scenario 1:
# """Python program to add two already given numbers"""
#
# num1 = 10
# num2 = 15
#
# # Adding two nos
# sum = num1 + num2
#
# # printing the sum
# print("Sum of {0} and {1} is {2}".format(num1, num2, sum))

# Scenario 2:
"""Python program to add two numbers provided by user input"""

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# Adding two nos
# User might also enter float numbers
# sum = float(number1) + float(number2)
sum = int(num1) + int(num2)

# Printing the sum
print("Sum of {0} and {1} is {2}".format(num1, num2, sum))
