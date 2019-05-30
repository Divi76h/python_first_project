x = input().split(",")
y = len(x)

List = []

for i in range(0, y):
    List.append(x[i])

max = max(List[0], List[1])
secondmax = min(List[0], List[1])

for n in range(2, y):
    if List[n] > max:
        secondmax = max
        max = List[n]
    else:
        if List[n] > secondmax:
            secondmax = List[n]

print("Second largest number is : {0}".format(secondmax))
