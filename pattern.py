import time


def pattern(n):

    for i in range(0, n):

        for a in range(0, i+1):
            print("* ", end="")

        print("\r")


def patternupsidedown(n):

    for i in range(0, n):

        for a in range(n, i, -1):
            print("* ", end="")

        print("\r")


def triangle(n):

    k = 2*n - 2

    for i in range(0, n):

        for j in range(0, k):
            print(end=" ")

        k = k - 1

        for j in range(0, i+1):

            print("* ", end="")

        print("\r")


def numpat(n):

    num = 1

    for i in range(0, n):

        num = 1

        for j in range(0, i+1):

            print(num, end=" ")

            num = num + 1

        print("\r")


def doublesidedstair(n):

    for i in range(1, n+1):

        k = i + 1 if(i % 2 != 0) else i

        for g in range(k, n):
            if g >= k:
                print(end="  ")

        for j in range(0, k):
            if j == k - 1:
                print(" * ")
            else:
                print(" * ", end=" ")


print("\nHi\n\nWelcome to Pattern Printer\n\nOptions of patterns : \n1) Triangle pattern")
print("2) Right angle triangle\n3) Upside down Right angle triangle")
print("4) Number right angle triangle\n5) Double sided stair \n6) Print your own name")

option = input(
    "\nplease enter which pattern you want to print (use the serial number) : ")
option = int(option)

if option == 1:
    n = input("\nplease enter the number of lines : ")
    n = int(n)
    print("\n")
    print("Printing   \n")
    time.sleep(2)
    triangle(n)

elif option == 2:
    n = input("\nplease enter the number of lines : ")
    n = int(n)
    print("\n")
    print("Printing   \n")
    time.sleep(2)
    pattern(n)

elif option == 3:
    n = input("\nplease enter the number of lines : ")
    n = int(n)
    print("\n")
    print("Printing   \n")
    time.sleep(2)
    patternupsidedown(n)

elif option == 4:
    n = input("\nplease enter the number of lines : ")
    n = int(n)
    print("\n")
    print("Printing   \n")
    time.sleep(2)
    numpat(n)

elif option == 5:
    n = input("\nplease enter the number of lines (enter a even number) : ")
    n = int(n)
    print("\n")
    print("Printing   \n")
    time.sleep(2)
    doublesidedstair(n)

elif option == 6:
    name = input("Enter your name: \n")
    print("\n")
    print("Printing...\n")
    time.sleep(2)

    lngth = len(name)
    l = ""

    for x in range(0, lngth):
        c = name[x]
        c = c.upper()

        if (c == "A"):
            print("  ######  \n  #    #  \n  ######  ", end=" ")
            print("\n  #    #  \n  #    #  \n\n")

        elif (c == "B"):
            print("  ######  \n  #    #  \n  #####   ", end=" ")
            print("\n  #    #  \n  ######  \n\n")

        elif (c == "C"):
            print("  ######  \n  #       \n  #       ", end=" ")
            print("\n  #       \n  ######  \n\n")

        elif (c == "D"):
            print("  #####   \n  #    #  \n  #    #  ", end=" ")
            print("\n  #    #  \n  #####   \n\n")

        elif (c == "E"):
            print("  ######  \n  #       \n  #####   ", end=" ")
            print("\n  #       \n  ######  \n\n")

        elif (c == "F"):
            print("  ######  \n  #       \n  #####   ", end=" ")
            print("\n  #       \n  #       \n\n")

        elif (c == "G"):
            print("  ######  \n  #       \n  # ####  ", end=" ")
            print("\n  #    #  \n  #####   \n\n")

        elif (c == "H"):
            print("  #    #  \n  #    #  \n  ######  ", end=" ")
            print("\n  #    #  \n  #    #  \n\n")

        elif (c == "I"):
            print("  ######  \n    ##    \n    ##    ", end=" ")
            print("\n    ##    \n  ######  \n\n")

        elif (c == "J"):
            print("  ######  \n    ##    \n    ##    ", end=" ")
            print("\n  # ##    \n  ####    \n\n")

        elif (c == "K"):
            print("  #   #   \n  #  #    \n  ##      ", end=" ")
            print("\n  #  #    \n  #   #   \n\n")

        elif (c == "L"):
            print("  #       \n  #       \n  #       ", end=" ")
            print("\n  #       \n  ######  \n\n")

        elif (c == "M"):
            print("  #    #  \n  ##  ##  \n  # ## #  ", end=" ")
            print("\n  #    #  \n  #    #  \n\n")

        elif (c == "N"):
            print("  #    #  \n  ##   #  \n  # #  #  ", end=" ")
            print("\n  #  # #  \n  #   ##  \n\n")

        elif (c == "O"):
            print("  ######  \n  #    #  \n  #    #  ", end=" ")
            print("\n  #    #  \n  ######  \n\n")

        elif (c == "P"):
            print("  ######  \n  #    #  \n  ######  ", end=" ")
            print("\n  #       \n  #       \n\n")

        elif (c == "Q"):
            print("  ######  \n  #    #  \n  # #  #  ", end=" ")
            print("\n  #  # #  \n  ######  \n\n")

        elif (c == "R"):
            print("  ######  \n  #    #  \n  # ##   ", end=" ")
            print("\n  #   #   \n  #    #  \n\n")

        elif (c == "S"):
            print("  ######  \n  #       \n  ######  ", end=" ")
            print("\n       #  \n  ######  \n\n")

        elif (c == "T"):
            print("  ######  \n    ##    \n    ##    ", end=" ")
            print("\n    ##    \n    ##    \n\n")

        elif (c == "U"):
            print("  #    #  \n  #    #  \n  #    #  ", end=" ")
            print("\n  #    #  \n  ######  \n\n")

        elif (c == "V"):
            print("  #    #  \n  #    #  \n  #    #  ", end=" ")
            print("\n   #  #   \n    ##    \n\n")

        elif (c == "W"):
            print("  #    #  \n  #    #  \n  # ## #  ", end=" ")
            print("\n  ##  ##  \n  #    #  \n\n")

        elif (c == "X"):
            print("  #    #  \n   #  #   \n    ##    ", end=" ")
            print("\n   #  #   \n  #    #  \n\n")

        elif (c == "Y"):
            print("  #    #  \n   #  #   \n    ##    ", end=" ")
            print("\n    ##    \n    ##    \n\n")

        elif (c == "Z"):
            print("  ######  \n      #   \n     #    ", end=" ")
            print("\n    #     \n  ######  \n\n")

        elif (c == " "):
            print("      \n      \n      ", end=" ")
            print("\n      \n\n")

        elif (c == " "):
            print("----  ----\n\n")

elif (option > 6 or option < 1):
    print("Incorrect Input")
