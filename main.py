import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
        time.sleep(0.1)
        screen.update()
        # create car in every loop
        car_manager.create_car()
        car_manager.move_cars()
        # detect collision with every car in list
        for car in car_manager.all_cars:
                if car.distance(player) < 25:
                        game_is_on = False
                        scoreboard.game_over()
        # detect player succeed
        if player.over_finish_line():
                player.start_turtle()
                car_manager.increase_speed()
                scoreboard.level_up()
screen.exitonclick()

