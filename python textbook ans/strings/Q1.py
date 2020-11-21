""" Write a program to input line(s) of text from the user
    until enter is pressed. Count the total number of
    characters in the text (including white spaces),total
    number of alphabets, total number of digits, total
    number of special symbols and total number of
    words in the given text. (Assume that each word is
    separated by one space)."""

s = str(input("please enter a string: "))

print("Number of Characters =", len(s))

alphabets = 0
numbers = 0
specials = 0
spaces = s.count(" ")

for i in s:
    if i.isalpha():
        alphabets += 1
    elif i.isdigit():
        numbers += 1
    else:
        specials += 1

print("Number of Alphabets =", alphabets)
print("Number of Numbers =", numbers)
print("Number of Specials =", specials - spaces)
print("Number of Words =", spaces + 1)
