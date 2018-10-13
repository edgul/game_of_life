#!/usr/bin/python
#

from graphics import *
from Button import Button

from Frame import Frame


class MainWindow:

	def __init__(self, win, rows, columns):

		self.win = win

		win_height = win.getHeight()
		win_width = win.getWidth()

		message_frame_height = int(win_height * .15)
		controller_frame_height = int(win_height * .15)
		matrix_frame_height = win_height - message_frame_height - controller_frame_height

		frame_msg = Frame(Point(0, 0), Point(win_width, message_frame_height), False)
		frame_matrix = Frame(Point(0, message_frame_height), Point(win_width, matrix_frame_height), False)
		frame_controller = Frame(Point(0, message_frame_height + matrix_frame_height), Point(win_width, controller_frame_height), False)

		cell_width = int(win_width / columns)
		cell_height = int(matrix_frame_height / rows)
		cell_vector = Point(cell_width, cell_height)

		# matrix
		self.cell_buttons = []
		for i in range(0, columns):
			for j in range(0, rows):
				cell_anchor_x = frame_matrix.top_left().getX() + i * cell_width
				cell_anchor_y = frame_matrix.top_left().getY() + j * cell_height
				cell_anchor_pt = Point(cell_anchor_x, cell_anchor_y)
				cell_button = Frame(cell_anchor_pt, cell_vector, False)
				self.cell_buttons.append(cell_button)

		# controller
		pt_vector = Point(50, 20)
		pt_quit = Point(win_width * 0.75, frame_controller.center().getY())
		pt_start = Point(win_width * 0.4, frame_controller.center().getY())

		center_points = True
		self.button_start = Button(pt_start, pt_vector, "Start / Stop", center_points)
		self.button_quit = Button(pt_quit, pt_vector, "Quit", center_points)

	def cell_clicked(self, point):
		result = -1

		for i in range(0, len(self.cell_buttons)):
			if self.cell_buttons[i].contains(point):
				result = i
				break

		return result

	def start_clicked(self, point):
		return self.button_start.contains(point)

	def quit_clicked(self, point):
		return self.button_quit.contains(point)

	def draw(self, win, matrix):

		# draw matrix
		for i in range(0, matrix.length()):
			cell = matrix.cell_at(i)

			# update color
			cell_color = "grey"
			if cell.get_alive():
				cell_color = "green"

			self.cell_buttons[i].set_background_color(cell_color)
			self.cell_buttons[i].draw(win)

		# draw buttons
		self.button_quit.draw(win)
		self.button_start.draw(win)

	def redraw(self, win, matrix):

		# draw matrix
		for i in range(0, matrix.length()):
			cell = matrix.cell_at(i)

			# update color
			cell_color = "grey"
			if cell.get_alive():
				cell_color = "green"

			self.cell_buttons[i].set_background_color(cell_color)
			self.cell_buttons[i].redraw(win)

		# draw buttons
		self.button_quit.redraw(win)
		self.button_start.redraw(win)