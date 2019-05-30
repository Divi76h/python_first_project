n = input("Enter Number to calculate sum : ")
n = int(n)

sum = 0

for a in range(0, n+1, 1):
    sum = sum + a

for a in range(1, n+1):
    print(a)

print("SUM of first {0} and number is {1}".format(n, sum))
