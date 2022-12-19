import turtle
from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, xcord):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.xcordinate = xcord
        self.goto(self.xcordinate, y= 0)


    def up(self):
        current_y = self.ycor()
        new_y = current_y + 20
        if current_y < 240:
            self.goto(self.xcordinate, new_y)


    def down(self):
        current_y = self.ycor()
        new_y = current_y - 20
        if current_y > -240:
            self.goto(self.xcordinate, new_y)



