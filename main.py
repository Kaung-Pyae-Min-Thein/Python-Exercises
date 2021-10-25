import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
# screen.bgcolor("black")
# turn-off the trace, so the screen is not update since the program start
screen.tracer(0)
screen.title("My Snake Game")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
game_is_on = True
while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        # detect collision with food
        if snake.head.distance(food) < 18:
                food.refresh_location()
                scoreboard.update_score()
                snake.extend_segment()
        # detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
                game_is_on = False
                scoreboard.game_over()
        # detect collision with tail
        for segment in snake.segments[1:]:
                if snake.head.distance(segment) < 10:
                        game_is_on = False
                        scoreboard.game_over()
screen.exitonclick()
