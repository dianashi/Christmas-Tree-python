import turtle
from random import randint
import time
n = 100.0
turtle.speed("fastest")

turtle.screensize()
turtle.bgcolor("#750101")

turtle.width(3)
turtle.left(90)
turtle.forward(3*n)
turtle.color("orange", "yellow")
turtle.begin_fill()
turtle.left(126)
for i in range(5):
    turtle.forward(n/5)
    turtle.right(144)
    turtle.forward(n/5)
    turtle.left(72)
turtle.end_fill()
turtle.right(126)
turtle.color("dark green")
turtle.backward(n*4.9)
def tree(d,s):
    if d <= 0: return
    turtle.forward(s)
    tree(d-1, s*.8)
    turtle.right(120)
    tree(d-3, s*.5)
    turtle.right(120)
    tree(d-3, s*.5)
    turtle.right(120)
    turtle.backward(s)
tree(15,n)
turtle.backward(n/2)

turtle.color("white")
turtle.width(1)

for i in range(80):
    turtle.up()
    turtle.goto(randint(-400, 400), randint(-300,300))
    turtle.down()
    turtle.begin_fill()
    for i in range(5):
        turtle.right(144)
        turtle.forward(15)
    turtle.end_fill()
    turtle.TurtleScreen._RUNNING = True

turtle.up()
    
