from time import sleep
from turtle import Turtle
from random import randint


class Game:
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
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

    def check_collision(self, dist):
        pass

    def play(self, screen):
        game_on = True
        threshold_dist = 10
        self.generate_food(screen.window_width(), screen.window_height())

        while game_on:
            screen.update()
            sleep(0.1)

            for segment_num in range(len(self.segments) - 1, 0, -1):
                new_xcor = self.segments[segment_num - 1].xcor()
                new_ycor = self.segments[segment_num - 1].ycor()
                self.segments[segment_num].goto(new_xcor, new_ycor)

            self.segments[0].forward(10)

            if self.food.distance(self.segments[0]) <= threshold_dist:
                self.grow()
                self.generate_food(screen.window_width(), screen.window_height())
