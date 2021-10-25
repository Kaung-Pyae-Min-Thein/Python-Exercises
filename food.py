import random
from turtle import Turtle


class Food(Turtle):
        def __init__(self):
                super().__init__()
                self.shape("circle")
                self.penup()
                self.shapesize(stretch_wid=0.5, stretch_len=0.5)
                self.color("green")
                self.refresh_location()


        def refresh_location(self):
                random_x = random.randint(-250, 250)
                random_y = random.randint(-250, 250)
                self.goto(x=random_x, y=random_y)

