import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    #Detect if player finishes level
    if player.ycor() > 280:
        player.reset()
        scoreboard.add_point()
        car_manager.level_up()

    #Detect if player collides with car
    for car in car_manager.all_cars:
        if player.distance(car) < 30:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()