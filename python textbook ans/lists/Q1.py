"""Write a program to find the number of times an element occurs in the list."""
import random

list1 = list()
inp = int(input("How many elements do you want to add in the list? "))

for i in range(inp):
    a = random.randint(0, 10)
    list1.append(a)

print("The list is:", list1)
inp = int(input("Which element occurrence would you like to count? "))

count = list1.count(inp)

print("The count of element", inp, "in the list is:", count)
