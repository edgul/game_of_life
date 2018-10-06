#!/usr/bin/python
#
# Cell.py

from Border import Border
from graphics import *


# Cell can be alive or dead, contains borders, points and background color;
class Cell:

    def __init__(self, pt1, pt2, win):
        # init to dead color
        self.color = 'grey'

        # width of cell?
        self.borderwidth = 50  ##__ this will need to be unhardcoded

        # alive = 1; dead = 0
        self.status = 0

        # corner points
        self.tl = pt1
        self.br = pt2
        self.tr = Point(pt2.x, pt1.y)
        self.bl = Point(pt1.x, pt2.y)

        # background?
        self.box = Rectangle(pt1, pt2)

        # make border
        self.border = Border(pt1, pt2)
        # init cell color
        self.updateColor(self.color)

    # draws the cell
    def draw(self, win):
        self.box.draw(win)
        self.border.draw(win)

    # reDraws the cell
    def redraw(self, win):
        self.box.undraw()
        self.box.draw(win)

    # turn cell ON
    def turnOn(self):
        self.status = 1
        self.color = 'green'
        self.updateColor(self.color)

    # turn cell off
    def turnOff(self):
        self.status = 0
        self.color = 'grey'
        self.updateColor(self.color)

    def updateColor(self, color):
        self.box.setFill(color)

    # returns true if pt is within the cell
    def withinCell(self, pt):
        return (pt.x < self.tr.x and pt.x > self.tl.x and pt.y < self.br.y and pt.y > self.tr.y)

    # toggle cell life ON/OFF
    def click(self):
        if (self.status):
            self.turnOff()
        else:
            self.turnOn()
