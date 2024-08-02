from food import Food
from time import sleep
from snake import Snake
from turtle import Screen
from controls import Controls
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

food = Food()
scoreboard = Scoreboard()

while True:
    snake = Snake()
    controls = Controls(snake.head)
    game_controls = controls.control_func
    snake_is_alive = True

    for control in game_controls:
        screen.onkeypress(game_controls[control], control)

    while snake_is_alive:
        screen.update()
        sleep(0.1)

        snake.move()

        if snake.head.distance(food) <= 20:
            food.respawn()
            snake.add_segment(1)
            scoreboard.score += 1
            scoreboard.update_score()
        elif (
            snake.collision_with_tail()
            or abs(snake.head.xcor()) >= screen.window_width() / 2
            or abs(snake.head.ycor()) >= screen.window_height() / 2
        ):
            scoreboard.update_high_score()
            scoreboard.score = 0
            scoreboard.update_score()
            snake.kill_snake()
            snake_is_alive = False
