def pattern(n):
    
    for i in range(0, n):

        for a in range(n, i, -1):
            print("* ",end="")
        
        print("\r")

n = input("please enter the number of lines : ")
n = int(n)
pattern(n)