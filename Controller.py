#!/usr/bin/python
#
#
# Controller.py

from Button import Button
from graphics import *


class Controller:

	def __init__(self, bottomLeftCoord, topRightCoord, win):
		centerY = (topRightCoord.getY()+bottomLeftCoord.getY())/2

		quitPt = Point(topRightCoord.getX()*.75, centerY ) 
		runPt = Point(topRightCoord.getX()*.4, centerY)

		#button objects
		self.startStop = Button( 0, "green", runPt, win , "Start / Stop")  ##
		self.startStop.draw()
		self.quit = Button( 0, "black", quitPt, win, "Quit" ) 
		self.quit.draw()
	
	
	def getGo(self):
		return self.startStop.getON()


	def getQuit(self):
		return self.quit.getON()

	def toggleGO(self):
		self.startStop.toggleReady()
	


