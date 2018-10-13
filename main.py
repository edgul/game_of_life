#!/usr/bin/python
#
# main.py

from Game import Game
from UserInput import *


def main():

    ROWS = 10
    COLUMNS = 10

    WINDOW_WIDTH = 750
    WINDOW_HEIGHT = 750

    user_input = UserInput(ROWS, COLUMNS, WINDOW_WIDTH, WINDOW_HEIGHT)

    game = Game(ROWS, COLUMNS)

    user_input.set_game(game)

    user_input.input_loop()


main()
