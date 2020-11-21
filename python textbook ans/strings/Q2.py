""" Write a user defined function to convert a string
    with more than one word into title case string where
    string is passed as parameter. (Title case means
    that the first letter of each word is capitalised)"""

def convertToTitle(string):
    titleString = string.title();
    print(titleString)

userInput = input("Write a sentence: ")
totalSpace = 0
for b in userInput:
    if b.isspace():
        totalSpace += 1
if (userInput.istitle()):
    print("The String is already in title case")
elif (totalSpace > 0):
    convertToTitle(userInput)
else:
    print("The String is of one word only")