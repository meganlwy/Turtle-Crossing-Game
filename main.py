import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Corssing Game")
turtle = Player()
screen.listen()
screen.onkey(turtle.turtle_up, "Up")  # turtle can only move forward

car_mgr = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_mgr.createcar()
    car_mgr.run()
    # if turtle collide with the cars
    for car in car_mgr.carlist:
        if turtle.distance(car) < 20:
            game_is_on = False
            scoreboard.endgame()
    if turtle.ycor() > 280:
        scoreboard.addscore()
        scoreboard.updatescore()
        turtle.backtostart()
        car_mgr.speedup()

screen.exitonclick()
