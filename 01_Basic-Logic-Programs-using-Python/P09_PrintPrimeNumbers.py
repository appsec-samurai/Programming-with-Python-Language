# Author: KEDAR BHARTIYA[appsec-samurai]
# Description: This program prints all the prime numbers within an interval

def print_prime(low, up):
    print("Prime numbers between {0} and {1} are: ".format(low, up))

    for num in range(low, up + 1):
        # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)


if __name__ == "__main__":
    lowerRange = int(input("Enter the lower range: "))
    upperRange = int(input("Enter the upper range: "))
    print_prime(lowerRange, upperRange)
