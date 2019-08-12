import math


def isPrime(num):

    if (num < 2):
        return False

    else:
        for i in range(2, int(math.sqrt(num) + 1)):
            if num % i == 0:
                return False
        return True


num = input()
num = int(num)
isPrime(num)

if isPrime(num) == False:
    print(num, "it is not a prime number")

elif isPrime(num) == True:
    print(num, "it is a prime number")
