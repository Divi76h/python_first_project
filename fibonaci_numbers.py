
def Fibonacci(n, count):
    count += 1
    print("count {0}".format(count))
    if n < 0:
        print("Incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1, count)+Fibonacci(n-2, count)


a = input("enter the numbers of fibonaci numbers you want : ")
a = int(a)
count = 0
print(Fibonacci(a, count))
