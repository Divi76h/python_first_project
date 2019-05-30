a = input("enter first digit : ")
b = input("enter second digit : ")

a = int(a)
b = int(b)

print("\na = {0}".format(a))
print("b = {0}".format(b))


a = a + b  # a has both the values
b = a - b  # now b has the original value of a (a + b - b = a)
a = a - b  # now a has the original value of b (a + b - a = b)

print("\na = {0}".format(a))
print("b = {0}".format(b))
