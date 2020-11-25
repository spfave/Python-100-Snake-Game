# from turtle import Turtle, Screen
from game_GUI import game_GUI, width_limit, height_limit
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


# Constants
FOODCOLLISIONLIMIT = 15


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

    # Detect collision food
    if snake.head.distance(food) < FOODCOLLISIONLIMIT:
        score_board.increase_score()
        snake.extend_snake()
        food.refresh()

    # Detect collision with wall
    if abs(snake.head.xcor()) > width_limit or abs(snake.head.ycor()) > height_limit:
        game_is_on = False
        score_board.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:  # excludes head segment
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()

screen.exitonclick()


def game_over():
    score_board.game_over()
    game_is_on = False
    return game_is_on
