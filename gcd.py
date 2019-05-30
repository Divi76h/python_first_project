def gcd(a, b):
    if a == 0:
        return b

    return gcd(b % a, a)


a = input()
b = input()
a = int(a)
b = int(b)

print("gcd(", a, ",", b, ") = ", gcd(a, b))
