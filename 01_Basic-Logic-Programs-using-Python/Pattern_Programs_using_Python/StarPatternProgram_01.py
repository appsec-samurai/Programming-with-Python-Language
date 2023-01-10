# Author: KEDAR BHARTIYA[appsec-samurai]
"""
Program to demonstrate printing pattern like this:
*
* *
* * *
* * * *
* * * * *
"""

# Scenario 1:
"""Using for loops"""


def draw_pattern(n):
    # outer loop to handle number of rows
    # n in this case
    for i in range(0, n):
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i + 1):
            # printing stars
            print("* ", end="")
        # ending line after each row
        print("\r")


if __name__ == '__main__':
    user_input = int(input("Enter the number of rows to print: "))
    draw_pattern(user_input)


# Scenario 2:
"""Using Lists"""


def draw_pattern(n):
    pattern_list = []
    for i in range(1, n+1):
        pattern_list.append("*"*i)
    print("\n".join(pattern_list))


if __name__ == '__main__':
    user_input = int(input("Enter the number of rows to print: "))
    draw_pattern(user_input)
