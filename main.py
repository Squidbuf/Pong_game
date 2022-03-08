from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time
import winsound

screen = Screen()
screen.bgcolor("green")
screen.setup(800, 600)
screen.title("PONG")
screen.tracer(0)

turtle = Turtle()
turtle.penup()
turtle.speed(0)
turtle.color('white')
turtle.hideturtle()
turtle.goto(-390,295)
turtle.pendown()
for i in range(2):
	turtle.forward(770)
	turtle.right(90)
	turtle.forward(580)
	turtle.right(90)
turtle.goto(0,295)
turtle.right(90)
turtle.goto(0,-285)
turtle.penup()
turtle.goto(-50,0)
turtle.pendown()
turtle.circle(50)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_continue = True

while game_continue:
    time.sleep(0.1)
    ball.move()
    screen.update()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.ycor() > -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.home()
        ball.bounce_x()
        score.l_point()

    if ball.xcor() < -380:
        ball.home()
        ball.bounce_x()
        score.r_point()

screen.exitonclick()