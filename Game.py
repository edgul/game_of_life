#!/usr/bin/python
#
# Game.py

from Frame import *

# window init and game logic ; contains frames for everything else

class Game:

	def __init__(self):

		#define window dimensions
		WINDOWWIDTH = 750
		WINDOWHEIGHT = 750

		#define frame dimensions
		MESSAGEFRAMEHEIGHT = 75
		CONTROLLERFRAMEHEIGHT = 75
		MATRIXFRAMEHEIGHT = WINDOWHEIGHT - MESSAGEFRAMEHEIGHT - CONTROLLERFRAMEHEIGHT
	
		#define cell dimensions	
		CELLHEIGHT = 27
		CELLWIDTH = 27

		#calculate number of columns & rows
		numColumns = WINDOWWIDTH/CELLWIDTH
		numRows = WINDOWHEIGHT/CELLHEIGHT

		#points for frames
		msgFrameBottomLeft = Point( 0, MESSAGEFRAMEHEIGHT )
		msgFrameTopRight = Point ( WINDOWWIDTH , 0 )

		matrixFrameBottomLeft = Point( 0, MESSAGEFRAMEHEIGHT + MATRIXFRAMEHEIGHT )
		matrixFrameTopRight = Point( WINDOWWIDTH, MESSAGEFRAMEHEIGHT)

		controllerFrameBottomLeft = Point( 0, WINDOWHEIGHT )
		controllerFrameTopRight = Point( WINDOWWIDTH, WINDOWHEIGHT - CONTROLLERFRAMEHEIGHT ) 

		#create graphics window 
		self.win = GraphWin("life", WINDOWWIDTH, WINDOWHEIGHT)		

		#build frame and controller
		self.matrixFrame = MatrixFrame(matrixFrameBottomLeft, matrixFrameTopRight, CELLWIDTH, CELLHEIGHT, numColumns, numRows, self.win) 
		self.controllerFrame = ControllerFrame(controllerFrameBottomLeft, controllerFrameTopRight, self.win)
		self.messageFrame = MessageFrame( msgFrameBottomLeft, msgFrameTopRight ) 

		#loop until quit
		while not( self.controllerFrame.controller.getQuit()):	

			#loop until start game
			while not(self.controllerFrame.controller.getGo()):
				print "click",
				clickpt = self.win.getMouse()	

				if self.matrixFrame.inFrame( clickpt ):
					for i in self.matrixFrame.matrix.cells:
						if i.withinCell(clickpt):
							i.click()
							i.redraw(self.win) 		##necessary?
							break

				elif self.controllerFrame.inFrame(clickpt):
					if clickpt.getX() > 550 and clickpt.getX() < 590:
						if clickpt.getY() > 700 :
							print "quit"
							#quit()
							self.controllerFrame.controller.quit.toggleGO()
						
					elif clickpt.getX() > 250 and clickpt.getX() < 330:
						print "start/stop"
						if clickpt.getY() > 700 :
							self.controllerFrame.controller.toggleGO()
								
			self.runGame()			
		
	def runGame(self):
		#update status list
		self.matrixFrame.matrix.updateStatusList()

		#iterate through orig, removing or adding based on copy list	
		for i in range(0, len(self.matrixFrame.matrix.cells)):
			#count neightbours that are alive
			neighbourCount = self.matrixFrame.matrix.countNeighbours(i)					
	
			#cell is alive
			if self.matrixFrame.matrix.cells[i].status:
				#cell dies:
				if (neighbourCount < 2 or neighbourCount > 3):
					self.matrixFrame.matrix.kill(i)
				#stays alive:
				else:
					self.matrixFrame.matrix.live(i)
			#cell is dead
			else:
				#revives:
				if (neighbourCount == 3):
					self.matrixFrame.matrix.live(i)
				#stays dead:
				else:
					self.matrixFrame.matrix.kill(i)

		#sleep after each pass
		time.sleep(2)


