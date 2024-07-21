from turtle import Screen


class GameScreen:
    def __init__(self, control_func) -> None:
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.title("Snake Game")
        self.screen.bgcolor("black")
        self.screen.tracer(0)
        self.screen.listen()

        for key in control_func:
            self.screen.onkeypress(control_func[key], key)
