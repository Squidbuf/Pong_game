from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 20, "bold")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.pu()
        self.ht()
        self.color("white")
        self.update()

    def update(self):
        self.goto(-200, 250)
        self.write(f"A : {self.l_score}", align=ALIGN, font=FONT)
        self.goto( 200, 250)
        self.write(f"B : {self.r_score}", align=ALIGN, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update()


    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update()
