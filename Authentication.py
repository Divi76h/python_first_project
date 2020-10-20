import os
import json


def signup(readFile):
    print("\nSignup")

    username = input("Enter Username : ")
    password = input("Enter Password (min length is 5 letters) : ")
    confirm = input("Please confirm password : ")

    while len(password) < 5:

        password = input("Enter Password (min length is 5 letters) : ")

    while password != confirm:

        confirm = input("The confirmed password is wrong please re-enter : ")

    data = {}
    data['users'] = []

    if os.stat("database.json").st_size != 0:

        data = json.loads(readFile.read())

        for user in data["users"]:

            if user['username'] == username:

                print("Username is taken")

                main()

        writeFile = open("database.json", 'w')

        data["users"].append({
            'username': username,
            'password': password
        })

        writeFile.write(json.dumps(data))
        print("User registered")

        writeFile.close()
        main()

    else:

        writeFile = open("database.json", 'w')

        data['users'].append({
            'username': username,
            'password': password
        })
        writeFile.write(json.dumps(data))
        print("User registered")

        writeFile.close()
        main()


def login(readFile):

    print("\nLogin")

    username = input("Please enter Username : ")
    password = input("Please enter Password : ")

    if os.stat("database.json").st_size == 0:

        print("Please Signup first")
        main()

    else:

        data = json.loads(readFile.read())

        isLoggedin = False
        loggedInUser = {}

        for user in data["users"]:

            if (user["username"] == username and user["password"] == password):

                isLoggedin = True
                loggedInUser = user

        if isLoggedin == True:

            print("\nYou have successfully logged-in")
            print("\nWhat do you want to do")
            print("1) Change Password\n2) Delete Account\n3) Close")

            option = input("Please enter your option : ")
            option = int(option)

            if option == 1:

                changePassword(loggedInUser)

            elif option == 2:

                deleteAccount(loggedInUser)

            elif option == 3:

                close()

        else:

            print("The combination of username and password is wrong")

            main()


def changePassword(user):

    x = input("Please enter old password : ")
    x = str(x)

    if user["password"] == x:

        newpassword = input(
            "Please enter new password (min length is 5 letters) : ")
        newpassword = str(newpassword)

        while (len(newpassword) < 5 or newpassword == x):

            print("Invalid input please re-enter")
            newpassword = input(
                "Please enter new password (min length is 5 letters) :  ")

        confirm = input("Please confirm new password : ")

        while confirm != newpassword:

            confirm = input(
                "The confirmed password is wrong please re-enter : ")

        readFile = open("database.json", "r")
        data = json.loads(readFile.read())
        position = -1

        for index, usr in enumerate(data["users"]):

            if usr['username'] == user["username"]:
                position = index
                user["password"] = newpassword
                break

        data['users'].pop(position)
        data['users'].insert(position, user)
        writeFile = open("database.json", "w")
        writeFile.write(json.dumps(data))
        print("Password changed successfully")


def deleteAccount(user):

    readFile = open("database.json", "r")
    data = json.loads(readFile.read())

    option = input(
        "Do you realy want to delete your account\nYes or No : ").lower()
    option = str(option)

    if option == "yes":

        data["users"].remove(user)

        writeFile = open("database.json", "w")
        writeFile.write(json.dumps(data))
        writeFile.close()
        print("User successfully Deleted")

        main()

    else:

        main()


def close():

    option = input("Do you want to close\nYes or No : ").lower()
    option = str(option)

    if option == "yes":

        print("Thank you")

    if option == "no":

        main()


def main():

    readFile = open("database.json", "r")
    print("\nMenu\n1) Signup\n2) Login\n3) Close")

    x = input("please enter your option : ")
    x = int(x)

    if x == 1:

        signup(readFile)

    elif x == 2:

        login(readFile)

    elif x == 3:

        close()

    elif (x != 1 or x != 2):

        print("Incorrect Input")
        main()


if __name__ == "__main__":

    main()

else:

    print("This file is being imported")

    main()
