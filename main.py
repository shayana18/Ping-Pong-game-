from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

right_paddle = Paddle(350)
left_paddle = Paddle(-350)
scoreboard = Score()
ball = Ball()

screen.listen()
screen.onkeypress(fun=right_paddle.up, key="Up")
screen.onkeypress(fun=right_paddle.down, key="Down")
screen.onkeypress(fun=left_paddle.up, key="w")
screen.onkeypress(fun=left_paddle.down, key="s")



game_on = True


while game_on:
    scoreboard.score()
    time.sleep(ball.move_speed)
    screen.update()

    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 360:
        scoreboard.left_point += 1
        scoreboard.score()
        ball.restart()
        ball.bounce_x()


    if ball.xcor() < -360:
        scoreboard.right_point += 1
        scoreboard.score()
        ball.restart()
        ball.bounce_x()








screen.exitonclick()
