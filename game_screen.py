from turtle import Screen


class GameScreen:
    def __init__(self, controls) -> None:
        self.game_screen = Screen()
        self.game_screen.setup(600, 600)
        self.game_screen.bgcolor("black")
        self.game_screen.listen()
        self.game_screen.title("Snake Game")
        self.game_screen.tracer(0)

        for control_key in controls:
            self.game_screen.onkey(controls[control_key], control_key)
