# MainWindow.py
#
#

from Tkinter import *
from Matrix import Matrix
from Game import Game


class MainWindow(Frame):

    def __init__(self, master, rows, columns):
        Frame.__init__(self, master)

        self.matrix = Matrix(master, rows, columns)
        self.matrix.grid(row=0, column=0)

        self.game = Game(rows, columns)
        self.game.set_matrix(self.matrix)

        self.start_button = Button(master, text="Start")
        self.start_button.grid(row=1, column=0)
        self.start_button["command"] = self.game.start_clicked

        self.quit_button = Button(master, text="Quit")
        self.quit_button.grid(row=1, column=1)
        self.quit_button["command"] = self.quit

        self.master = master
        master.title("Life")

        # override the "X" close button
        self.master.protocol("WM_DELETE_WINDOW", self.quit)

    def quit(self):
        print "quitting"
        self.game.quit_clicked()
        self.master.quit()
