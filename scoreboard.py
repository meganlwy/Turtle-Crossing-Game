from turtle import Turtle

FONT = ("Arial", 30, "bold")
POSITION = (-220, 250)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.penup()
        self.color("black")
        self.goto(POSITION)
        self.updatescore()

    def updatescore(self):
        self.clear()
        self.write(f"LEVEL:{self.score}", False, "center", FONT)

    def addscore(self):
        self.score += 1

    def endgame(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER.", False, "center", FONT)
