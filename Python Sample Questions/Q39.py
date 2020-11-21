""" Write a program to input ‘n’ employees’ salary and
    find minimum & maximum salary among ‘n’ employees."""

t = tuple()
n = int(input("Enter total number of employees: "))

for i in range(n):
    a = input("Enter salary of employee {}: ".format(i + 1))
    t = t + (a,)

    print("maximum salary amongst all employees: ", max(t))
    print("minimum salary amongst all employees: ", min(t))
