def main():
    print("e = encode")
    print("d = decode")
    print("q = quit")

    option = input("what do you want to do : ")
    option = str(option)
    if option == "e":
        print("you have chosen to encode")
        a = str(input("enter a string to encode : ")).lower()
        b = int(input("enter rotation (1 - 25) : "))
        print("encoded word =", encode(a, b))
        quit()
    elif option == "d":
        print("you have chosen to decode")
        decode()
        quit()
    elif option == "q":
        quit()
    else:
        print("wrong input")
        main()


def encode(str1, rot):
    if (rot < 1 or rot > 25):
        print("wrong rotation")
        main()
    str2 = "abcdefghijklmnopqrstuvwxyz"
    str3 = ""
    length = len(str1)
    pos = 0
    pos = int(pos)
    for i in range(0, int(length)):
        if str1[i] == " ":
            str3 = str3 + str1[i]
        else:
            pos = str2.find(str1[i])
            str3 = str3 + str2[(pos + rot) % 25]
    return str3


def decode():
    str4 = str(input("give me a string to decode : ")).lower()
    str5 = str(input("give me the first decoded word : "))
    for j in range(1, 25, 1):
        if str(encode(str5, j)) in str4:
            break
    print("decoded word =", encode(str4, 25-j))


def quit():
    x = input("do you want to quit yes/no : ").lower()
    x = str(x)
    if x == "yes":
        print("thank you")
    elif x == "no":
        main()
    else:
        print("wrong input")
        main()


main()
