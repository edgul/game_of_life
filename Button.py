#!/usr/bin/python
#
# Button.py

from graphics import *
from Border import Border
from Frame import Frame


class Button(Frame):

    def __init__(self, pt_anchor, pt_vector, msg, anchor_center_pt):
        Frame.__init__(self, pt_anchor, pt_vector, anchor_center_pt)

        self.text = Text(self.pt_top_left, msg)
        self.border = Border(pt_anchor, pt_vector, anchor_center_pt)

    def draw(self, win):
        Frame.draw(self, win)
        self.border.draw(win)
        self.text.draw(win)

    def redraw(self, win):
        Frame.redraw(self, win)
        self.border.redraw(win)

        self.text.undraw()
        self.text.draw(win)
