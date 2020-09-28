####### SYLLABUS:: Dictionary
'''
Creation, Accessing elements of a dictionary,
add an item,
modify an item in a dictionary;
Traversal,
functions/methods -
len(), dict(), keys(), values(), items(),
get(), update(),
del(), del, clear(), pop(), popitem(),
fromkeys(), copy(), setdefault(),
max(), min(),
sorted()
copy();
count the number of times a character appears in a given string using a dictionary,
create a dictionary with names of employees, their salary and access them.
'''

####### Creation, Accessing elements of a dictionary
####### Functions/methods - dict()
####### Add an item
####### Modify an item in a dictionary
'''
D=dict()   # OR D1={}
for i in range(3):
    Name=input("Enter name of the student: ")
    Marks=int(input("Enter the marks scored by "+Name+": "))
    D[Name]=Marks  
print(D)
print("Enter details of one new student and one existing student:")
for i in range(2):
    Name=input("Enter name of the student: ")
    Marks=int(input("Enter the marks scored by "+Name+": "))
    D[Name]=Marks
print(D)
'''

####### Functions/methods - len(), keys(), values(), items()
'''
D1={"Ajay":67,"Raj":56,"Kareena":77}
print(D1)

for K in D1.keys():
    if K=="Raj":
        print(K," has scored ",D1[K])

for V in D1.values():
    print(V)

for I in D1.items():  #[("Ajay",67),("Raj",56),("Kareena",77}]
    print(I)  ##
    print(I[0]," has scored ",I[1])
'''

####### Traversal
'''
D={"Ajay":67,"Raj":16,"Kareena":77}
Pass=0
Fail=0
for K in D.keys():
    if D[K]>=33:
        Pass+=1
    else:
        Fail+=1
print("Total number of students passed: ",Pass)
print("Total number of students failed: ",Fail)
'''


####### Functions/methods - get(), update()
'''
D={"Ajay":67,"Raj":16,"Kareena":77}
print(D["Ajay"])
#print(D["Rahim"])

print(D.get("Ajay"))
print(D.get("Rahim"))

print(D.get("Rahim", "Key doesn't exist!"))

E={"Raj":56,"Rahim":55}
print("Updating ",D," with ",E)
D.update(E)
print("Updated Dictionary: ",D)
'''

####### Functions/methods - del(), del, clear()
'''
D={"Ajay":67,"Raj":16,"Kareena":77}
print("Dictionary before deletion: ",D)
del(D["Raj"])
print("Dictionary after deletion: ",D)
del(D)
#print("Dictionary after deletion: ",D)
print("\n\n")


D={"Ajay":67,"Raj":16,"Kareena":77}
print("Dictionary before clear: ",D)
D.clear()
print("Dictionary after clear: ",D)
print("\n\n")
'''

####### Functions/methods - pop(), popitem()
'''
D={"Ajay":67,"Raj":16,"Kareena":77,"Vishal":88,"John":87}
print("Original Dictionary: ",D)
D.pop("Raj")
print("Dictionary after deletion: ",D)

print(D.pop("Ajay")," has been poped")
print("Dictionary after deletion 1",D)
print(D.popitem()," has been poped")
print("Dictionary after deletion: ",D)
'''

####### Functions/methods - fromkeys()
'''
L=["Ajay","Raj","Vishal"]

VAL=[1,2]

D1=dict.fromkeys(L)
print("Original Dictionary D1: ",D1)

D2=dict.fromkeys(L,0)
print("Original Dictionary D2: ",D2)

D3=dict.fromkeys(L,VAL)
print("Original Dictionary D2: ",D3)

VAL.append(3)
print("Original Dictionary D2: ",D3)

print("\n\n")
'''

####### Functions/methods - copy()
'''
D1={"Ajay":67,"Raj":16,"Kareena":77}

D2=D1

D2["Raju"]=99

print("Original dictionary: ",D1)

D3=D1.copy()

D3["Rajesh"]=88

print("Original dictionary: ",D1)
print("Copied dictionary: ",D3)
'''

####### Functions/methods - setdefault()
'''
D={"Ajay":67,"Raj":16,"Kareena":77}
print(D["Raj"])
#print(D["Raju"])

print(D.setdefault("Raj"))
print(D.setdefault("Raju"))
print(D.setdefault("Rajesh",100))

print("Updated Dictionary: ",D)
'''

####### Functions/methods - max(), min()
'''
D={"Ajay":67,"Raj":16,"Kareena":77}
print("Original Dictionary: ",D)

print("\n\n")
print("Max Keys: ", max(D))
print("Keys with Max Values: ", max(D,key=D.get))
print("Keys with Max Values: ", max(D, key= lambda x: D[x]))

print("\n\n")
print("Min Keys: ", min(D))
print("Keys witth Min values: ", min(D,key=D.get))
print("Keys witth Min values: ", min(D,key= lambda x: D[x]))
'''

####### Functions/methods - sorted()
'''
D={"Ajay":67,"Raj":16,"Kareena":77}
print("Orinal Dictionary: ",D)
print("Default sorted Dictionary: ",sorted(D))
print("Dictionary Sorted on Keys: ",sorted(D.keys()))
print("Dictionary Sorted on values: ",sorted(D.values()))
print("Dictionary Sorted on items-keys: ",sorted(D.items()))
print("Dictionary Sorted on items-Values: ",sorted(D.items(),key=lambda x: x[1]))
print("Dictionary Sorted on items-values: ",sorted(D.items(),key=lambda x: x[1], reverse=True))
'''

####### Count the number of times a character appears in a given string using a dictionary
'''
STR="MISSISSIPPI"
D={}   
for Ch in STR:
    if Ch in D.keys():
        D[Ch]+=1
    else:
        D[Ch]=1
print(D)
Ch=input("Enter the character whose frequency you want to find: ")
if Ch in D.keys():
    print(Ch," belongs to ",STR, " and appears ",D[Ch]," times.")
else:
    print(Ch," doesn't belong to ",STR)
'''

####### Create a dictionary with names of employees, their salary and access them.
'''
Employee=dict()
N=int(input("Enter the numbeer of employees: "))
for i in range(N):
    Name=input("Enter name of the employee: ")
    Salary=int(input("Enter the salary of "+Name+": "))
    Employee[Name]=Salary

print(Employee)

KeyMax=max(Employee,key=Employee.get)
print(Employee[KeyMax], " is the maximum salary earned by ",KeyMax)

KeyMin=min(Employee,key=Employee.get)
print(Employee[KeyMin], " is the maximum salary earned by ",KeyMin)

AveSalary=sum(Employee.values())/len(Employee)
print("Averahe Salary earned by the employees = ",AveSalary)
'''






























































a=input()
