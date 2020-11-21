""" Write a program to read email IDs of n number of
    students and store them in a tuple. Create two new
    tuples, one to store only the usernames from the
    email IDs and second to store domain names from
    the email ids. Print all three tuples at the end of the
    program."""

emails = tuple()
username = tuple()
domainname = tuple()

n = int(input("How many email ids you want to enter?: "))
for i in range(0, n):
    emid = input("> ")
    emails = emails + (emid,)
    spl = emid.split("@")
    username = username + (spl[0],)
    domainname = domainname + (spl[1],)

print("\nThe email ids in the tuple are:")
print(emails)

print("\nThe username in the email ids are:")
print(username)

print("\nThe domain name in the email ids are:")
print(domainname)

name = tuple()
n = int(input("How many names do you want to enter?: "))
for i in range(0, n):
    num = input("> ")
    name = name + (num,)

print("\nThe names entered in the tuple are:")
print(name)

search = input("\nEnter the name of the student you want to search? ")

if search in name:
    print("The name", search, "is present in the tuple")
else:
    print("The name", search, "is not found in the tuple")
