#!/usr/bin/python
#
# Cell.py


class Cell:

    def __init__(self, index):
        self.index = index # TODO: needed?
        self.alive = False

    def set_alive(self, on):
        self.alive = on

    def get_alive(self):
        return self.alive
