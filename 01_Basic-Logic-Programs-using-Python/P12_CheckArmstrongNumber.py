# Author: KEDAR BHARTIYA[appsec-samurai]
# Description: This program determine whether the number is Armstrong number or not.
# Summary: A positive integer is called an Armstrong number of order n if,
# abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + ....

def check_armstrong(number):
    # Changed num variable to string, and calculated the length (number of digits)
    lengthOfNumber = len(str(number))

    # initialize the sum
    sum = 0

    # find the sum of the power of each digit
    temp = number
    while temp > 0:
       digit = temp % 10
       sum += digit ** lengthOfNumber
       temp //= 10

    # display the result
    if number == sum:
        print("Given number", number, "is an Armstrong number")
    else:
        print("Given number", number, "is not an Armstrong number")


if __name__ == "__main__":
    userInput = int(input("Enter the number to check whether it is Armstrong or not: "))
    check_armstrong(userInput)
