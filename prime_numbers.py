start = input(
    "give a starting number for the range to find the prime numbers : ")
end = input("give the end of the range : ")

print("The range is {0} - {1}".format(start, end))

start = int(start)
end = int(end)

for val in range(start, end + 1):
    if val > 1:
        for n in range(2, val):
            if (val % n) == 0:
                break
        else:
            print(val)
