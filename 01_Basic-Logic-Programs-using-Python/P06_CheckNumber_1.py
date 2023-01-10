# Author: KEDAR BHARTIYA[appsec-samurai]
# Description: This program checks if a Number is Positive, Negative or 0

# Scenario 1:
"""Program using if...elif...else"""

num = float(input("Enter a number to check: "))
if num > 0:
    print("Given number {0} is Positive number".format(num))
elif num == 0:
    print("Given number {0} is Zero".format(num))
else:
    print("Given number {0} is Negative number".format(num))

# Scenario 2:
"""Program using Nested if"""

num = float(input("Enter a number to check: "))
if num >= 0:
    if num == 0:
        print("Given number {0} is Zero".format(num))
    else:
        print("Given number {0} is Positive number".format(num))
else:
    print("Given number {0} is Negative number".format(num))
