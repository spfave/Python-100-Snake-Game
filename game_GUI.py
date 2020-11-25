from turtle import Screen


# Constants
WINDOWWIDTH = 600
WINDOWHEIGHT = 600
EDGE_OFFSET = 20


# Variables
width_limit = WINDOWWIDTH/2 - EDGE_OFFSET
height_limit = WINDOWHEIGHT/2 - EDGE_OFFSET


# Functions
def game_GUI():
    """ Returns game screen """

    screen = Screen()
    screen.setup(width=WINDOWWIDTH, height=WINDOWHEIGHT)
    screen.tracer(0)
    screen.title("Snake Game")
    screen.bgcolor("black")

    return screen
