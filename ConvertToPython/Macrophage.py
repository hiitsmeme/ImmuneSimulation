import pyray as pr
from Cell import Cell

class Macrophage(Cell):

    def __init__(self,screen_width: int, screen_height: int, color=pr.RED, range=10):
        super().__init__(screen_width, screen_height, color)
        # range in which it can kill bacteria
        self.range = range

    

