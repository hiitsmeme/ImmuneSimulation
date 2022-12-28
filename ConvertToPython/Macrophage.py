import pyray as pr
from Cell import Cell
from Bacteria import Bacteria
from Cytokine import Cytokine

class Macrophage(Cell):

    def __init__(self,screen_width: int, screen_height: int, posx: int, posy: int, radius=10, color=pr.RED, range=20):
        super().__init__(screen_width, screen_height, posx, posy, radius, color)
        # range in which it can kill bacteria
        self.range = range

        self.kill_count = 0

    def draw(self):
        # draw range as a circle
        pr.draw_circle(self.posx, self.posy, self.range, pr.LIGHTGRAY)
        super().draw()

    # checks for overlap between self and some bacteria
    # returns false if not in range, true if it is
    def killBacteria(self, other: Bacteria) -> bool:
        if pr.check_collision_circles(self.getPosition(), float(self.radius), other.getPosition(), float(other.radius)):
            self.kill_count += 1
        return pr.check_collision_circles(self.getPosition(), float(self.radius), other.getPosition(), float(other.radius))

    # returns true if cytokine is in range of
    def encounterCytokine(self, other: Cytokine) -> bool:
        return pr.check_collision_circles(self.getPosition(), float(self.radius), other.getPosition(), float(other.radius))

    # def updatePosition(self, update_factor_x, update_factor_y, cytokine=None) -> None:
    #     # check if a cytokine was encountered
    #     super().updatePosition(update_factor_x, update_factor_y)
        # if cytokine:
        #     self.posx += cytokine.posx - cytokine.last_x
        #     self.posy += cytokine.posy - cytokine.last_y
            
        #     self.position = (self.posx, self.posy)

    def suicide(self) -> bool:
        if self.kill_count >= 30:
            return True
        return False

        



    

