# Author: KEDAR BHARTIYA[appsec-samurai]
# Description: This program determine whether given number is a Disarium Number.
# Summary: A number is said to be the Disarium number when the sum of its digit raised
# to the power of their respective positions becomes equal to the number itself.
# For example, 175 is a Disarium number as follows:
# 1^1+ 7^2 + 5^3 = 1+ 49 + 125 = 175


def check_disarium(num):
    rem = s = 0
    count_digits = len(str(num))

    # Makes a copy of the original number num
    n = num

    # Calculates the sum of digits powered with their respective position
    while num > 0:
        rem = num % 10
        s += int(rem ** count_digits)
        num = num // 10
        count_digits -= 1

    # Checks whether the sum is equal to the number itself
    if s == n:
        print("Given number {0} is a Disarium number".format(n))
    else:
        print("Given number {0} is not a Disarium number".format(n))


if __name__ == "__main__":
    userInput = int(input("Enter the number to check whether it is Disarium or not: "))
    check_disarium(userInput)

