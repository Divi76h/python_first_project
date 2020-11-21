""" Write a function that takes a sentence as an input
    parameter where each word in the sentence is
    separated by a space. The function should replace
    each blank with a hyphen and then return the
    modified sentence."""


def replaceChar(string):
    return string.replace(' ', '-')


userInput = input("Enter a sentence: ")

result = replaceChar(userInput)

print("The new sentence is:", result)
