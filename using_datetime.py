import datetime

# date in yyyy/mm/dd format
for x in range(2020, 2100):
    d1 = datetime.datetime(x, 1, 1).weekday()
    d2 = datetime.datetime(x, 1, 13).weekday()
    d3 = datetime.datetime(x, 1, 26).weekday()
    d4 = datetime.datetime(x, 8, 15).weekday()
    d5 = datetime.datetime(x, 10, 2).weekday()
    d6 = datetime.datetime(x, 11, 14).weekday()
    d7 = datetime.datetime(x, 12, 25).weekday()
    if (d1 < 5) and (d2 < 5) and (d3 < 5) and (d4 < 5) and (d5 < 5) and (d6 < 5) and (d7 < 5):
        print(x, "all weekday, good")
    else:
        print(x, "all weekend, bad")
