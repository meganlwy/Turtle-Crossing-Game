from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.carlist = []
        self.carspeed = STARTING_MOVE_DISTANCE

    def createcar(self):
        chance = random.randint(1, 5)
        if chance == 1:
            newcar = Turtle("square")
            newcar.penup()
            newcar.color(random.choice(COLORS))
            newcar.shapesize(stretch_wid=1, stretch_len=2)
            newcar.goto(300, random.randint(-250, 250))
            self.carlist.append(newcar)

    def run(self):
        for car in self.carlist:
            car.backward(self.carspeed)

    def speedup(self):
        self.carspeed += MOVE_INCREMENT
        for car in self.carlist:
            car.backward(self.carspeed)
