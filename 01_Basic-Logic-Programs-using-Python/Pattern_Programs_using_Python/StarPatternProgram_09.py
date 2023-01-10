# Author: KEDAR BHARTIYA[appsec-samurai]
"""
Program to demonstrate Diamond Pattern:
        *
       * *
      * * *
     * * * *
    * * * * *
   * * * * * *
    * * * * *
     * * * *
      * * *
       * *
        *
"""


def draw_diamond(n):
    k = 2 * n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")
    k = n - 2
    for i in range(n, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")


if __name__ == '__main__':
    user_input = int(input("Enter the number of rows to print: "))
    draw_diamond(user_input)
