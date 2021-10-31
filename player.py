from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.left(90)
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.color("black")

    def turtle_up(self):
        self.forward(MOVE_DISTANCE)

    def backtostart(self):
        self.goto(STARTING_POSITION)
