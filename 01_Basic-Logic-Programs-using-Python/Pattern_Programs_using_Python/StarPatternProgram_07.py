# Author: KEDAR BHARTIYA[appsec-samurai]
"""
Program to demonstrate Hourglass Pattern:
* * * * *
 * * * *
  * * *
   * *
    *
   * *
  * * *
 * * * *
* * * * * 
"""


def draw_hourglass_pattern(n):
    # for loop for printing upper half
    for i in range(1, n + 1):
        # printing i spaces at the beginning of each row
        for k in range(1, i):
            print(" ", end="")
        # printing i to rows value at the end of each row
        for j in range(i, n + 1):
            print("*", end=" ")
        print()
    # for loop for printing lower half
    for i in range(n - 1, 0, -1):
        # printing i spaces at the beginning of each row
        for k in range(1, i):
            print(" ", end="")
        # printing i to rows value at the end of each row
        for j in range(i, n + 1):
            print("*", end=" ")
        print()


if __name__ == '__main__':
    user_input = int(input("Enter the number of rows to print: "))
    draw_hourglass_pattern(user_input)
