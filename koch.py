from turtle import *


# function to create koch snowflake or koch curve
def kochSnowflake(lengthSide, levels):
    if levels == 0:
        forward(lengthSide)
        return
    lengthSide /= 3.0
    snowflake(lengthSide, levels-1)
    left(60)
    snowflake(lengthSide, levels-1)
    right(120)
    snowflake(lengthSide, levels-1)
    left(60)
    snowflake(lengthSide, levels-1)


speed(0)
length = 300.0


penup()

backward(length/2.0)


pendown()
for i in range(3):
    kochSnowflake(length, 4)
    right(120)


# main function
if __name__ == "__main__":
    # defining the speed of the turtle
