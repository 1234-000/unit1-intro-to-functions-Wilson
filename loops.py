import turtle
from turtle import *
t = Turtle()
t.speed(100)


sidelength = 50
rotate = 144
def star(x,y):
    for i in range(5):
        t.forward(x)
        t.right(144)
star(5,144)

def addSquares(iRange):
    length = 25
    for i in range(iRange):
        star(length, 144)
        length += 5
        t.right(5)
addSquares(60)


turtle.done()

def doubleSquares(iRange):
    length = 25
    for i in range(iRange):
        square(length, 90)
        length = length * 2
doubleSquares(5)



sidelength = 5
rotate = 90
def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)
square(5,90)

def addSquares(iRange):
    length = 25
    for i in range(iRange):
        square(length, 90)
        length += 5
        t.right(5)
addSquares(60)




sidelength = 100
rotate = 90
def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)
square(100,90)

def addSquares(iRange):
    length = 100
    for i in range(iRange):
        square(length, 90)
        t.left(5)
addSquares(60)


