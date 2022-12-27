from Bacteria import Bacteria

class Creator:
    def __init__(self, cells, screen_width, screen_height):
        self.cells = cells

        self.screen_width = screen_width
        self.screen_height = screen_height

    def createBacteria(self, wound_pos, radius=5):
        new_bac = Bacteria(self.screen_width, self.screen_height, wound_pos[0], wound_pos[1], radius)
        self.cells["bacteria"].append(new_bac)

    def createMacrophage(self, radius=10):
        # create at random spot
        pass

