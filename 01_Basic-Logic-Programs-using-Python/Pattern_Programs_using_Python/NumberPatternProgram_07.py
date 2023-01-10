# Author: KEDAR BHARTIYA[appsec-samurai]
"""
Program to demonstrate printing pattern of numbers like this:
          1
        1 2
      1 2 3
    1 2 3 4
  1 2 3 4 5
"""


def print_mirrored_num_triangle(n):
    for row in range(1, n):
        num = 1
        for j in range(n, 0, -1):
            if j > row:
                print(" ", end=" ")
            else:
                print(num, end=" ")
                num += 1
        print(" ")


if __name__ == '__main__':
    user_input = int(input("Enter the number of rows to print: "))
    print_mirrored_num_triangle(user_input)
