from turtle import Turtle
ALIGHMENT = "center"
FONT = ("DejaVu Sans Mono", 22, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 265)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGHMENT ,font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGHMENT ,font=FONT)
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()