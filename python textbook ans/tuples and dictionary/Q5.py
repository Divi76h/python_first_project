""" Write a program to input your friends’ names
    and their Phone Numbers and store them in the
    dictionary as the key-value pair. Perform the
    following operations on the dictionary:
    a)  Display the name and phone number of all your
        friends
    b)  Add a new key-value pair in this dictionary and
        display the modified dictionary
    c)  Delete a particular friend from the dictionary
    d)  Modify the phone number of an existing friend
    e)  Check if a friend is present in the dictionary or
        not
    f)  Display the dictionary in sorted order of names"""

dic = {}

while True:
    print("1. Add New Contact")
    print("2. Modify Phone Number of Contact")
    print("3. Delete a Friend's contact")
    print("4. Display all entries")
    print("5. Check if a friend is present or not")
    print("6. Display in sorted order of names")
    print("7. Exit")
    inp = int(input("Enter your choice(1-7): "))

    if inp == 1:
        name = input("Enter your friend name: ")
        phonenumber = input("Enter your friend's contact number: ")
        dic[name] = phonenumber
        print("Contact Added \n\n")
    elif inp == 2:
        name = input("Enter the name of friend whose number is to be modified: ")
        if name in dic:
            phonenumber = input("Enter the new contact number: ")
            dic[name] = phonenumber
            print("Contact Modified\n\n")
        else:
            print("This friend's name is not present in the contact list")
    elif inp == 3:
        name = input("Enter the name of friend whose contact is to be deleted: ")
        if name in dic:
            del dic[name]
            print("Contact Deleted\n\n")
        else:
            print("This friend's name is not present in the contact list")
    elif inp == 4:
        print("All entries in the contact")
        for a in dic:
            print(a, "\t\t", dic[a])
        print("\n\n\n")
    elif inp == 5:
        name = input("Enter the name of friend to search: ")
        if name in dic:
            print("The friend", name, "is present in the list\n\n")
        else:
            print("The friend", name, "is not present in the list\n\n")
    elif inp == 6:
        print("Name\t\t\tContact Number")
        for i in sorted(dic.keys()):
            print(i, "\t\t\t", dic[i])
        print("\n\n")
    elif inp == 7:
        break
    else:
        print("Invalid Choice. Please try again\n")
