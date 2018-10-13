#!/usr/bin/python
#
# Border.py

from graphics import *
from Frame import Frame


class Border(Frame):

    def __init__(self, pt_anchor, pt_vector, anchor_is_center):
        Frame.__init__(self, pt_anchor, pt_vector, anchor_is_center)

    def draw(self, win):
        Frame.draw(self, win)

        top_border = Line(self.top_left(), self.top_right())
        left_border = Line(self.top_left(), self.bottom_left())
        right_border = Line(self.top_right(), self.bottom_right())
        bottom_border = Line(self.bottom_left(), self.bottom_right())

        top_border.draw(win)
        left_border.draw(win)
        right_border.draw(win)
        bottom_border.draw(win)

    def redraw(self, win):
        Frame.redraw(self, win)

        top_border = Line(self.top_left(), self.top_right())
        left_border = Line(self.top_left(), self.bottom_left())
        right_border = Line(self.top_right(), self.bottom_right())
        bottom_border = Line(self.bottom_left(), self.bottom_right())

        top_border.draw(win)
        left_border.draw(win)
        right_border.draw(win)
        bottom_border.draw(win)
