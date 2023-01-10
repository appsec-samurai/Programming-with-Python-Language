# Author: KEDAR BHARTIYA[appsec-samurai]
"""
Program to demonstrate Pascal’s Triangle Program:
Summary: Pascal’s triangle is a pattern of the triangle which is based on nCr, below is the
      1
     1 1
    1 2 1
   1 3 3 1
  1 4 6 4 1
"""


def print_pascal_triangle(n):
    for i in range(1, n + 1):
        for j in range(0, n - i + 1):
            print(' ', end='')

        # first element is always 1
        C = 1
        for j in range(1, i + 1):
            # first value in a line is always 1
            print(' ', C, sep='', end='')

            # using Binomial Coefficient
            C = C * (i - j) // j
        print()


if __name__ == '__main__':
    user_input = int(input("Enter the number of rows to print: "))
    print_pascal_triangle(user_input)