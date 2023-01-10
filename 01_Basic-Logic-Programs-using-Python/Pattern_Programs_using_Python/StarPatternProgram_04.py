# Author: KEDAR BHARTIYA[appsec-samurai]
"""
Program to demonstrate printing pattern like this:
* * * * * *
 * * * * *
  * * * *
   * * *
    * *
     *
"""


def draw_reverse_triangle_pattern(n):
    k = 2 * n - 2
    for i in range(n, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print("*", end=" ")
        print("\r")


if __name__ == '__main__':
    user_input = int(input("Enter the number of rows to print: "))
    draw_reverse_triangle_pattern(user_input)
