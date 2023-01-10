# Author: KEDAR BHARTIYA[appsec-samurai]
# Description: This program checks if a Number is Odd or Even

num = int(input("Enter a number to check: "))
if (num % 2) == 0:
    print("Given number {0} is Even".format(num))
else:
    print("Given number {0} is Odd".format(num))
