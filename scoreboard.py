FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
        def __init__(self):
                super().__init__()
                self.level = 1
                self.penup()
                self.hideturtle()
                self.goto(x=-210, y=250)
                self.start_level()

        def start_level(self):
                self.clear()
                self.write(f"Level: {self.level}", align="center", font=FONT)

        def level_up(self):
                self.level += 1
                self.start_level()

        def game_over(self):
                self.goto(0, 0)
                self.write("Game Over!", align="center", font=FONT)
