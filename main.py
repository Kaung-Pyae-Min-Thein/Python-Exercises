import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong Game")
# turn_off the animation
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key="Up", fun=r_paddle.up)
screen.onkeypress(key="Down", fun=r_paddle.down)
screen.onkeypress(key="w", fun=l_paddle.up)
screen.onkeypress(key="s", fun=l_paddle.down)


game_is_on = True
while game_is_on:
        time.sleep(ball.move_speed)
        # refresh the screen & show everything in the bg
        screen.update()
        ball.move()
        # check collision if collise the Y-axis continously substract by 10 instead of plus
        if ball.ycor() > 270 or ball.ycor() < -270:
                ball.bounce_y()
        # detect collision with paddle
        if ball.xcor() < -320 and ball.distance(l_paddle) < 50 or ball.xcor() > 320 and ball.distance(r_paddle) < 50:
                ball.bounce_x()

        # detect right paddle miss
        if ball.xcor() > 400:
                ball.refresh_ball()
                scoreboard.l_point()
        # detect left paddle miss
        if ball.xcor() < -400:
                ball.refresh_ball()
                scoreboard.r_point()


screen.exitonclick()
