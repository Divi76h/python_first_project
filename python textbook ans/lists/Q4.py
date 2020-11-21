"""Write a function to return the second largest number from a list of numbers."""


def secLargestNum(list1):
    list1.sort()
    secondLast = list1[-2]
    return secondLast


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sec_num = secLargestNum(list1)

print("The elements of the list", list1)
print("\nThe second-largest number of the list:", sec_num)
