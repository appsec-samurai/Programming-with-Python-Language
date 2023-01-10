# Author: KEDAR BHARTIYA[appsec-samurai]
# Description: This program checks if a Number is given number is prime or not

def check_prime(number):
    """This function checks for prime number"""
    isPrime = False
    if number == 2:
        print(number, 'is a Prime Number')
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                print(number, 'is not a Prime Number')
                isPrime = False
                break
            else:
                isPrime = True

        if isPrime:
            print(number, 'is a Prime Number')


if __name__ == "__main__":
    userInput = int(input("Enter a number to check: "))
    check_prime(userInput)

