import pyray as pr
from Cell import Cell

class Bacteria(Cell):
    def __init__(self, screen_width: int, screen_height: int, posx: int, posy: int, radius: int, color=pr.GREEN):
        super().__init__(screen_width, screen_height, posx, posy, radius, color)
