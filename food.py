from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("orange")
        self.speed("fastest")
        self.respawn()

    def respawn(self):
        self.goto(randint(-280, 280), randint(-280, 280))
