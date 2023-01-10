# Author: KEDAR BHARTIYA[appsec-samurai]
# Description: This program performs the swapping of two variables
# using temporary variable, without using temporary variable

# Scenario 1:
"""Python program to swap two variables using temporary variable"""

x = input("Enter the value of x: ")
y = input("Enter the value of y: ")

print("The value of x before swapping: {}".format(x))
print("The value of y before swapping: {}".format(y))

# Create a temporary variable and swap the values
temp = x
x = y
y = temp

print("The value of x after swapping: {}".format(x))
print("The value of y after swapping: {}".format(y))

# Scenario 2:
"""Python program to swap two variables without using temporary variable"""

x = input("Enter the value of x: ")
y = input("Enter the value of y: ")

print("The value of x before swapping: {}".format(x))
print("The value of y before swapping: {}".format(y))

# Swapping values without temporary variable
x, y = y, x

print("The value of x after swapping: {}".format(x))
print("The value of y after swapping: {}".format(y))

# Scenario 3:
"""Python program to swap two variables without using temporary variable"""
# If the variables are both numbers, we can use arithmetic operations to do the same.

x = input("Enter the value of x: ")
y = input("Enter the value of y: ")

print("The value of x before swapping: {}".format(x))
print("The value of y before swapping: {}".format(y))

# Swap variables using Addition and Subtraction
x = x + y
y = x - y
x = x - y

# Swap variables using Multiplication and Division
x = x * y
y = x / y
x = x / y

# Swap variables using XOR swap
# This algorithm works for integers only
x = x ^ y
y = x ^ y
x = x ^ y

print("The value of x after swapping: {}".format(x))
print("The value of y after swapping: {}".format(y))