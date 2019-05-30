print("This is a simple program to find simple intrest")

principle = input("Please enter the amount : ")
time = input("Please eneter the time (in years) : ")
rate = input("please enter the rate (in % per anum/year) : ")
currency = input("please enter the currency : ")

time = int(time)
principle = float(principle)
rate = float(rate)
currency = str(currency)

SI = (time * principle * rate) / 100

print("The simple intrest with amount : {0}{1}, time : {2} years and rate : {3}% is {4}{5}".format(
    currency, principle, time, rate, currency, SI))
