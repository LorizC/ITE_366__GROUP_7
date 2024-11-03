import turtle # turtle.bgcolor() turtle.speed()
from turtle import * #bgcolor() speed()
from random import radiant

window=turtle.Screen()
window.title('TURTLE RACE GAME')

turtle.bgcolor('green')
turtle.speed(0)
turtle.penup()
turtle.setpos(-140,200)
turtle.write("TURTLE RACE",font=('Arial',30))

turtle.setpos(-400,-180)
turtle.color('brown')
turtle.begin_fill()
turtle.pendown()
for i in range(2):
    turtle.forward(800)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
turtle.endfill()

