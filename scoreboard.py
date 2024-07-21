from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, screen_height) -> None:
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, int(screen_height / 2) - 50)
        self.write_score()

    def write_score(self):
        self.write(
            f"Score: {self.score}", align="center", font=("Courier", 14, "normal")
        )

    def update_score(self):
        self.clear()
        self.score += 1
        self.write_score()

    def final_score(self):
        self.clear()
        self.goto(0, 0)
        self.write(
            f"      Game Over.\nYour final score is {self.score}",
            align="center",
            font=("Courier", 24, "normal"),
        )
