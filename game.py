import turtle
from time import sleep
from turtle import Turtle
from random import randint


class Game:
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.score = 0
        self.food = ""

    def create_snake(self):
        for n in range(7):
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(x=-n * 20, y=0)
            self.segments.append(segment)

    def generate_food(self, screen_width, screen_height):
        random_xcor = randint(-int(screen_width / 2) + 20, int(screen_width / 2) - 20)
        random_ycor = randint(-int(screen_height / 2) + 20, int(screen_height / 2) - 20)
        food = Turtle("circle")
        food.color("orange")
        food.penup()
        food.goto(x=random_xcor, y=random_ycor)
        self.food = food

    def grow(self):
        self.score += 1
        self.food.shape("square")
        self.food.color("white")
        self.segments.append(self.food)

    def game_over(self, screen_height, screen_width):
        if (
            self.head.xcor() > (screen_width / 2)
            or self.head.xcor() < -(screen_width / 2)
            or self.head.ycor() > (screen_height / 2)
            or self.head.ycor() < -(screen_height / 2)
        ):
            turtle.done()
            print(f"\nYour score is {self.score}\n\n")

    def play(self, screen):
        game_on = True
        s_width = screen.window_width()
        s_height = screen.window_height()
        self.generate_food(s_width, s_height)

        while game_on:
            screen.update()
            sleep(0.1)

            for segment_num in range(len(self.segments) - 1, 0, -1):
                new_xcor = self.segments[segment_num - 1].xcor()
                new_ycor = self.segments[segment_num - 1].ycor()
                self.segments[segment_num].goto(new_xcor, new_ycor)

            self.head.forward(10)

            self.game_over(s_height, s_width)

            if self.food.distance(self.head) <= 10:
                self.grow()
                self.generate_food(s_width, s_height)
