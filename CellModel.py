
# CellModel.py
#
#


class CellModel:

    def __init__(self, index):
        self.alive = False
        self.index = index

    def set_alive(self, on):
        self.alive = on

    def get_alive(self):
        return self.alive

