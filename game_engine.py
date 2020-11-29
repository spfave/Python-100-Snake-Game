from game_GUI import WINDOWWIDTH, WINDOWHEIGHT


# Constants
EDGE_OFFSET = 20
FOOD_COLLISION_LIMIT = 15
TAIL_COLLISION_LIMIT = 10


# Variables
width_limit = WINDOWWIDTH/2 - EDGE_OFFSET
height_limit = WINDOWHEIGHT/2 - EDGE_OFFSET


# Functions
def detect_food_collision(snake_head_to_food_distance):
    """ Evaluate if snake head is within distance of food to be considered a collision """
    return snake_head_to_food_distance < FOOD_COLLISION_LIMIT


def detect_wall_collision(snake_head):
    """ Evaluate if snake head is exiting game play area limits """
    return abs(snake_head.xcor()) > width_limit or abs(snake_head.ycor()) > height_limit


def detect_tail_collision(snake_segments):
    """ Evaluates if snake head has collided with the snake tail """
    for segment in snake_segments[1:]:  # excludes head segment
        if snake_segments[0].distance(segment) < TAIL_COLLISION_LIMIT:
            return True
    return False
