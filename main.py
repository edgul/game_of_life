#!/usr/bin/python
#
# main.py

from Tkinter import Tk
from MainWindow import MainWindow

ROWS = 10
COLUMNS = 10

def main():

    WINDOW_WIDTH = 750
    WINDOW_HEIGHT = 750

    root = Tk()
    main_window = MainWindow(root, ROWS, COLUMNS)
    root.mainloop()

main()
