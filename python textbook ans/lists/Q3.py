"""Write a function that returns the largest element of the list passed as parameter."""


def largestNum(list1):
    l = max(list1)
    return l


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

max_num = largestNum(list1)
print("The elements of the list", list1)

print("\nThe largest number of the list:", max_num)
