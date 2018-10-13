#!/usr/bin/python
#
# Frame.py

from graphics import Point
from graphics import Rectangle


class Frame:

    def __init__(self, pt_anchor, pt_vector, anchor_center_pt):
        if anchor_center_pt:
            self.pt_top_left = Point(pt_anchor.getX() - pt_vector.getX()/2, pt_anchor.getY() - pt_vector.getY()/2)
        else:
            self.pt_top_left = pt_anchor

        self.pt_vector = pt_vector

        self.rectangle = Rectangle(self.top_left(), self.bottom_right())
        self.rectangle.setFill("grey")

    def top_left(self):
        return self.pt_top_left

    def top_right(self):
        return Point(self.pt_top_left.getX() + self.pt_vector.getX(), self.pt_top_left.getY())

    def bottom_left(self):
        return Point(self.pt_top_left.getX(), self.pt_top_left.getY() + self.pt_vector.getY())

    def bottom_right(self):
        return Point(self.pt_top_left.getX() + self.pt_vector.getX(), self.pt_top_left.getY() + self.pt_vector.getY())

    def center(self):
        return Point(self.top_left().getX() + int(self.pt_vector.getX()/2), self.top_left().getY() + int(self.pt_vector.getY()/2))

    def contains(self, pt):
        pt_x = pt.getX()
        pt_y = pt.getY()

        within_x = False
        within_y = False

        if self.top_left().getX() <= pt_x <= self.top_right().getX():
            within_x = True

        if self.top_left().getY() <= pt_y <= self.bottom_left().getY():
            within_y = True

        return within_x and within_y

    def set_background_color(self, color):
        self.rectangle.setFill(color)

    def draw(self, win):
        self.rectangle.draw(win)

    def redraw(self, win):
        self.rectangle.undraw()
        self.rectangle.draw(win)