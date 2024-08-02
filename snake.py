from turtle import Turtle


class Snake:
    def __init__(self):
        self.segments = []
        self.add_segment(3)
        self.head = self.segments[0]

    def add_segment(self, num_of_segments):
        for n in range(num_of_segments):
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.hideturtle()

            if num_of_segments == 3:
                segment.goto(-(20 * n), 0)
            else:
                segment.goto(self.segments[-1].position())

            self.segments.append(segment)
            segment.showturtle()

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def collision_with_tail(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) <= 10:
                return True
        return False

    def kill_snake(self):
        for segment in self.segments:
            segment.hideturtle()
            segment.goto(10000, 10000)
        self.segments.clear()
