def solveEquation(equation):

    n = len(equation)
    sign = 1
    coeff = 0
    total = 0
    i = 0

    # Traverse the equation
    for j in range(0, n):

        if (equation[j] == '+' or
                equation[j] == '-'):

            if (j > i):
                total = (total + sign *
                         int(equation[i: j]))
            i = j

        # For cases such
        # as: x, -x, +x
        elif (equation[j] == 'x'):

            if ((i == j) or
                    equation[j - 1] == '+'):
                coeff += sign
            elif (equation[j - 1] == '-'):
                coeff = coeff - sign
            else:
                coeff = (coeff + sign *
                         int(equation[i: j]))
            i = j + 1

        # Flip sign once
        # '=' is seen
        elif (equation[j] == '='):

            if (j > i):
                total = (total + sign *
                         int(equation[i: j]))
            sign = -1
            i = j + 1

    # There may be a number
    # left in the end
    if (i < n):
        total = (total + sign *
                 int(equation[i: len(equation)]))

    # For infinite solutions
    if (coeff == 0 and
            total == 0):
        return "Infinite solutions"

    # For no solution
    if (coeff == 0 and total):
        return "No solution"

    # x = total sum / coeff of x
    # '-' sign indicates moving
    # numeric value to right hand side
    ans = -total / coeff
    return int(ans)


# Driver code
equation = input()
print("x = {0}" .
      format(solveEquation(equation)))

# This code is contributed by
# Manish Shaw(manishshaw1)
