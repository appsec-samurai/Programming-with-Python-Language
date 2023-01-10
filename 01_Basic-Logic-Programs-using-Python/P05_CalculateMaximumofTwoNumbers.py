# Author: KEDAR BHARTIYA[appsec-samurai]
# Description: This program finds the Maximum of two numbers.


# Scenario 1:
def maximum(x, y):
    if x > y:
        print("{0} is greater than {1}".format(x, y))
    elif y > x:
        print("{0} is greater than {1}".format(y, x))
    else:
        print("{0} and {1} are equal numbers".format(x, y))


x = input("Enter the value of x: ")
y = input("Enter the value of y: ")
maximum(x, y)

# Scenario 2:
"""Using max() function"""

x = input("Enter the value of x: ")
y = input("Enter the value of y: ")

maximum = max(x, y)
print("{0} is greater among {1 }and {2} are equal numbers".format(maximum, x, y))
