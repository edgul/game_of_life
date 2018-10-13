#!/usr/bin/python
#
# Matrix.py

from Cell import Cell


class Matrix:

    def __init__(self, numRows, numCols ):

        self.rows = numRows
        self.columns = numCols
        self.cells = Matrix.empty_cells(self.rows, self.columns)

    def print_cells(self):
        for cell in self.cells:
            print cell.get_alive(),
        print

    @staticmethod
    def empty_cells(rows, columns):
        cells = []
        for i in range(0, rows * columns):
            cells.append(Cell(i))
        return cells

    def length(self):
        return len(self.cells)

    def cell_at(self, i):
        cell = -1

        if 0 <= i < len(self.cells):
            cell = self.cells[i]

        return cell

    def neighbours(self, cell):
        neighbours = []
        if self.cell_tr(cell) != -1:      neighbours.append(self.cell_tr(cell))
        if self.cell_tm(cell) != -1:      neighbours.append(self.cell_tm(cell))
        if self.cell_tl(cell) != -1:      neighbours.append(self.cell_tl(cell))
        if self.cell_right(cell) != -1:   neighbours.append(self.cell_right(cell))
        if self.cell_left(cell) != -1:    neighbours.append(self.cell_left(cell))
        if self.cell_br(cell) != -1:      neighbours.append(self.cell_br(cell))
        if self.cell_bm(cell) != -1:      neighbours.append(self.cell_bm(cell))
        if self.cell_bl(cell) != -1:      neighbours.append(self.cell_bl(cell))
        return neighbours

    def last_column(self):
        return self.columns - 1

    def first_column(self):
        return 0

    def first_row(self):
        return 0

    def last_row(self):
        return self.rows - 1

    def cell_tr(self, cell):
        n_tr = -1

        if self.row(cell) != 0 and self.column(cell) != self.last_column():
            n_tr = self.cells[cell.index - self.columns + 1]

        return n_tr

    def cell_tm(self, cell):
        neighbour = -1

        if self.row(cell) != 0:
            neighbour = self.cells[cell.index - self.columns]

        return neighbour

    def cell_tl(self, cell):
        neighbour = -1

        if self.row(cell) != self.first_row() and self.column(cell) != self.first_column():
            neighbour = self.cells[cell.index - self.columns - 1]

        return neighbour

    def cell_left(self, cell):
        neighbour = -1

        if self.column(cell) != self.first_column():
            neighbour = self.cells[cell.index - 1]

        return neighbour

    def cell_right(self, cell):
        neighbour = -1

        if self.column(cell) != self.last_column():
            neighbour = self.cells[cell.index + 1]

        return neighbour

    def cell_br(self, cell):
        neighbour = -1

        if self.row(cell) != self.last_row() and self.column(cell) != self.last_column():
            neighbour = self.cells[cell.index + self.columns + 1]

        return neighbour

    def cell_bl(self, cell):
        neighbour = -1

        if self.row(cell) != self.last_row() and self.column(cell) != self.first_column():
            neighbour = self.cells[cell.index + self.columns - 1]

        return neighbour

    def cell_bm(self, cell):
        neighbour = -1

        if self.row(cell) != self.last_row():
            neighbour = self.cells[cell.index + self.columns]

        return neighbour

    def column(self, cell):
        return cell.index % self.columns

    def row(self, cell):
        return cell.index / self.columns


