import os

#a = append
#r = read
# w = over write
# x = creates a file
# os.remove = removes a file (deletes it)

# flie is being created

if os.path.exists("file.txt"):
    print("it exists")

else:
    print("it dosent exist")

x = open("file.txt", "x")
# flie is being appended
x = open("file.txt", "a")
x.write("flie created")
x.close()

if os.path.exists("file.txt"):
    print("it exists")

else:
    print("it dosent exist")

x = open("file.txt", "r")
print(x.read())
x.close()

x = open("file.txt", "a")
x.write("yolo")
x.close()

x = open("file.txt", "r")
print(x.read())
x.close()

x = open("file.txt", "w")
x.write("opps!")
x.close()

x = open("file.txt", "r")
print(x.read())
x.close()

os.remove("file.txt")

if os.path.exists("file.txt"):
    print("it exists")

else:
    print("it dosent exist")
