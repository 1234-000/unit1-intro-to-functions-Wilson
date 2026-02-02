import turtle
from turtle import *
t = Turtle()

def equal(x):
    t.forward(90)
    t.left(120)
    t.forward(90)
    t.left(120)
    t.forward(90)
equal(200) 

def rectangle(x):
    t.forward(125)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(125)
    t.left(90)
    t.forward(100)
    t.left(90)
rectangle(200)

turtle.done()

def right():
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(135)
    t.forward(142)
right()