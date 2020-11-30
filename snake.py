from turtle import Turtle


# Constants
STARTING_POSITIONS = [(0, 0,), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
HEADING_UP = 90
HEADING_DOWN = 270
HEADING_LEFT = 180
HEADING_RIGHT = 0


# Classes
class Snake():
    """  """

    def __init__(self):
        """  """
        self.segments = []
        self.create_snake()
        [].clear()

    def create_snake(self):
        """ Create starting snake body and position for game start """
        for position in STARTING_POSITIONS:
            self.add_segment(position)
        self.head = self.segments[0]

    def reset(self):
        """ Set snake to starting configuration """
        for segment in self.segments:   # move Turtle segments off screen - how to delete Turtle?
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()

    def add_segment(self, position):
        """ Add body segment to snake """
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend_snake(self):
        """ Add segment to end of snake body """
        self.add_segment(self.segments[-1].position())

    def move(self):
        """ Control movement of snake """
        for segment in range(len(self.segments)-1, 0, -1):
            new_position = self.segments[segment-1].pos()
            self.segments[segment].goto(new_position)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != HEADING_DOWN:
            self.head.setheading(HEADING_UP)

    def down(self):
        if self.head.heading() != HEADING_UP:
            self.head.setheading(HEADING_DOWN)

    def left(self):
        if self.head.heading() != HEADING_RIGHT:
            self.head.setheading(HEADING_LEFT)

    def right(self):
        if self.head.heading() != HEADING_LEFT:
            self.head.setheading(HEADING_RIGHT)
