import os


def signup():

    name = True

    while name == True:

        x = input("Please enter the name of the file : ")
        x = str(x)
        z = "{0}.txt".format(x)
        z = str(z)

        if os.path.exists(z):
            print("Sorry this name is taken")
            name = True

        else:
            name = False

    y = open("{0}".format(z), "x")

    username = input("Please enter Username : ")

    passwordIsCorrect = False

    while passwordIsCorrect == False:
        password = input("Please enter Password (min length is 5) : ")

        if len(password) > 4:
            passwordIsCorrect = True

        else:
            passwordIsCorrect = False

    y.write("{0} {1}".format(username, password))
    y.close()
    print("User Registered Successfully")
    main()


def login():

    x = input(
        "\nPlease enter the name of the file you entered when you signed up : ")
    x = str(x)
    t = "{0}.txt".format(x)
    t = str(t)

    if os.path.exists(t):

        z = open("{0}".format(t), "r")
        d = z.read().split(" ")

        user = str(d[0])
        passw = str(d[1])

        use = input("Enter the username : ")
        pas = input("Enter the password : ")

        if (user == use and passw == pas):
            print("You have successfully logged-in")

            print("\nWhat do you want to do")
            print("1) Change Password\n2) Change Username\n3) Delete Account\n4) Close")

            option = input("")

            if option == 1:
                x = input("Please enter the new password")

        else:
            print("The username or the password you entered is wrong")

    else:
        print("Wrong Name")


def main():

    print("menu\n1) Signup\n2) Login")

    option = input()
    option = int(option)

    if option == 1:
        signup()

    elif option == 2:
        login()

    else:
        print("Incorrect Input")


if __name__ == "__main__":
    main()

else:
    print("This file is being imported")
    main()
