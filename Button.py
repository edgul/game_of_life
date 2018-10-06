#!/usr/bin/python
#
# Button.py

from graphics import *

class Button:

    def __init__(self, ON , color, pt, win, msg):
        self.textBox = Text( pt, msg )
        self.color = color
        self.ON = ON
        self.pt = pt
        self.win = win

    def getON(self):
        return self.ON

    def click(self):
        self.toggleColor()
        self.toggleReady()

    def toggleColor(self):
        if self.color == "grey":
            self.color = "green"
        else:
            self.color = "grey"
        self.textBox.setFill( self.color )

    def toggleReady(self):
        self.ON = not(self.ON)

    def draw(self):  # might also need a re-draw function
        self.textBox.draw(self.win)

    def getGo(self):
        return self.ON

