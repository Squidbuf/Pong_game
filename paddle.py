from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.pu()
        self.goto(position)
        self.speed(9)

    def move_up(self):
        y_position = self.ycor() + 20
        self.goto(self.xcor(), y_position)

    def move_down(self):
        y_position = self.ycor() - 20
        self.goto(self.xcor(), y_position)

