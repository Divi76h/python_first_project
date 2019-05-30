import random

while True:
    print("\n\nNumber Guessing Game")
    print("\nTry your luck gusseing a number")
    print("\nHow to play:\n1) Enter a range\n2) Then enter a number")
    print("3) If the game says your number is greater, try to enter a smaller number")
    print("4) If the game says your number is smaller, try to enter a larger number")
    print("5) If you enter the same number, you win! ")
    print("6) If you want to exit the game at any moment, enter 'Ctrl + C' and then 'exit()'")
    print("\n Hint : the higher the range, the more chances you need to win")

    eq = False

    while (eq == False):
        print("\nPlease enter the range of the random number,")
        a = input("from 1 - ")

        try:
            a = int(a)
            if a <= 5:
                print("\nCome On!! Chose a bigger range")
            elif a > 5:
                eq = True
        except:
            print("Input must be numeric")

    random_num = int(random.randint(1, a))
    print("\nThe game has decided a random number from 1 - {0}".format(a))
    print("Now enter your guess")

    equal = False

    while (equal == False):
        value = input("\nEnter your number : ")
        try:
            value = int(value)
            if value == random_num:
                print("The the random number was : {0}".format(random_num))
                print("\nYOU WIN!")
                equal = True
                option = "No"
            elif value > random_num:
                print('Your number is greater than the random number, keep trying')
            elif value < random_num:
                print('Your number is smaller than the random number, keep trying')
        except:
            print("Input must be numberic. Please re-enter")
    print("Thank You for playing")
    print("\nDo you want to play again?")
    option = input("Yes/No : ")
    if (option == "Yes" or option == "yes"):
        continue
    else:
        print("\n\nGame Over!")
        print("Thank You")
        break
