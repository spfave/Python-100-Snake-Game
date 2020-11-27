"""
-   What logic belongs to the game and what logic belongs to the game engine?
    1. Should the game engine only be determining collision
    2. If collision is detected specific the in-game response is executed by game logic

-   Should the game engine be a set of independent functions that act on objects in the game, or
-   Should the game engine be a class with methods that act on objects in the game
    1. If the game engine is a class what are its attributes?
    2. The Snake, Food, and Scoreboard instances I feel should be game attributes

"""

# Constants
FOOD_COLLISION_LIMIT = 15


# Variables
# width_limit = WINDOWWIDTH/2 - EDGE_OFFSET
# height_limit = WINDOWHEIGHT/2 - EDGE_OFFSET


# Classes
class GameEngine():
    """ Snake game engine """

    def __init__(self):
        """  """
        pass


# Detect collision with food
# if snake.head.distance(food) < FOOD_COLLISION_LIMIT:

# Detect collision with wall
# if abs(snake.head.xcor()) > width_limit or abs(snake.head.ycor()) > height_limit:


# Detect collision with tail
# for segment in snake.segments[1:]:  # excludes head segment
