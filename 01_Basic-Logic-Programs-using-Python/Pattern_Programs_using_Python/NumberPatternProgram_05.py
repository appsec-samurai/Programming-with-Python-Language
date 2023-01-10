# Author: KEDAR BHARTIYA[appsec-samurai]
"""
Program to demonstrate printing pattern of numbers like this:
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""


def print_desc_order_num_triangle(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")

        print("")


if __name__ == '__main__':
    user_input = int(input("Enter the number of rows to print: "))
    print_desc_order_num_triangle(5)