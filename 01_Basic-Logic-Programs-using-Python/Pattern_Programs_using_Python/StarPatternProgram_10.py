# Author: KEDAR BHARTIYA[appsec-samurai]
"""
Program to demonstrate Hollow diamond Pattern:
  *
 * *
*   *
 * *
  *
"""


def draw_hollow_diamond(n):

    for i in range(5):
        for j in range(5):
            if i + j == 2 or i - j == 2 or i + j == 6 or j - i == 2:
                print("*", end="")
            else:
                print(end=" ")
        print()


if __name__ == '__main__':
    user_input = int(input("Enter the number of rows to print: "))
    draw_hollow_diamond(user_input)
