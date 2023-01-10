# Author: KEDAR BHARTIYA[appsec-samurai]
"""
Program to demonstrate Downward Half-Pyramid Pattern:
* * * * * *
* * * * *
* * * *
* * *
* *
*
"""


def draw_downward_half_pyramid_pattern(n):
    for i in range(n, -1, -1):
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")


if __name__ == '__main__':
    user_input = int(input("Enter the number of rows to print: "))
    draw_downward_half_pyramid_pattern(user_input)
