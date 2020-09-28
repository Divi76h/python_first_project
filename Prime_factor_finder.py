# WAPP to find the prime factors of a natural number inputted
# Divij Kapoor S6-C date: 28 aug

import math


def primeFactors(natural_number):

    while natural_number % 2 == 0:
        print("2")
        natural_number = natural_number / 2
    for i in range(3, int(math.sqrt(natural_number)) + 1, 2):
        while natural_number % i == 0:
            print(i)
            natural_number = natural_number / i
    if natural_number > 2:
        print(natural_number)

natural_number = int(input("Pls enter a natural number: "))
print("Prime factors are: ")
primeFactors(natural_number)
