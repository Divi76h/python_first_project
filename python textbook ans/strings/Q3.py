""" Write a function deleteChar() which takes two
    parameters one is a string and other is a character.
    The function should create a new string after
    deleting all occurrences of the character from the
    string and return the new string."""

def deleteChar(string, char):
    newString = string.replace(char, '')
    return newString


userInput = input("Enter any string: ")
delete = input("Input the character to delete from the string: ")

newStr = deleteChar(userInput, delete)

print("The new string after deleting all occurrences of", delete, "is: ", newStr)
