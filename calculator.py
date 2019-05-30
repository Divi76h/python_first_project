print("calculator\navailable operations\n1) +\n2) -\n3) *\n4) /\n5) modulus(%)")
print("6)square of both the numbers\n7)cube of both the numbers")

num1 = input("enter first number : ")
num2 = input("enter second number : ")

opt = input("enter the operation you want to preform: ")
value = 0

if (opt == '+' or opt == "1"):
    value = float(num1) + float(num2)

elif (opt == '-' or opt == "2"):
    value = float(num1) - float(num2)

elif (opt == '*' or opt == "3"):
    value = float(num1) * float(num2)

elif (opt == '/' or opt == "4"):
    value = float(num1) / float(num2)

elif (opt == '%' or opt == "5"):
    value = float(num1) % float(num2)

elif opt == "6":
    value = float(num2) * float(num2)
    value2 = float(num1) * float(num1)
    print(value2)

elif opt == "7":
    value = float(num2) * float(num2) * float(num2)
    value2 = float(num1) * float(num1) * float(num1)
    print(value2)


print(value)
