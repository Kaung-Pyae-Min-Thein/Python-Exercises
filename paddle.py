from turtle import Turtle


class Paddle(Turtle):
        def __init__(self, paddle_pos):
                super().__init__()
                self.shape("square")
                self.penup()
                self.shapesize(stretch_len=5, stretch_wid=1)
                self.goto(paddle_pos)
                self.setheading(90)

        def up(self):
                self.fd(50)

        def down(self):
                self.bk(50)
