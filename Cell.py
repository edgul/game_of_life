#!/usr/bin/python
#
# Cell.py

from Tkinter import Button
from CellModel import CellModel

class Cell(Button, CellModel):

    def __init__(self, master, index, callback=None):
        Button.__init__(self, master)
        CellModel.__init__(self, index)

        # register a callback
        self.callback = callback
        self.config(command=self.clicked)

        self.refresh()

    def set_model(self, model):
        self.alive = model.alive
        self.refresh()


    def model(self):
        new_model = CellModel(self.index)
        new_model.alive = self.alive
        return new_model

    def refresh(self):
        color = "gray"
        if self.alive: color = "green"
        self.config(bg=color)

    def clicked(self):
        self.alive = not (self.alive)
        self.refresh()

        if self.callback != None:
            self.callback()


