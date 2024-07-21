from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, screen_height) -> None:
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, int(screen_height / 2) - 50)

    def update_score(self, score):
        self.clear()
        self.write(f"Score: {score}", align="center", font=("Courier", 14, "normal"))

    def final_score(self, score):
        self.clear()
        self.goto(0, 0)
        self.write(
            f"      Game Over!\nYour final score is {score}",
            align="center",
            font=("Courier", 24, "normal"),
        )
