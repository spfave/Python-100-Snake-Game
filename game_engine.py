from game_GUI import WINDOWWIDTH, WINDOWHEIGHT


""" Refactoring Logic? 

-   What logic belongs to the game and what logic belongs to the game engine?
    1. Should the game engine only be determining collision
    2. If collision is detected specific the in-game response is executed by game logic

-   Should the game engine be a set of independent functions that act on objects in the game, or
-   Should the game engine be a class with methods that act on objects in the game
    1. If the game engine is a class what are its attributes?
    2. The Snake, Food, and Scoreboard instances I feel should be game attributes

"""


# Constants
EDGE_OFFSET = 20
FOOD_COLLISION_LIMIT = 15
TAIL_COLLISION_LIMIT = 10


# Variables
width_limit = WINDOWWIDTH/2 - EDGE_OFFSET
height_limit = WINDOWHEIGHT/2 - EDGE_OFFSET


# Classes
# class GameEngine():
#     """ Snake game engine """

#     def __init__(self):
#         """  """
#         pass


# Detect collision with food
def detect_food_collision(snake_head_to_food_distance):
    """ Evaluate if snake head is within distance of food to be considered a collision """
    return snake_head_to_food_distance < FOOD_COLLISION_LIMIT


# Detect collision with wall
def detect_wall_collision(snake_head):
    """ Evaluate if snake head is exiting game play area limits """
    return abs(snake_head.xcor()) > width_limit or abs(snake_head.ycor()) > height_limit


# Detect collision with tail
def detect_tail_collision(snake_segments):
    """ Evaluates if snake head has collided with the snake tail """
    for segment in snake_segments[1:]:  # excludes head segment
        if snake_segments[0].distance(segment) < TAIL_COLLISION_LIMIT:
            return True
    return False
