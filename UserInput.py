#!/usr/bin/python
#
# UserInput.py

from graphics import *
from MainWindow import MainWindow

class UserInput:

    def __init__(self, rows, columns, window_width, window_height):

        self.has_quit = False

        self.win = GraphWin("life", window_width, window_height)
        self.main_window = MainWindow(self.win, rows, columns)


    def window(self):
        return self.win

    def set_game(self, game):
        self.game = game

    def input_loop(self):
        self.main_window.draw(self.win, self.game.get_matrix())

        # init cells loop
        while True:

            self.main_window.redraw(self.win, self.game.get_matrix())
            pt = self.win.checkMouse()

            if pt is not None:

                cell_clicked = self.main_window.cell_clicked(pt)

                if cell_clicked != -1:
                    cell = self.game.get_matrix().cell_at(cell_clicked)
                    self.game.cell_clicked(cell)

                elif self.main_window.quit_clicked(pt):
                    self.quit()
                    break

                elif self.main_window.start_clicked(pt):
                    self.game.start_clicked()
                    break

        # game loop
        while not self.has_quit:

            self.main_window.redraw(self.win, self.game.get_matrix())
            pt = self.win.checkMouse()

            if pt is not None:

                if self.main_window.quit_clicked(pt):
                    self.quit()
                    break

    def quit(self):
        self.has_quit = True
        self.game.quit_clicked()
        self.win.close()
