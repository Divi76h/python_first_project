""" Input a string having some digits. Write a function
    to return the sum of digits present in this string."""

def sumDigit(string):
    sum = 0
    for a in string:
        if (a.isdigit()):
            sum += int(a)
    return sum


userInput = input("Enter any string with digits: ")

result = sumDigit(userInput)

print("The sum of all digits in the string '", userInput, "' is:", result)
