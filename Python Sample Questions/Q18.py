""" Write a program that reads a string
    and display the longest substrstring of
    the given string having just the consonants."""

string = input("Enter a string: ")
length = len(string)

maxsubstr = ''
substr = ''

for a in range(length):
    if string[a] in 'aeiou' or string[a] in 'AEIOU':
        maxsubstr = substr
        substr = ''
    else:
        substr += string[a]

print("Maximum consonant substrstring is: {}".format(maxsubstr))
