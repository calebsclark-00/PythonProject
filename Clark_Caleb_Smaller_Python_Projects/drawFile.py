from turtle import *

#Draw line from point1 to poin2
def drawLine(y1,x2,y2):
    penup()
    goto(x1,y1)
    pendown()
    goto(x2,y2)
#Write a text at the specified location
def writeText(s,x,y):

    penup()
    goto(x,y)
    pendown()
    write(x)

#Draw a point
def drawPoint:
    penup()
    goto(x,y)
    pendown()
    dot(4,"red")

def drawCircle(x,y,radius):
    penup()
    goto(x,y - radius)
    pendown()
    circle(radius)
def drawRectangle(x,y,width,height):
    penup()
    goto(x + width / 2, y + height / 2)
    pendown()
    right(90)
    forward(height)
    right(90)
    forward(width)
    right(90)
    forward(height)
    right(90)
    forward(width)
    right(90)
    forward(width)
