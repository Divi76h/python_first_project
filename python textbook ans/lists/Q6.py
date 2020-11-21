""" Write a program to read a list of elements. Modify this list so that
    it does not contain any duplicate elements, i.e., all elements occurring
    multiple times in the list should appear only once."""


def removeDup(list1):
    length = len(list1)
    newList = []
    for a in range(length):
        if list1[a] not in newList:
            newList.append(list1[a])
    return newList


list1 = []
inp = int(input("How many elements do you want to add in the list? "))

for i in range(inp):
    a = int(input("Enter the elements: "))
    list1.append(a)

print("The list entered is:", list1)
print("The list without any duplicate element is:", removeDup(list1))
