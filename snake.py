from turtle import Turtle, Screen
import time

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.createsnake()

    def createsnake(self):
        for a in range(3):
            STARTING_WIDTH = 0
            my_snake = Turtle("square")
            my_snake.color("red")
            my_snake.penup()
            my_snake.teleport(STARTING_WIDTH, 0)
            STARTING_WIDTH -= 20
            self.segments.append(my_snake)

    def new_segment(self, position):
            my_snake = Turtle("square")
            my_snake.color("red")
            my_snake.penup()
            my_snake.teleport(position[0], position[1])
            self.segments.append(my_snake)

 
    def extend(self):
        self.new_segment(self.segments[-1].position())


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
