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

















turtle1 = Turtle()
turtle1.speed(0)
turtle1.color('red')
turtle1.shape('turtle')
turtle1.penup()
turtle1.goto(-250, 100)
turtle1.pendown()

turtle2 = Turtle()
turtle2.speed(0)
turtle2.color('blue')
turtle2.shape('turtle')
turtle2.penup()
turtle2.goto(-250, 35)#50 65
turtle2.pendown()

turtle3 = Turtle()
turtle3.speed(0)
turtle3.color('pink')
turtle3.shape('turtle')
turtle3.penup()
turtle3.goto(-250, -35)#0 65
turtle3.pendown()

turtle4 = Turtle()
turtle4.speed(0)
turtle4.color('purple')
turtle4.shape('turtle')
turtle4.penup()
turtle4.goto(-250, -100)#50
turtle4.pendown()

