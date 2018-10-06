#!/usr/bin/python
#
# Border.py

from graphics import *

#  Contains lines to draw cell perimeter
class Border:

    def __init__(self, pt1, pt2):
        # store corner points of the cell
        self.tr = Point(pt2.x, pt1.y)
        self.bl = Point(pt1.x, pt2.y)

        # build lines
        self.topborder = Line(pt1, self.tr)
        self.leftborder = Line(pt1, self.bl)
        self.rightborder = Line(self.tr, pt2)
        self.bottomborder = Line(self.bl, pt2)

    # draws lines around the cell
    def draw(self, win):
        self.topborder.draw(win)
        self.leftborder.draw(win)
        self.rightborder.draw(win)
        self.bottomborder.draw(win)
