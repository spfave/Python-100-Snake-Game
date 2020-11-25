from turtle import Turtle
from game_GUI import width_limit, height_limit
from random import randint


# Functions
def random_location():
    """ Return random coordinates within game space limits """
    horz_coord = randint(-width_limit, width_limit)
    vert_coord = randint(-height_limit, height_limit)
    return (horz_coord, vert_coord)


# Classes
class Food(Turtle):
    """  """

    def __init__(self):
        """  """
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(random_location())
