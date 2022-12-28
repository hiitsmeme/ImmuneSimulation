from Cell import Cell
import pyray as pr

class Cytokine(Cell):
    def __init__(self, screen_width, screen_height, posx, posy, update_factors: tuple, radius=4, color=pr.BLUE):
        super().__init__(screen_width, screen_height, posx, posy, radius, color)
    
        self.last_x = 0
        self.last_y = 0

        self.update_factors = update_factors

    def updatePosition(self) -> None:
        self.last_x = self.posx
        self.last_y = self.posy

        super().updatePosition(self.update_factors[0], self.update_factors[1])

