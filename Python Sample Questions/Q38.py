""" Write a program to input ‘n’ numbers and separate the tuple in the following manner.
    Example:
        T=(1,2,3,4,5,6)
        Tl=(1,3,5)
        T2=(2,4,6)"""


tup = tuple()
len_tup = int(input("Enter len of tuple: "))

for i in range(len_tup):
    elements_of_tup = int(input("Enter the list of elements: "))
    tup = tup + (elements_of_tup,)
    tup1 = tup2 = tuple()

for i in tup:
    if i % 2 == 0:
        tup2 = tup2 + (i,)
    else:
        tup1 = tup1 + (i,)

print("tup is =", tup)
print("tup1 is = ", tup1)
print("tup2 is = ", tup2)
