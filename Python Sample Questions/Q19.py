""" Write a program that reads a string
    and then prints a string that capitalizes
    every other letter in the string"""

str_input = input('Enter your string: ')
str_input = list(str_input)

for i in range(len(str_input)):
    if i % 2 != 0:
        str_input[i] = str_input[i].upper()
print(''.join(str_input))
