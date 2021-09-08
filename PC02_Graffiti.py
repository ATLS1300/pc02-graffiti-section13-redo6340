#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Reeve Donner
Sep 2, 2021
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Demon Bezos======
#====Demon Eyes
t=turtle.Turtle()
t.penup()
t.color("red")
t.goto(-15,113)
t.dot()
t.goto(43,120)
t.dot()
#=====Demon Tounge
t.color("pink")
t.pensize(5)
t.goto(20,50)
t.fd(5)
t.pendown()
t.rt(90)
t.begin_fill()
t.goto(35,10)
t.rt(90)
t.goto(21,10)
t.rt(90)
t.goto(18,50)
t.rt(90)
t.fd(5)
t.end_fill()
t.penup()
t.backward(3)
t.color("black")
t.rt(90)
t.pendown()
t.pensize(3)
t.goto(30,10)
#======Stink Face
t.penup()
t.goto(1,145)
t.pendown()
t.goto(11,128)
t.lt(180)
t.goto(17,150)
#=====Staff
t.penup()
t.pensize(6)
t.color("bisque3")
t.goto(20,-20)
t.pendown()
t.begin_fill()
t.rt(180)
t.goto(19,-65)
t.lt(90)
t.fd(20)
t.lt(90)
t.goto(35,-20)
t.lt(90)
t.goto(20,-20)
t.end_fill()
t.penup()
t.goto(20,-153)
t.lt(90)
t.pendown()
t.begin_fill()
t.goto(20,-247)
t.lt(90)
t.fd(20)
t.lt(90)
t.goto(35,-153)
t.lt(90)
t.goto(20,-153)
t.end_fill()
t.penup()
t.goto(25,0)
t.pen(pencolor="green", fillcolor="DarkOliveGreen1", pensize=5, speed=9)
t.pendown()
t.begin_fill()
t.circle(20)
t.end_fill()
t.penup()


#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
#turtle.done()

