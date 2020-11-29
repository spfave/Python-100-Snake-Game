# Python 100 Days of Code: Snake Game

Course: 100 Days of Code - The Complete Python Pro Bootcamp for 2021
Course url: https://www.udemy.com/course/100-days-of-code/

Section 20,21: Build the Snake Game
Creation of the popular snake game in Python using the Turtle graphics module.

<br>

### Refactoring Thoughts 11/26/20

- What logic belongs to the game and what logic belongs to the game engine?

  1. Should the game engine only be determining collision
  2. If collision is detected specific the in-game response is executed by game logic

- Should the game engine be a class with methods that act on objects in the game

  1. If the game engine is a class what are its attributes?
  2. The Snake, Food, and Scoreboard instances I feel are game attributes not game engine attributes

- Should the game engine be a set of independent functions that act on objects in the game, or

  1. If game engine does not have attributes what would be the reason to make it a class

     - https://stackoverflow.com/questions/21883511/module-with-classes-with-only-static-methods
     - https://stackoverflow.com/questions/10388127/static-classes-in-python

     These two questions seem to answer my question and indicate going with independent functions is more correct/pythonic

- Should constants and variables below be in a separate module? game_parameters.py
