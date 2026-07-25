from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        

    def create_snake(self):
        for position in STARTING_POSITIONS:
            segment = Turtle()
            segment.color("white")
            segment.shape("square")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)
        #print(self.segments)