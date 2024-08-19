from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        try:
            with open("high_score.txt", "r") as high_score_file:
                self.high_score = int(high_score_file.read())
        except FileNotFoundError:
            self.high_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            align="center",
            font=("Courier", 14, "normal"),
        )

    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "w") as high_score_file:
                high_score_file.write(f"{self.high_score}")
