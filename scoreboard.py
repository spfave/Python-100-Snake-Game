from turtle import Turtle
from game_GUI import WINDOWHEIGHT

# Constants
TEXT_SIZE = 16
TEXT_ALIGNMENT = "center"
FONT_STYLE = ("Courier", TEXT_SIZE, "bold")


# Variables
scoreboard_position = (0, WINDOWHEIGHT/2-TEXT_SIZE*2)


# Classes
class ScoreBoard(Turtle):
    """  """

    def __init__(self):
        """  """
        super().__init__()
        self.score = 0
        self.read_high_score()
        self.hideturtle()
        self.penup()
        self.goto(scoreboard_position)
        self.color("white")
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.high_score}",
                   align=TEXT_ALIGNMENT, font=FONT_STYLE)

    def increase_score(self):
        self.score += 1
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=TEXT_ALIGNMENT, font=FONT_STYLE)

    def game_reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()
        self.score = 0
        self.write_score()

    def read_high_score(self):
        with open("highscore.txt", mode="r") as file:
            self.high_score = int(file.read())

    def write_high_score(self):
        with open("highscore.txt", mode="w") as file:
            file.write(str(self.high_score))
