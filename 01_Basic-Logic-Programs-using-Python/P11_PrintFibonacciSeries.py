# Author: KEDAR BHARTIYA[appsec-samurai]
# Description: This program calculates the fibonacci series till the n-th term
# Summary: A Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8....The first two terms are 0 and 1.
# All other terms are obtained by adding the preceding two terms.
# This means to say the nth term is the sum of (n-1)th and (n-2)th term.

# Scenario 1:
"""This function calculates the fibonacci series till the n-th term in Recursive manner"""

def fibonacci_with_recursion(number):
    if number <= 1:
        return number
    else:
        return (fibonacci_with_recursion(number - 1) + fibonacci_with_recursion(number - 2))

# Scenario 2:
"""This function calculates the fibonacci series till the n-th term in Iterative manner"""

def fibonacci_without_recursion(number):
    if number <= 0:
        print("Please enter a positive integer and greater than 0")
        return 0
    fib0, fib1 = 0, 1
    print(fib0, fib1, end=" ")
    for i in range(2, number):
        fib1, fib0 = fib0 + fib1, fib1
        print((fib1), end=" ")
    return fib1

# Scenario 3:
"""This function calculates the fibonacci series by creating an array in the function."""

def fibonacci_with_array(number):
    arr = [0] * (number + 1)
    arr[1] = 1

    for i in range(2, number + 1):
        arr[i] = arr[i - 1] + arr[i - 2]
    for i in arr:
        print((i), end=" ")


if __name__ == '__main__':
    userInput = int(input('Enter the number upto which you wish to calculate fibonacci series: '))
    # for i in range(userInput + 1):
    #     print(fibonacci_with_recursion(i), end=' ')

    # # Without Recursion
    fibonacci_without_recursion(userInput)
    # With Array
    # fibonacci_with_array(userInput)