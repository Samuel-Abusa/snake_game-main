import turtle
from time import sleep
from turtle import Turtle
from random import randint
from scoreboard import Scoreboard


class Game:
    def __init__(self) -> None:
        self.segments = []
        self.create_snake(7)
        self.head = self.segments[0]
        self.score = 0
        self.food = Turtle("circle")
        self.food.color("orange")
        self.food.penup()
        self.food.speed("fastest")

    def create_snake(self, segment_length):
        for n in range(segment_length):
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.hideturtle()
            if segment_length > 1:
                segment.goto(x=-n * 20, y=0)
            else:
                segment.goto(self.segments[len(self.segments) - 1].position())
            self.segments.append(segment)
            segment.showturtle()

    def refresh_food(self, screen_width, screen_height):
        random_xcor = randint(-int(screen_width / 2) + 20, int(screen_width / 2) - 20)
        random_ycor = randint(-int(screen_height / 2) + 20, int(screen_height / 2) - 20)
        self.food.goto(random_xcor, random_ycor)

    def game_over(self, screen_height, screen_width, board):
        if (
            self.head.xcor() > (screen_width / 2)
            or self.head.xcor() < -(screen_width / 2)
            or self.head.ycor() > (screen_height / 2)
            or self.head.ycor() < -(screen_height / 2)
        ):
            board.final_score(self.score)
            turtle.done()

    def play(self, screen):
        s_width = screen.window_width()
        s_height = screen.window_height()
        scoreboard = Scoreboard(s_height)

        scoreboard.update_score(self.score)
        self.refresh_food(s_width, s_height)

        while True:
            screen.update()
            sleep(0.1)

            for segment_num in range(len(self.segments) - 1, 0, -1):
                new_xcor = self.segments[segment_num - 1].xcor()
                new_ycor = self.segments[segment_num - 1].ycor()
                self.segments[segment_num].goto(new_xcor, new_ycor)

            self.head.forward(10)

            self.game_over(s_height, s_width, scoreboard)

            if self.food.distance(self.head) <= 15:
                self.score += 1
                self.create_snake(1)
                scoreboard.update_score(self.score)
                self.refresh_food(s_width, s_height)
