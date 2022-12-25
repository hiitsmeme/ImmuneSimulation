import pyray as pr
from Cell import Cell

class Bacteria(Cell):
    def __init__(self, screen_width: int, screen_height: int, color=pr.GREEN):
        super().__init__(screen_width, screen_height, color)
