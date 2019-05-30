time = input(
    "\nPlease enter time in 12hr format (in this hh:mm:ss manner) : ").split(":")
hr = int(time[0])
mint = int(time[1])
sec = int(time[2])
x = input("AM/PM ? : ").lower()

if x == "am":
    if hr == 12:
        hr = 0

    print("Your time in 24hr format is {0:02d}:{1}:{2} hrs".format(
        hr, mint, sec))

elif x == "pm":
    hr += 12

    print("Your time in 24hr format is {0:02d}:{1}:{2} hrs".format(
        hr, mint, sec))

else:
    print("Invalid Input")
