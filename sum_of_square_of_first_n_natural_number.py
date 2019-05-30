def squaresum(n):
    return (n * (n + 1) * (2 * n + 1)) // 6


n = input()
n = int(n)
print(squaresum(n))
