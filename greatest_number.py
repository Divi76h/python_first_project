def greatestNumber(arr, length):
    maximum = arr[0]
    for a in range(1, length):
        if arr[a] > maximum:
            maximum = arr[a]
    return maximum


arr = input("Enter array of numbers\n").split()
length = len(arr)
maxNum = greatestNumber(arr, length)
print("The greatest number is : {0}".format(maxNum))
