import turtle
from turtle import Turtle,Screen
import random

# timmy = Turtle()
# turtle.shape("turtle")
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)
tim_turtle = Turtle()
# turtle.shape("circle")
# turtle.shapesize(0.1,0.1,0.1)
# for _ in range(10):
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)
#     turtle.pendown()

#drawing shapes
# for sides in range(4, 11):
#     degree = round(360 / sides)
#     for _ in range(sides):
#         r = random.random()
#         g = random.random()
#         b = random.random()
#         turtle.pencolor(r, g, b)
#         turtle.forward(50)
#         turtle.right(degree)
#random walk
# turtle.pensize(10)
# for _ in range(100):
#     step = 50
#     turtle.forward(step)
#     degree = random.choice([90, 0, 180, 270])
#     #turtle.right(degree)
#     turtle.setheading(degree)
#     r = random.random()
#     g = random.random()
#     b = random.random()
#     turtle.color(r, g, b)
#     turtle.pencolor(r, g, b)
turtle.colormode(255)
def set_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
#spirograph
tim_turtle.speed("fastest")
for heading in range(0,361,10):
    tim_turtle.color(set_color())
    tim_turtle.setheading(heading)
    tim_turtle.circle(100)



# which starts at 0 and at each step moves +1 or −1
screen = Screen()
screen.exitonclick()
