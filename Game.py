#!/usr/bin/python
#
# Game.py

import threading
from MainWindow import *
from Matrix import Matrix

import copy


class Game:

	def __init__(self, rows, columns):

		self.matrix = Matrix(rows, columns)

		self.quitting = False
		self.active = False
		self.start = False

		self.t = threading.Thread(target=self.init_loop)
		self.t.start()

	def get_matrix(self):
		return self.matrix

	def cell_clicked(self, cell):
		if not self.active:
			cell.set_alive(not cell.get_alive())

	def start_clicked(self):
		if not self.active:
			self.start = True

	def quit_clicked(self):
		self.quitting = True

	def run(self):
		self.active = True
		print "starting simulation..."

		# update cells
		while not self.quitting:

			 # print "updating"
			# self.matrix.print_cells()

			matrix_cells_copy = copy.deepcopy(self.matrix.cells)

			for cell in self.matrix.cells:
				neighbours = self.matrix.neighbours(cell)

				active_neighbours = 0
				for neighbour in neighbours:
					if neighbour.get_alive():
						active_neighbours += 1

				# print active_neighbours,

				# update cell states
				if cell.alive:
					if active_neighbours < 2 or active_neighbours > 3:
						matrix_cells_copy[cell.index].set_alive(False)
				else:
					if active_neighbours == 3:
						matrix_cells_copy[cell.index].set_alive(True)

			self.matrix.cells = matrix_cells_copy

			# print
			# self.matrix.print_cells()

			time.sleep(1)

		self.active = False
		quit()

	def init_loop(self):
		print "init loop started"

		while True:
			if self.quitting or self.start:
				break

			time.sleep(1)

		if self.quitting:
			self.quit()
		elif self.start:
			self.run()

	def quit(self):
		print "quitting"


