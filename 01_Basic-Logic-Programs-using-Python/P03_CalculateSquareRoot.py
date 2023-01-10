# Author: KEDAR BHARTIYA[appsec-samurai]
# Description: This program calculates the square root of Positive as well as Real or Complex numbers.
import cmath

# Scenario 1:
"""Python program to calculate the square root for positive numbers"""

num = float(input("Enter number to find Square root: "))

num_sqrt = num ** 0.5
print("The square root of %0.3f is 0.3f"%(num, num_sqrt))

# Scenario 2:
"""Python program to calculate the square root for real or complex numbers"""
# Importing the complex math module

# Take input from the user like 1+2j
num = eval(input('Enter a number: '))

num_sqrt = cmath.sqrt(num)
print("The square root of {0} is {1:0.3f}+{2:0.3f}".format(num, num_sqrt.real, num_sqrt.imag))
