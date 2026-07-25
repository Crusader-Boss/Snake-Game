from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        

    def create_snake(self):
        for position in STARTING_POSITIONS:
            segment = Turtle()
            segment.color("white")
            segment.shape("square")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)
        #print(self.segments)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(
            self.segments[i - 1].xcor(),
            self.segments[i - 1].ycor()
            )
        self.head.forward(20)
