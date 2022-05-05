from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "gray", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.start_speed = STARTING_MOVE_DISTANCE
        self.making_car()
        self.start_position()
        self.moving()

    def making_car(self):
        self.shape('square')
        self.color(choice(COLORS))
        self.setheading(180)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.start_position()

    def start_position(self):
        x_begin = randint(270, 600)
        y_begin = randint(-250, 250)
        self.goto(x_begin, y_begin)

    def moving(self):
        x_new = self.xcor() - self.start_speed
        y_new = self.ycor()
        self.goto(x_new, y_new)
        if x_new < randint(-330, -280):
            self.start_position()

    def speeding_up(self):
        self.start_speed += MOVE_INCREMENT
























