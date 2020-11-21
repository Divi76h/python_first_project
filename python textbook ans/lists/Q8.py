""" Write a program to read elements of a list.
    a)  The program should ask for the position of
        the element to be deleted from the list. Write
        a function to delete the element at the desired
        position in the list.
    b)  The program should ask for the value of the element
        to be deleted from the list. Write a function to
        delete the element of this value from the list."""


# Program a)

def deleteElements():
    global list1
    inp = input("Do you want to delete any element from the list? (Y/N) ")
    if (inp == 'Y' or inp == 'y'):
        elem = int(input("Enter the element which you would like to delete: "))
        for a in list1:
            if (a == elem):
                list1.remove(elem)
        print("The element is deleted from the list. ")
        deleteElements()
    else:
        print("The elements in the list", list1)


list1 = []
inp = int(input("How many elements do you want to add in the list? "))

for i in range(inp):
    a = int(input("Enter the elements: "))
    list1.append(a)

print("The list entered is:", list1)
deleteElements()


def deleteElementsAtIndex():
    global list1
    inp = input("Do you want to delete any element from the list? (Y/N) ")
    if (inp == 'Y' or inp == 'y'):
        index = int(input("Enter the index of the element you would like to delete: "))
        if (index < len(list1)):
            list1.pop(index)
            print("The element is deleted from the list. ")
        else:
            print("The index is out of range.")

        deleteElementsAtIndex()
    else:
        print("The elements in the list", list1)


list1 = list()
inp = int(input("How many elements do you want to add in the list? "))

for i in range(inp):
    a = int(input("Enter the elements: "))
    list1.append(a)

print("The list entered is:", list1)

deleteElementsAtIndex()
