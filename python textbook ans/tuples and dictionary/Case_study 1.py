def main():
    print("This is a small bank smimilator.")

    """print("Menu:")
    print("1) Open saveings bank account")
    print("2) Open Fixed Deposit account")"""

    fixed_deposit()

    """correct = False
    while not correct:
        option = int(input("Please enter your option: "))
        if option == 1:
            correct = True
            savings_account()
        elif option == 2:
            correct = True
            fixed_deposit()
        else:
            print("Wrong Input!")
            correct = False"""


def fixed_deposit():
    print("Fixed Deposit")
    print("Please specify the time duration for the fixed deposit: ")
    print("1) 0-30      days,   interest - 5.00%")
    print("2) 30-90     days,   interest - 5.20%")
    print("3) 90-180    days,   interest - 5.50%")
    print("4) 180-270   days,   interest - 5.75%")
    print("5) 270-365   days,   interest - 6.00%")
    print("6) 1-2       years,  interest - 5.75%")
    print("7) 2-5       years,  interest - 5.50%")
    print("8) 5-10      years,  interest - 5.25%")

    info_dic = {1: "30 5.00",
                2: "90 5.20",
                3: "180 5.50",
                4: "270 5.75",
                5: "365 6",
                6: "730 5.75",
                7: "1825 5.50",
                8: "3650 5.25"}

    correct = False
    while not correct:
        option = int(input("Please enter your option: "))
        if 1 > option > 8:
            correct = False
        else:
            correct = True

    info = info_dic.get(option).split(" ")
    duration = int(info[0])
    interest = float(info[1])

    account_info = {"account name": str(input("Please enter your name: ")),
                    "account_type": 'FD', "duration": duration, "interest": interest,
                    'deposit': float(input("Please enter the amount you want to deposit: "))}

    money_after_interest = float((account_info.get("deposit")) + (account_info.get("deposit")
                                                                  * (account_info.get("duration") / 365)
                                                                  * account_info.get("interest")) / 100)

    print("After {0} days..., you now have now {1} money in your your account"
          .format(account_info.get("duration"),
                  money_after_interest))


main()
