import pyray as pr
from Cell import Cell
from Bacteria import Bacteria

class Macrophage(Cell):

    def __init__(self,screen_width: int, screen_height: int, posx: int, posy: int, radius: int, color=pr.RED, range=20):
        super().__init__(screen_width, screen_height, posx, posy, radius, color)
        # range in which it can kill bacteria
        self.range = range

    def draw(self):
        # draw range as a circle
        pr.draw_circle(self.posx, self.posy, self.range, pr.LIGHTGRAY)
        super().draw()

    # checks for overlap between self and some bacteria
    # returns false if not in range, true if it is
    def killBacteria(self, other: Bacteria) -> bool:
        return pr.check_collision_circles(self.getPosition(), float(self.radius), other.getPosition(), float(other.radius))


    

