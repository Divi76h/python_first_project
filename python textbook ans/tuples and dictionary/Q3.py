""" Write a Python program to find the highest 2 values
    in a dictionary."""

import random

dic = {"A": random.randint(0, 100), "B": random.randint(0, 100), "C": random.randint(0, 100),
       "D": random.randint(0, 100), "E": random.randint(0, 100), "F": random.randint(0, 100),
       "G": random.randint(0, 100), "H": random.randint(0, 100), "I": random.randint(0, 100),
       "J": random.randint(0, 100)}
print("\nThe dictionary is:", dic, "\n")

lst = list()
for a in dic.values():
    lst.append(a)
lst.sort()

key_of_max = list(dic.keys())[list(dic.values()).index(lst[-1])]
key_of_second_max = list(dic.keys())[list(dic.values()).index(lst[-2])]

print("Highest value is of '{0}': {1}".format(key_of_max, lst[-1]))
print("Second highest value is of '{0}': {1}".format(key_of_second_max, lst[-2]))
