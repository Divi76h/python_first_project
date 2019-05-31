import turtle
from turtle import Turtle
import math
import random
from random import randint
import time
import random as r
import sys
import pygame
from math import pi, sin, cos, exp
from pygame.locals import *


def main():
    print("This is a cool program for turtle graphics")
    print("\nMENU")
    print("1) Spirograph Star\n2) Square inside a square (outside in)")
    print("3) Square inside a square(inside out)")
    print("4) Star\n5) Hexagon\n6) Sprial Helix\n7) Rainbow Benzene")
    print("8) Sunflower\n9) Honey Comb\n10) Gorgia Spiral")
    print("11) Super Sprial\n12) Hologram\n13) Spider web\n14) Koch snowflake")
    print("15) Draw your own polygon")

    option = input("\nEnter serial number : ")
    option = int(option)

    if option == 1:
        spirographStar()

    elif option == 2:
        outsideIn()

    elif option == 3:
        insideOut()

    elif option == 4:
        star()

    elif option == 5:
        hexagon()

    elif option == 6:
        sprialHelix()

    elif option == 7:
        rainbowBenzene()

    elif option == 8:
        sunflower()

    elif option == 9:
        honeycomb()

    elif option == 10:
        gorgiaSprial()

    elif option == 11:
        superSprial()

    elif option == 12:
        hologram()

    elif option == 13:
        spiderWeb()

    elif option == 14:
        kochSnowflake()

    elif option == 15:
        makeYourOwn()

    elif (option > 13 or option < 1):
        print("wrong input")

    else:
        print("wrong input")


def spirographStar():
    y = input("please enter the colour : ")
    y = str(y)
    z = input("please enter the backgorund colour : ")
    z = str(z)
    x = turtle.Screen()
    skk = turtle.Turtle()
    skk.color(y)
    x.bgcolor(z)

    for i in range(0, 18):

        skk.right(200)
        skk.left(300)
        skk.backward(200)

    turtle.exitonclick()


def outsideIn():
    y = input("please enter the colour : ")
    y = str(y)
    z = input("please enter the backgorund colour : ")
    z = str(z)
    x = turtle.Screen()
    x.bgcolor(z)
    x.title("Turtle")
    skk = turtle.Turtle()
    skk.color(y)

    def sqrfunc(size):
        for i in range(4):
            skk.fd(size)
            skk.left(90)
            size = size-5

    sqrfunc(146)
    sqrfunc(126)
    sqrfunc(106)
    sqrfunc(86)
    sqrfunc(66)
    sqrfunc(46)
    sqrfunc(26)

    turtle.exitonclick()


def insideOut():
    y = input("please enter the colour : ")
    y = str(y)
    z = input("please enter the backgorund colour : ")
    z = str(z)
    x = turtle.Screen()
    x.bgcolor(z)
    x.title("Turtle")
    skk = turtle.Turtle()
    skk.color(y)

    def sqrfunc(size):
        for i in range(4):
            skk.fd(size)
            skk.left(90)
            size = size+5

    sqrfunc(6)
    sqrfunc(26)
    sqrfunc(46)
    sqrfunc(66)
    sqrfunc(86)
    sqrfunc(106)
    sqrfunc(126)
    sqrfunc(146)

    turtle.exitonclick()


def star():
    y = input("please enter the colour : ")
    y = str(y)
    z = input("please enter the backgorund colour : ")
    z = str(z)
    x = turtle.Screen()
    x.bgcolor(z)
    x.title("Turtle")
    skk = turtle.Turtle()
    skk.color(y)

    for i in range(25):
        skk.forward(200)
        skk.right(144)

    turtle.exitonclick()


def hexagon():
    y = input("please enter the colour : ")
    y = str(y)
    z = input("please enter the backgorund colour : ")
    z = str(z)
    x = turtle.Screen()
    x.bgcolor(z)
    x.title("Turtle")
    skk = turtle.Turtle()
    skk.color(y)

    for i in range(1, 7):
        skk.forward(100)
        skk.right(60)

    turtle.exitonclick()


def sprialHelix():
    y = input("please enter the colour : ")
    y = str(y)
    z = input("please enter the backgorund colour : ")
    z = str(z)
    x = turtle.Screen()
    x.bgcolor(z)
    x.title("Turtle")
    skk = turtle.Turtle()
    skk.color(y)
    skk.speed(0)

    for i in range(50):
        skk.circle(5*i)
        skk.circle(-5*i)
        skk.left(i)

    turtle.exitonclick()


def rainbowBenzene():
    colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
    t = turtle.Pen()
    turtle.bgcolor('black')
    for x in range(270):
        t.pencolor(colors[x % 6])
        t.width(x/100 + 1)
        t.forward(x)
        t.left(59)

    turtle.exitonclick()


def makeYourOwn():
    numberofside = input("Please enter the number of sides : ")
    numberofside = int(numberofside)
    angle = 360/numberofside
    angle = float(angle)
    y = input("please enter the colour : ")
    y = str(y)
    z = input("please enter the backgorund colour : ")
    z = str(z)
    x = turtle.Screen()
    x.bgcolor(z)
    x.title("Turtle")
    skk = turtle.Turtle()
    skk.color(y)
    skk.speed(0)

    for i in range(0, numberofside):
        skk.forward(50)
        skk.right(angle)

    turtle.exitonclick()


def sunflower():
    def drawPhyllPattern(turtle, t, petalstart, angle=137.508, size=2, cspread=4):
        turtle.color('black')
        turtle.fillcolor("orange")
        phi = angle * (math.pi / 180.0)
        xcenter = 0.0
        ycenter = 0.0

        for n in range(0, t):
            r = cspread * math.sqrt(n)
            theta = n * phi

            x = r * math.cos(theta) + xcenter
            y = r * math.sin(theta) + ycenter

            turtle.up()
            turtle.setpos(x, y)
            turtle.down()
            turtle.setheading(n * angle)
            if n > petalstart-1:
                turtle.color("yellow")
                drawPetal(turtle, x, y)
            else:
                turtle.stamp()

    def drawPetal(turtle, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.color('black')
        turtle.fillcolor('yellow')
        turtle.begin_fill()
        turtle.right(20)
        turtle.forward(70)
        turtle.left(40)
        turtle.forward(70)
        turtle.left(140)
        turtle.forward(70)
        turtle.left(40)
        turtle.forward(70)
        turtle.penup()
        turtle.end_fill()

    gfg = turtle.Turtle()
    gfg.shape("turtle")
    gfg.speed(10000000)
    drawPhyllPattern(gfg, 200, 160, 137.508)
    gfg.penup()
    gfg.forward(1000)

    turtle.exitonclick()


def honeycomb():
    size = 20
    circles = 20
    turtle.speed(0)

    turtle.colormode(255)

    def move(length, angle):
        turtle.right(angle)
        turtle.forward(length)

    def hex():
        turtle.pendown()
        turtle.color(randint(0, 255), randint(0, 255), randint(0, 255))
        turtle.begin_fill()
        for i in range(6):
            move(size, -60)
        turtle.end_fill()
        turtle.penup()

    turtle.penup()

    for circle in range(circles):
        if circle == 0:
            hex()
            move(size, -60)
            move(size, -60)
            move(size, -60)
            move(0, 180)
        for i in range(6):
            move(0, 60)
            for j in range(circle+1):
                hex()
                move(size, -60)
                move(size, 60)
            move(-size, 0)
        move(-size, 60)
        move(size, -120)
        move(0, 60)

    turtle.exitonclick()


def gorgiaSprial():
    wn = turtle.Screen()
    wn.bgcolor('black')
    Albert = turtle.Turtle()
    Albert.speed(0)
    Albert.color('white')
    rotate = int(360)

    def drawCircles(t, size):
        for i in range(10):
            t.circle(size)
            size = size-4

    def drawSpecial(t, size, repeat):
        for i in range(repeat):
            drawCircles(t, size)
            t.right(360/repeat)

    drawSpecial(Albert, 100, 10)
    Steve = turtle.Turtle()
    Steve.speed(0)
    Steve.color('yellow')
    rotate = int(90)

    def drawCircles(t, size):
        for i in range(4):
            t.circle(size)
            size = size-10

    def drawSpecial(t, size, repeat):
        for i in range(repeat):
            drawCircles(t, size)
            t.right(360/repeat)

    drawSpecial(Steve, 100, 10)
    Barry = turtle.Turtle()
    Barry.speed(0)
    Barry.color('blue')
    rotate = int(80)

    def drawCircles(t, size):
        for i in range(4):
            t.circle(size)
            size = size-5

    def drawSpecial(t, size, repeat):
        for i in range(repeat):
            drawCircles(t, size)
            t.right(360/repeat)

    drawSpecial(Barry, 100, 10)
    Terry = turtle.Turtle()
    Terry.speed(0)
    Terry.color('orange')
    rotate = int(90)

    def drawCircles(t, size):
        for i in range(4):
            t.circle(size)
            size = size-19

    def drawSpecial(t, size, repeat):
        for i in range(repeat):
            drawCircles(t, size)
            t.right(360/repeat)

    drawSpecial(Terry, 100, 10)
    Will = turtle.Turtle()
    Will.speed(0)
    Will.color('pink')
    rotate = int(90)

    def drawCircles(t, size):
        for i in range(4):
            t.circle(size)
            size = size-20

    def drawSpecial(t, size, repeat):
        for i in range(repeat):
            drawCircles(t, size)
            t.right(360/repeat)

    drawSpecial(Will, 100, 10)

    turtle.exitonclick()

def superSprial():
    turtle.setup(width=600, height=500)
    turtle.reset()
    turtle.hideturtle()
    turtle.speed(0)

    turtle.bgcolor('black')

    c = 0
    x = 0

    colors = [
    #reddish colors
    (1.00, 0.00, 0.00),(1.00, 0.03, 0.00),(1.00, 0.05, 0.00),(1.00, 0.07, 0.00),(1.00, 0.10, 0.00),(1.00, 0.12, 0.00),(1.00, 0.15, 0.00),(1.00, 0.17, 0.00),(1.00, 0.20, 0.00),(1.00, 0.23, 0.00),(1.00, 0.25, 0.00),(1.00, 0.28, 0.00),(1.00, 0.30, 0.00),(1.00, 0.33, 0.00),(1.00, 0.35, 0.00),(1.00, 0.38, 0.00),(1.00, 0.40, 0.00),(1.00, 0.42, 0.00),(1.00, 0.45, 0.00),(1.00, 0.47, 0.00),
    #orangey colors
    (1.00, 0.50, 0.00),(1.00, 0.53, 0.00),(1.00, 0.55, 0.00),(1.00, 0.57, 0.00),(1.00, 0.60, 0.00),(1.00, 0.62, 0.00),(1.00, 0.65, 0.00),(1.00, 0.68, 0.00),(1.00, 0.70, 0.00),(1.00, 0.72, 0.00),(1.00, 0.75, 0.00),(1.00, 0.78, 0.00),(1.00, 0.80, 0.00),(1.00, 0.82, 0.00),(1.00, 0.85, 0.00),(1.00, 0.88, 0.00),(1.00, 0.90, 0.00),(1.00, 0.93, 0.00),(1.00, 0.95, 0.00),(1.00, 0.97, 0.00),
    #yellowy colors
    (1.00, 1.00, 0.00),(0.95, 1.00, 0.00),(0.90, 1.00, 0.00),(0.85, 1.00, 0.00),(0.80, 1.00, 0.00),(0.75, 1.00, 0.00),(0.70, 1.00, 0.00),(0.65, 1.00, 0.00),(0.60, 1.00, 0.00),(0.55, 1.00, 0.00),(0.50, 1.00, 0.00),(0.45, 1.00, 0.00),(0.40, 1.00, 0.00),(0.35, 1.00, 0.00),(0.30, 1.00, 0.00),(0.25, 1.00, 0.00),(0.20, 1.00, 0.00),(0.15, 1.00, 0.00),(0.10, 1.00, 0.00),(0.05, 1.00, 0.00),
    #greenish colors
    (0.00, 1.00, 0.00),(0.00, 0.95, 0.05),(0.00, 0.90, 0.10),(0.00, 0.85, 0.15),(0.00, 0.80, 0.20),(0.00, 0.75, 0.25),(0.00, 0.70, 0.30),(0.00, 0.65, 0.35),(0.00, 0.60, 0.40),(0.00, 0.55, 0.45),(0.00, 0.50, 0.50),(0.00, 0.45, 0.55),(0.00, 0.40, 0.60),(0.00, 0.35, 0.65),(0.00, 0.30, 0.70),(0.00, 0.25, 0.75),(0.00, 0.20, 0.80),(0.00, 0.15, 0.85),(0.00, 0.10, 0.90),(0.00, 0.05, 0.95),
    #blueish colors
    (0.00, 0.00, 1.00),(0.05, 0.00, 1.00),(0.10, 0.00, 1.00),(0.15, 0.00, 1.00),(0.20, 0.00, 1.00),(0.25, 0.00, 1.00),(0.30, 0.00, 1.00),(0.35, 0.00, 1.00),(0.40, 0.00, 1.00),(0.45, 0.00, 1.00),(0.50, 0.00, 1.00),(0.55, 0.00, 1.00),(0.60, 0.00, 1.00),(0.65, 0.00, 1.00),(0.70, 0.00, 1.00),(0.75, 0.00, 1.00),(0.80, 0.00, 1.00),(0.85, 0.00, 1.00),(0.90, 0.00, 1.00),(0.95, 0.00, 1.00)
    ]

    while x < 1000:
        idx = int(c)
        color = colors[idx]
        turtle.color(color)
        turtle.forward(x)
        turtle.right(98)
        x = x + 1
        c = c + 0.1

    turtle.exitonclick()

def hologram():
    print("Quit: q key")

    width, height = 1280, 720       
    width, height = 1920, 1080      
    width, height = 1280, 1024      
    width, height = 1680, 1050     
    width, height = 1200, 800
          
    dd = 0.99995                  
    dt = 0.02                     
    speed = 200                   
    hui = 57*2                   
    hue, sat, val, aaa = 0, 100, 100, 0
    sd = 0.005                   
    mx = 4                        
    print("Hit SPACE to save")


    def check_event():
        global save
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_q:
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_SPACE:
                save = True
                print("Saving when finished...")


    def scale(length):
        while True:
            a1, a2 = r.randint(-mx, mx), r.randint(-mx, mx)
            max = abs(a1)+abs(a2)
            if max > 0:
                break
        return a1, a2, length/(2*max)


    steps = 0
    pygame.init()
    pygame.event.set_allowed([QUIT, KEYDOWN])
    screen = pygame.display.set_mode((width, height), DOUBLEBUF)
    screen.set_alpha(None)
    fg = (255, 255, 255)
    while True:
        ax1, ax2, xscale = scale(width)
        ay1, ay2, yscale = scale(height)
        fx1, fx2 = r.randint(1, mx) + r.gauss(0,
                                            sd), r.randint(1, mx) + r.gauss(0, sd)
        fy1, fy2 = r.randint(1, mx) + r.gauss(0,
                                            sd), r.randint(1, mx) + r.gauss(0, sd)
        px1, px2 = r.uniform(0, 2*pi), r.uniform(0, 2*pi)
        py1, py2 = r.uniform(0, 2*pi), r.uniform(0, 2*pi)
        print(ax1, ax2, ay1, ay2)
        print(fx1, fx2, fy1, fy2)
        print(px1, px2, py1, py2)

        dec = 1.0
        t = 0.0                       
        first = True
        while dec > 0.015:
                                   
            x = xscale * dec * (ax1*sin(t * fx1 + px1) + ax2 *
                                sin(t * fx2 + px2)) + width/2
            y = yscale * dec * (ay1*sin(t * fy1 + py1) + ay2 *
                                sin(t * fy2 + py2)) + height/2
            dec *= dd                 
            if not first:           
                pygame.draw.aaline(screen, fg, (x, y), (prev_x, prev_y), 1)
            else:
                first = False

            prev_x = x              
            prev_y = y
            if steps % speed == 0:
                pygame.display.update()
            steps += 1
            t += dt                   
            check_event()

        screen.fill((0, 0, 0))

def spiderWeb():
    y = input("please enter the colour : ")
    y = str(y)
    z = input("please enter the backgorund colour : ")
    z = str(z)
    x = turtle.Turtle()
    x.speed(0)
    x.color(y)
    turtle.bgcolor(z)
    b = 180
    for c in range(5):
        a = 9*c
        for i in range(100):
            x.circle(i, a)
            x.right(b)
            x.circle(i, a)
            x.right(b)
            x.circle(i, a)
            x.right(b)
            x.circle(i, a)

    turtle.exitonclick()

def kochSnowflake():
    y = input("please enter the colour : ")
    y = str(y)
    z = input("please enter the backgorund colour : ")
    z = str(z)
    turtle.color(y)
    turtle.bgcolor(z)
    def snowflake(lengthSide, levels): 
        if levels == 0: 
            turtle.forward(lengthSide) 
            return
        lengthSide /= 3.0
        snowflake(lengthSide, levels-1) 
        turtle.left(60) 
        snowflake(lengthSide, levels-1) 
        turtle.right(120) 
        snowflake(lengthSide, levels-1) 
        turtle.left(60) 
        snowflake(lengthSide, levels-1) 

    turtle.speed(0)                    
    length = 300.0   
           
    turtle.penup()                      
  
    turtle.backward(length/2.0) 
      
    turtle.pendown()            
    for i in range(3):     
        snowflake(length, 4) 
        turtle.right(120)

    turtle.exitonclick()


if __name__ == "__main__":
    main()

else:
    print("This file is being imported")
    main()
