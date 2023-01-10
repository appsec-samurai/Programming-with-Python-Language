# Author: KEDAR BHARTIYA[appsec-samurai]
"""
Program to demonstrate printing diamond pattern of numbers like this:
      1
     2 2
    3 3 3
   4 4 4 4
  5 5 5 5 5
   4 4 4 4
    3 3 3
     2 2
      1
"""


def print_diamond_num_pattern(n):
    k = 2 * n - 2
    x = 0
    for i in range(0, n):
        x += 1
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print(x, end=" ")
        print("")
    k = n - 2
    x = n + 2
    for i in range(n, -1, -1):
        x -= 1
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print(x, end=" ")
        print("")


if __name__ == '__main__':
    user_input = int(input("Enter the number of rows to print: "))
    print_diamond_num_pattern(user_input)
