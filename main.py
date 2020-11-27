# from turtle import Turtle, Screen
from game_GUI import game_GUI  # , width_limit, height_limit
import game_engine
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


# Constants
FOOD_COLLISION_LIMIT = 15


# Functions
def game_over():
    score_board.game_over()
    return False


# MAIN --------------------------------------------------------------
# Game components and actions
screen = game_GUI()
score_board = ScoreBoard()

snake = Snake()
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
food = Food()

# Game
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if game_engine.detect_food_collision(snake.head.distance(food)):
        score_board.increase_score()
        snake.extend_snake()
        food.refresh()

    # Detect collision with wall
    if game_engine.detect_wall_collision(snake.head):
        game_is_on = game_over()

    # Detect collision with tail
    if game_engine.detect_tail_collision(snake.segments):
        game_is_on = game_over()

screen.exitonclick()
