""" Read a list of n elements.
    Pass this list to a function
    which reverses this list in-place
    without creating a new list."""


def reverseList():
    global list1
    list1.reverse()
    print("Reversed List:", list1)


list1 = list()
inp = int(input("How many elements do you want to add in the list? "))

for i in range(inp):
    a = int(input("Enter the elements: "))
    list1.append(a)

print("The list entered is:", list1)

reverseList()
