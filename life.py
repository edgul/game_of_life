#!/usr/bin/python
#
# The game of life
# concept by John Horton Conway
# implementation by Ed Guloien
#
# ./life.py <arg>
# where <arg> is an integer of tiles to initialize the game with
# game will immediately begin upon placement of last tile
# watch life unfold!
#
# Notes:
#	works with python 2.7 (linux box)
# requires graphics.py
#	does not terminate gracefully (yet), kill via Ctrl + c in command prompt
# 
# Future adjustments:
#	screen sizing options
# cells sizing options
# timing options
#	dynamic placement
# pause/start buttons
# restart when game ends/stable


from graphics import *
import time
import sys

class Boarder:
	def __init__(self,pt1,pt2,win):
		self.tl = pt1
		self.br = pt2
		self.tr = Point(pt2.x, pt1.y)
		self.bl = Point(pt1.x, pt2.y)
		self.win = win
		self.topboarder = Line(pt1, self.tr)
		self.leftboarder = Line(pt1, self.bl)
		self.rightboarder = Line(self.tr, pt2)
		self.bottomboarder = Line(self.bl, pt2)
		#self.draw(self.win)
	
	def draw(self,win):
		self.topboarder.draw(win)
		self.leftboarder.draw(win)
		self.rightboarder.draw(win)
		self.bottomboarder.draw(win)
		
			
class Cell:
	def __init__(self,pt1,pt2, win):
		self.color = 'grey'
		self.borderwidth = 50
		self.status = 0
		self.win = win
		self.tl = pt1
		self.br = pt2
		self.tr = Point(pt2.x, pt1.y)
		self.bl = Point(pt1.x, pt2.y)
		self.box = Rectangle(pt1, pt2)
		self.border = Boarder(pt1,pt2, self.win)
		self.updateColor(self.color)
	
	def draw(self, win):
		self.box.draw(win)	
		self.border.draw(win)
	
	def redraw(self, win):
		self.box.undraw()	
		self.box.draw(win)	

	def turnOn(self):
		self.status = 1
		self.color = 'green'
		self.updateColor(self.color)
		
	def turnOff(self):
		self.status = 0
		self.color = 'grey'
		self.updateColor(self.color)
	
	def updateColor(self,color):
		self.box.setFill(color)

	def withinCell(self, pt):
		return (pt.x < self.tr.x and pt.x > self.tl.x and pt.y < self.br.y and pt.y > self.tr.y)

	def click(self):
		if (self.status):
			self.turnOff()
		else:
			self.turnOn()
	
	#def kill(self):
		#self.turnOff()
	#def live(self):
		#self.turnOn()	


class Matrix:
	def __init__(self,cellwidth,cellheight,win):
		self.cells = []	
		self.win = win
		self.numcol = win.width/cellwidth
		self.numrow = win.height/cellheight
		self.numcells = self.numrow * self.numcol
		#print self.numrow, self.numcol
		for i in range(0,self.numrow * cellheight,cellheight):
			for j in range(0, self.numcol * cellwidth,cellwidth):
				pt = Point(j, i)
				self.cells.append( Cell(pt,Point(pt.x+cellwidth, pt.y+cellheight),self.win))

		for i in self.cells:
			i.draw(self.win)

	def topleft(self, index,copylist):
		if ((index % self.numcol == 0) or index < self.numcol):
			return 0
		else:
			return copylist[index-self.numcol-1]
	
	def topmid(self, index,copylist):
		if (index < self.numcol):
			return 0
		else:
			return copylist[index-self.numcol]
	
	def topright(self, index,copylist):
		if (index % self.numcol >= self.numcol-1 or index < self.numcol):
			return 0
		else:
			return copylist[index-self.numcol+1]

	def bottomright(self, index,copylist):
		if (index % self.numcol >= self.numcol-1 or index/self.numrow >= self.numrow-1):
			return 0
		else:
			return copylist[index+self.numcol+1]

	def bottommid(self, index,copylist):
		if (index/self.numrow >= self.numrow-1):
			return 0
		else:
			return copylist[index+self.numcol]
	
	def bottomleft(self, index,copylist):
		if (index % self.numcol == 0 or index/self.numrow >= self.numrow-1):
			return 0
		else:
			return copylist[index+self.numcol-1]

	def left(self, index,copylist):
		if (index % self.numcol == 0):
			return 0
		else:
			return copylist[index-1]

	def right(self, index,copylist):
		if (index % self.numcol >= self.numcol-1):
			return 0
		else:
			return copylist[index+1]
	
	def countNeighbours(self, index, copylist):
		count = 0
		count += self.topleft(index,copylist)
		count += self.topmid(index,copylist)
		count += self.topright(index,copylist)
		count += self.right(index,copylist)
		count += self.left(index,copylist)
		count += self.bottomleft(index,copylist)
		count += self.bottommid(index,copylist)
		count += self.bottomright(index,copylist)
		#print "index: ", index, " count: ", count
		return count
	
	def kill(self,index):
		self.cells[index].turnOff()	

	def live(self,index):
		self.cells[index].turnOn()

def main():
	if ( len(sys.argv) != 2):
		print "ERR: Provide int number for number of cells to init"
	else:
		n = int(str(sys.argv[1]), base=10)
		win = GraphWin("wind",750,750)		
		#start = GraphWin("start")
		matrix = Matrix(50,50,win)
		copylist = []	
	
		#get get 10 clicks to init	
		for j in range(0,n):	
			clickpt = win.getMouse()	
			for i in matrix.cells:
				if i.withinCell(clickpt):
					i.click()
					i.redraw(win)
					break

		copylist = list() 
		for i in range (0, len(matrix.cells)):
			copylist.append(matrix.cells[i].status)

		#kick off the game
		while( True):
			#copy the list
			for i in range(0, len(matrix.cells)):
				copylist[i] = matrix.cells[i].status

			#iterate through orig, removing or adding based on copy list	
			for i in range(0,len(matrix.cells)):
				neighbourCount = matrix.countNeighbours(i,copylist)					
				if matrix.cells[i].status:
					if (neighbourCount < 2 or neighbourCount > 3):
						matrix.kill(i)
					else:
						matrix.live(i)
				else:
					if (neighbourCount == 3):
						matrix.live(i)
					else:
						matrix.kill(i)
			time.sleep(2)
		
main()

