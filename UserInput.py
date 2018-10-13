#!/usr/bin/python
#
# UserInput.py

from graphics import *
from MainWindow import MainWindow


class UserInput:

    def __init__(self, rows, columns, window_width, window_height):

        self.win = GraphWin("life", window_width, window_height)
        self.main_window = MainWindow(self.win, rows, columns)

    def window(self):
        return self.win

    def set_game(self, game):
        self.game = game

    def input_loop(self):
        self.main_window.draw(self.win, self.game.get_matrix())

        while True:

            self.main_window.redraw(self.win, self.game.get_matrix())

            # print "waiting for click"
            pt = self.win.getMouse()

            # print "x: ", pt.getX(), " y: ", pt.getY()

            cell_clicked = self.main_window.cell_clicked(pt)

            if cell_clicked != -1:
                cell = self.game.get_matrix().cell_at(cell_clicked)
                self.game.cell_clicked(cell)

            elif self.main_window.quit_clicked(pt):
                self.game.quit_clicked()
                self.win.close()
                break

            elif self.main_window.start_clicked(pt):
                self.game.start_clicked()
                break

        while True:
            self.main_window.redraw(self.win, self.game.get_matrix())

