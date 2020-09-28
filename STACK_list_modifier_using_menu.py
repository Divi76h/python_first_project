# WA menu based Python program to execute the following operations (options)
# on a Python List STACK containing integers:
#   1. Display all the elements of the List STACK
#   2. Add one new element at the beginning of the List STACK
#   3. Remove the first element of the List STACK, if not empty AND also display the deleted element.
# Divij Kapoor S6-C date: 28 aug


def display_stack():

    print(STACK)
    main()


def add_element_to_stack():

    element = int(input("Pls enter an element to add to stack: "))
    print("Added the element")
    STACK.insert(0, element)
    main()


def delete_first_element_of_stack():

    if len(STACK) == 0:
        print("STACK is empty")
        main()
    else:
        STACK.remove(STACK[0])
        print("First element has bee removed from STACK")
        main()

def quit():

    print("\nThank you for using the program")

def main():

    print("menu\n")
    print("1) Display all te elements of STACK")
    print("2) Add an elements to STACK")
    print("3) Delete the first element of STACK")
    print("4) quit")

    option = int(input("pls enter your option: "))

    if option == 1:
        display_stack()
    elif option == 2:
        add_element_to_stack()
    elif option == 3:
        delete_first_element_of_stack()
    elif option == 4:
        quit()
    else:
        print("Wrong option")
        main()

STACK = []
print("\nThis is a menu based STACK list modifier\n")
main()
