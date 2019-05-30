def areaOfCircle(r):
    PI = 3.141592653589793238462643383279502884197169399375105820974944592307816406286
    PI = float(PI)

    return PI * (r * r)


def cirumferenceOfCircle(r):
    PI = 3.141592653589793238462643383279502884197169399375105820974944592307816406286
    PI = float(PI)

    return 2 * PI * r


def areaOfSquare(side):

    return side * side


def surfaceAreaOfCube(side):

    return 6 * (side * side)


def volumeOfCube(side):

    return side * side * side


def areaOfRectangle(l, b):
    l = float(l)
    b = float(b)
    area = l * b
    area = float(area)

    return area


def surfaceAreaOfRectangle(l, b, h):
    l = float(l)
    b = float(b)
    h = float(h)
    surfacearea = 2 * ((l * b) + (b * h) + (l * h))
    surfacearea = float(surfacearea)

    return surfacearea


def volumeOfCuboid(l, b, h):
    l = float(l)
    b = float(b)
    h = float(h)
    volume = l * b * h
    volume = float(volume)

    return volume


print("\n1) Area of circle\n2) Circumference of circle\n3) Area of square")
print("4) Surface area of cube\n5) Volume of cube\n6) Area of rectangle\n7) Surface area of rectangle\n8) Volume of cuboid")
option = input("\nWhat do you want to do (use serial number) : ")
print("\r")

option = int(option)

if option == 1:
    value = input(
        "Give the radius of the circle with unit (with a space between the value and the unit) : ").split(" ")
    r = float(value[0])
    unit = value[1]
    print("\nThe area of circle with radius {0} {1} is {2} square {3}".format(
        r, unit, areaOfCircle(r), unit))

elif option == 2:
    value = input(
        "Give the radius of the circle with unit (with a space between the value and the unit) : ").split(" ")
    r = float(value[0])
    unit = value[1]
    print("\nThe circumference of circle with radius {0} {1} is {2} {3}".format(
        r, unit, cirumferenceOfCircle(r), unit))

elif option == 3:
    value = input(
        "give the side of the squrae with unit (with a space between the value and the unit) : ").split(" ")
    side = float(value[0])
    unit = value[1]
    print("\nThe area of cube with side {0} {1} is {2} square {3}".format(
        side, unit, areaOfSquare(side), unit))

elif option == 4:
    value = input(
        "give the side of the squrae with unit (with a space between the value and the unit) : ").split(" ")
    side = float(value[0])
    unit = value[1]
    print("\nThe surface area of cube with side {0} {1} is {2} square {3}".format(
        side, unit, surfaceAreaOfCube(side), unit))

elif option == 5:
    value = input(
        "give the side of the cube with unit (with a space between the value and the unit) : ").split(" ")
    side = float(value[0])
    unit = value[1]
    print("\nThe volume of cube with side {0} {1} is {2} cube {3}".format(
        side, unit, volumeOfCube(side), unit))

elif option == 6:
    value = input(
        "Give the length, breadth with unit for both (with a space between them) : ").split(" ")
    l = float(value[0])
    b = float(value[2])
    unit = value[3]
    print("\nThe area of rectangle with length {0} {1} and breadth {2} {3} is {4} square {5}".format(
        l, unit, b, unit, areaOfRectangle(l, b), unit))

elif option == 7:
    value = input(
        "Give the length, breadth and height with unit for all (with a space between them) : ").split(" ")
    l = float(value[0])
    b = float(value[2])
    h = float(value[4])
    unit = value[5]
    print("\nThe surface area of rectangle with length {0} {1} breadth {2} {3} and height {4} {5} is {6} square {7}".format(
        l, unit, b, unit, h, unit, surfaceAreaOfRectangle(l, b, h), unit))

elif option == 8:
    value = input(
        "Give the length, breadth and height with unit for all (with a space between them) : ").split(" ")
    l = float(value[0])
    b = float(value[2])
    h = float(value[4])
    unit = value[5]
    print("\nThe volume of cuboid with length {0} {1} breadth {2} {3} and height {4} {5} is {6} cube {7}".format(
        l, unit, b, unit, h, unit, volumeOfCuboid(l, b, h), unit))

elif (option > 8 or option < 1):
    print("Incorrect Input")
