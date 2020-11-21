""" Write a program to read a list of n integers and find their median.
    The median value of a list of values is the middle one when they are
    arranged in order. If there are two middle values then take their
    average."""


def medianValue(list1):
    list1.sort()
    indexes = len(list1)
    if (indexes % 2 == 0):
        num1 = (indexes) // 2
        num2 = (indexes // 2) + 1
        med = (list1[num1 - 1] + list1[num2 - 1]) / 2
        return med
    else:
        middle = (indexes - 1) // 2
        med = list1[middle]
        return med


list1 = list()
inp = int(input("How many elements do you want to add in the list? "))

for i in range(inp):
    a = int(input("Enter the elements: "))
    list1.append(a)

print("The median value is", medianValue(list1))
