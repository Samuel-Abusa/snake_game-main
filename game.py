import turtle
from time import sleep
from turtle import Turtle
from random import randint
from scoreboard import Scoreboard

COLLISSION_DISTANCE = 15


class Game:
    def __init__(self) -> None:
        self.segments = []
        self.add_segment(3)
        self.head = self.segments[0]
        self.food = Turtle("circle")
        self.food.color("orange")
        self.food.penup()
        self.food.speed("fastest")

    def add_segment(self, segment_length):
        for n in range(segment_length):
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.hideturtle()
            if segment_length > 1:
                segment.goto(x=-n * 20, y=0)
            else:
                segment.goto(self.segments[-1].position())
            self.segments.append(segment)
            segment.showturtle()

    def refresh_food(self, screen_width, screen_height):
        random_xcor = randint(-int(screen_width / 2) + 20, int(screen_width / 2) - 20)
        random_ycor = randint(-int(screen_height / 2) + 20, int(screen_height / 2) - 20)
        self.food.goto(random_xcor, random_ycor)

    def game_over(self, screen_height, screen_width, board):
        tail_collision = False

        for segment in self.segments[1:]:
            if segment.distance(self.head) <= COLLISSION_DISTANCE:
                tail_collision = True

        if (
            self.head.xcor() > (screen_width / 2)
            or self.head.xcor() < -(screen_width / 2)
            or self.head.ycor() > (screen_height / 2)
            or self.head.ycor() < -(screen_height / 2)
            or tail_collision
        ):
            board.final_score()
            turtle.done()
            return True

    def play(self, screen):
        s_width = screen.window_width()
        s_height = screen.window_height()
        scoreboard = Scoreboard(s_height)
        self.refresh_food(s_width, s_height)

        while True:
            screen.update()
            sleep(0.1)

            for segment_num in range(len(self.segments) - 1, 0, -1):
                new_xcor = self.segments[segment_num - 1].xcor()
                new_ycor = self.segments[segment_num - 1].ycor()
                self.segments[segment_num].goto(new_xcor, new_ycor)

            self.head.forward(20)

            if self.game_over(s_height, s_width, scoreboard):
                break

            if self.food.distance(self.head) <= COLLISSION_DISTANCE:
                self.add_segment(1)
                scoreboard.update_score()
                self.refresh_food(s_width, s_height)
