# Author: KEDAR BHARTIYA[appsec-samurai]
"""
Program to demonstrate printing pattern of numbers like this:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""


def print_num_pattern(n):
    # initialising starting number
    num = 1

    # outer loop to handle number of rows
    for i in range(0, n):

        # re assigning num
        num = 1

        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i + 1):
            # printing number
            print(num, end=" ")

            # incrementing number at each column
            num = num + 1

        # ending line after each row
        print("\r")


if __name__ == '__main__':
    user_input = int(input("Enter the number of rows to print: "))
    print_num_pattern(user_input)
