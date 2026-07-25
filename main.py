from turtle import Screen
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
#screen.tracer(0)

snake = Snake()

screen.exitonclick()