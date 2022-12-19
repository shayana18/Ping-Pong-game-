from turtle import Turtle

ALIGNMENT = "center"
FONT_TYPE = ("arial", 48, "italic")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.right_point = 0
        self.left_point = 0

    def score(self):
        self.clear()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 220)
        self.write(f"{self.left_point}        {self.right_point}", True, ALIGNMENT, FONT_TYPE)




