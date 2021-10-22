# import colorgram
# rgb_colors = []
# colors = colorgram.extract('spot.jpg', 8)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)
color_list = [(58, 106, 148), (224, 200, 109), (134, 84, 58), (223, 138, 62), (196, 145, 171), (234, 226, 204),
              (224, 234, 230)]

tim_turtle = Turtle()
tim_turtle.penup()
tim_turtle.speed("fastest")
tim_turtle.hideturtle()
x = -250
y = -250

for _ in range(10):
        tim_turtle.setpos(x, y)

        for _ in range(10):
                color = random.choice(color_list)
                tim_turtle.dot(20, color)
                tim_turtle.forward(50)
        y += 50

screen = Screen()
screen.exitonclick()
