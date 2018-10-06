#!/usr/bin/python
#
# Matrix.py

from Cell import Cell
from graphics import *

# Contains cells and statusList; can check life of neightbour cell given index
class Matrix:

    def __init__(self, bottomLeft, topRight, cellwidth, cellheight, numCols, numRows, win):

        # fields to init matrix
        self.numcol = numCols
        self.numrow = numRows
        self.numcells = self.numrow * self.numcol
        self.bottomLeft = bottomLeft
        self.topRight = topRight

        # create list of cells
        self.createCells(cellwidth, cellheight, win)

        # list to hold life statuses of cells
        self.statusList = self.buildStatusList()

        # draw list of cells
        for i in self.cells:
            i.draw(win)

    def createCells(self, cellwidth, cellheight, win):
        self.cells = []
        for i in range(int(self.topRight.getY()), int(self.bottomLeft.getY()), cellheight):
            for j in range(int(self.bottomLeft.getX()), self.numcol * cellwidth, cellwidth):
                pt = Point(j, i)
                self.cells.append(Cell(pt, Point(pt.x + cellwidth, pt.y + cellheight), win))

    # initializes the status list to match existing matrix
    def updateStatusList(self):
        for i in range(0, len(self.cells)):
            self.statusList[i] = self.cells[i].status

    # build list of life statuses
    def buildStatusList(self):
        statusList = []
        for i in range(0, len(self.cells)):
            statusList.append(self.cells[i].status)
        return statusList

    # returns neighbour state if calling cell is not in left column or top row
    def topleft(self, index):
        try:
            # if leftColumn or firstRow
            if ((index % self.numcol == 0) or index < self.numcol):
                return 0
            else:
                return self.statusList[index - self.numcol - 1]
        except:
            return 0

    # returns neighbour state if calling cell is not in first row
    def topmid(self, index):
        try:
            # if in first row
            if (index < self.numcol):
                return 0
            else:
                return self.statusList[index - self.numcol]
        except:
            return 0

    # returns neighbour state if calling cell is not in last column or top row
    def topright(self, index):
        try:
            if (index % self.numcol >= self.numcol - 1 or index < self.numcol):
                return 0
            else:
                return self.statusList[index - self.numcol + 1]
        except:
            return 0

    # returns neighbours state if calling cell is not in last row or last column
    def bottomright(self, index):
        try:
            if (index % self.numcol >= self.numcol - 1 or index / self.numrow >= self.numrow - 1):
                return 0
            else:
                return self.statusList[index + self.numcol + 1]
        except:
            return 0

    # returns neighbours state if calling cell is not in last row
    def bottommid(self, index):
        try:
            if (index / self.numrow >= self.numrow - 1):
                return 0
            else:
                return self.statusList[index + self.numcol]
        except:
            return 0

    # returns neighbours state if calling cell is not in last row or first column
    def bottomleft(self, index):
        try:
            if (index % self.numcol == 0 or index / self.numrow >= self.numrow - 1):
                return 0
            else:
                return self.statusList[index + self.numcol - 1]
        except:
            return 0

    # returns neighbours state if calling cell is not in first column
    def left(self, index):
        try:
            if (index % self.numcol == 0):
                return 0
            else:
                return self.statusList[index - 1]
        except:
            return 0

    # returns neighbours state if calling cell is not in last column
    def right(self, index):
        try:
            if (index % self.numcol >= self.numcol - 1):
                return 0
            else:
                return self.statusList[index + 1]
        except:
            return 0

    # count number of alive neighbours
    def countNeighbours(self, index):
        count = 0
        count += self.topleft(index)
        count += self.topmid(index)
        count += self.topright(index)
        count += self.right(index)
        count += self.left(index)
        count += self.bottomleft(index)
        count += self.bottommid(index)
        count += self.bottomright(index)
        return count

    # kill cell at index
    def kill(self, index):
        self.cells[index].turnOff()

    # revive cell at index
    def live(self, index):
        self.cells[index].turnOn()
