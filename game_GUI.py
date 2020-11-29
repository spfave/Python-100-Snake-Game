from turtle import Screen


# Constants
WINDOWWIDTH = 600
WINDOWHEIGHT = 600


# Functions
def game_GUI():
    """ Returns game screen """

    screen = Screen()
    screen.setup(width=WINDOWWIDTH, height=WINDOWHEIGHT)
    screen.tracer(0)
    screen.title("Snake Game")
    screen.bgcolor("black")

    return screen
