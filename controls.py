class Controls:
    def __init__(self, segment) -> None:
        self.segment = segment
        self.control_func = {
            "Up": self.up,
            "Down": self.down,
            "Left": self.left,
            "Right": self.right,
        }

    def up(self):
        if self.segment.heading() != 270:
            self.segment.setheading(90)

    def down(self):
        if self.segment.heading() != 90:
            self.segment.setheading(-90)

    def left(self):
        if self.segment.heading() != 0:
            self.segment.setheading(180)

    def right(self):
        if self.segment.heading() != 180:
            self.segment.setheading(0)
