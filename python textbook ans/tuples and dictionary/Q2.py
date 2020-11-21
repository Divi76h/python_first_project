""" Write a program to input names of n students and
    store them in a tuple. Also, input a name from the
    user and find if this student is present in the tuple or not."""

def searchStudent(tuple1, search):
    for a in tuple1:
        if a == search:
            print("The name", search, "is present in the tuple")
            return
    print("The name", search, "is not found in the tuple")


name = tuple()
n = int(input("How many names do you want to enter?: "))
for i in range(0, n):
    num = input("> ")
    name = name + (num,)

print("\nThe names entered in the tuple are:")
print(name)
search = input("\nEnter the name of the student you want to search? ")
searchStudent(name, search)
