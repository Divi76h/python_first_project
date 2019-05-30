import re

# Make a regular expression
# for validating an Email
regex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

# Define a function for
# for validating an Email


def check(email):

    # pass the regualar expression
    # and the string in search() method
    if(re.search(regex, email)):
        print("Valid Email")

    else:
        print("Invalid Email")


# Driver Code
if __name__ == '__main__':

    # Enter the email
    email = input("enter your email : ")
    check(email)
