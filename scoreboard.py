from turtle import Turtle


class Scoreboard(Turtle):
        def __init__(self):
                super().__init__()
                self.penup()
                self.hideturtle()
                self.left_paddle = 0
                self.right_paddle = 0
                self.update_board()

        def update_board(self):
                self.clear()
                self.goto(x=0, y=250)
                self.write(f"{self.left_paddle}   :   {self.right_paddle}", align="center", font=("Arial", 30, 'bold'))

        def l_point(self):
                self.left_paddle += 1
                self.update_board()
        def r_point(self):
                self.right_paddle += 1
                self.update_board()