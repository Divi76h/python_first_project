def solveEquation(equation):

    n = len(equation)
    sign = 1
    coeff = 0
    total = 0
    i = 0

    for j in range(0, n):

        if (equation[j] == '+' or
                equation[j] == '-'):

            if (j > i):
                total = (total + sign * float(equation[i: j]))
            i = j

        elif (equation[j] == 'x'):

            if ((i == j) or equation[j - 1] == '+'):
                coeff += sign
            elif (equation[j - 1] == '-'):
                coeff = coeff - sign
            else:
                coeff = (coeff + sign *
                         float(equation[i: j]))
            i = j + 1

        elif (equation[j] == '='):

            if (j > i):
                total = (total + sign * float(equation[i: j]))
            sign = -1
            i = j + 1

    if (i < n):
        total = (total + sign * float(equation[i: len(equation)]))

    if (coeff == 0 and total == 0):
        return "Infinite solutions"

    if (coeff == 0 and total):
        return "No solution"

    ans = -total / coeff
    return float(ans)

equation = input()
print("x = {0}" .format(solveEquation(equation)))
