from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
INITIAL_SEGMENTS = 3


class Snake:

        def __init__(self):
                self.segments = []
                self.create_snake()
                self.head = self.segments[0]

        def create_snake(self):
                x_coordinate = 0
                y_coordinate = 0
                for _ in range(INITIAL_SEGMENTS):
                        self.add_segment((x_coordinate, y_coordinate))
                        x_coordinate -= 20

        def add_segment(self, position):
                # create 1 obj at each time
                new_object = Turtle(shape="square")
                new_object.penup()
                new_object.color("blue", "blue")
                new_object.goto(position)
                self.segments.append(new_object)

        def extend_segment(self):
                # add new segment to snake list
                """the position of last segment will move forward when move. so the extended segment will replace in the last of the list and combine with the list"""
                self.add_segment(self.segments[-1].pos())

        def move(self):
                """move position third to second but not first.First is freely move forward"""
                for seg_num in range(len(self.segments) - 1, 0, -1):
                        former_one_xsegment = self.segments[seg_num - 1].xcor()
                        former_one_ysegment = self.segments[seg_num - 1].ycor()
                        self.segments[seg_num].goto(former_one_xsegment, former_one_ysegment)
                self.head.forward(MOVE_DISTANCE)

        def up(self):
                if self.head.heading() != DOWN:
                        self.head.setheading(UP)

        def down(self):
                if self.head.heading() != UP:
                        self.head.setheading(DOWN)

        def left(self):
                if self.head.heading() != RIGHT:
                        self.head.setheading(LEFT)

        def right(self):
                if self.head.heading() != LEFT:
                        self.head.setheading(RIGHT)
