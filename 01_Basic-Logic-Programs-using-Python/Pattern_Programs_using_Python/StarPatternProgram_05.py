# Author: KEDAR BHARTIYA[appsec-samurai]
"""
Program to demonstrate printing pattern like this:
*
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * * * *
* * * * * *
* * * * *
* * * *
* * *
* *
*
"""


def draw_right_start_pattern(n):
    for i in range(0, n + 1):
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")
    for i in range(n, 0, -1):
        for j in range(0, i):
            print("* ", end="")
        print("\r")


if __name__ == '__main__':
    user_input = int(input("Enter the number of rows to print: "))
    draw_right_start_pattern(user_input)
