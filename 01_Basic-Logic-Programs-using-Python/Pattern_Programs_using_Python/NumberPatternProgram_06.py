# Author: KEDAR BHARTIYA[appsec-samurai]
"""
Program to demonstrate printing pattern of numbers like this:
        10
       1010
      101010
     10101010
    1010101010
"""


def print_binary_num_pattern(n):
    k = 2 * n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print('10', end="")

        print("")


pattern(5)