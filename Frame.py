#!/usr/bin/python
#

from Controller import *
from Matrix import Matrix


# Abstract container class
class Frame:

	def init(self, bottomLeftCoord, topRightCoord ):
		self.bottomLeftCoord = bottomLeftCoord
		self.topRightCoord = topRightCoord
		self.backgroundColor = "grey"

	def inFrame( self, pt):
		return self.bottomLeftCoord.getX() < pt.getX() and \
			self.bottomLeftCoord.getY() > pt.getY() and \
			self.topRightCoord.getY() < pt.getY() and \
			self.topRightCoord.getX() > pt.getX()
			


# Holds the view of the matrix of cells
class MatrixFrame( Frame ):

	def __init__(self, bottomLeftCoord, topRightCoord, cellWidth, cellHeight, numCols, numRows, win  ):
		self.init(bottomLeftCoord,topRightCoord )

		#build matrix
		self.matrix = Matrix(bottomLeftCoord, topRightCoord, cellWidth, cellHeight, numCols, numRows, win)


# Holds buttons to interact with
class ControllerFrame( Frame ):

	def __init__(self, bottomLeftCoord, topRightCoord, win ):
		self.init(bottomLeftCoord, topRightCoord ) 
		self.controller = Controller(bottomLeftCoord, topRightCoord, win)


# Holds messages to the user
class MessageFrame( Frame ):

	def __init__(self, bottomLeftCoord, topRightCoord ):
		self.init(bottomLeftCoord, topRightCoord ) 
		
	

