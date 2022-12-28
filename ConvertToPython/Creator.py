import random

from Bacteria import Bacteria
from Macrophage import Macrophage
from Cytokine import Cytokine

class Creator:
    def __init__(self, cells, screen_width, screen_height):
        self.cells = cells

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.macrophage_count = 0
        self.bacteria_count = 0

    # create a new bacterium at the wound (for now middle of window)
    def createBacteria(self, wound_pos, radius=5):
        if self.bacteria_count < 300:
            new_bac = Bacteria(self.screen_width, self.screen_height, wound_pos[0], wound_pos[1], radius)
            self.cells["bacteria"].append(new_bac)

        self.bacteria_count += 1

    
    # create a new macrophage at a random point
    def createMacrophage(self, radius=10):
        # create at random spot
        if self.macrophage_count < 10:
            posx = random.randint(0, self.screen_width - radius)
            posy = random.randint(0, self.screen_height - radius)

            new_macro = Macrophage(self.screen_width, self.screen_height, posx, posy, radius)
            self.cells["macrophages"].append(new_macro)

        self.macrophage_count += 1

    def createCytokines(self, macrophage):
        origin = (macrophage.posx, macrophage.posy)

        # create new Cytokines in a pattern
        # left
        cyt1 = Cytokine(self.screen_width, self.screen_height, origin[0] - macrophage.radius, origin[1], (-5, 0))
        # top
        cyt2 = Cytokine(self.screen_width, self.screen_height, origin[0], origin[1] + macrophage.radius, (0, 5))
        # right
        cyt3 = Cytokine(self.screen_width, self.screen_height, origin[0] + macrophage.radius, origin[1], (5, 0))
        # bottom
        cyt4 = Cytokine(self.screen_width, self.screen_height, origin[0], origin[1] - macrophage.radius, (0, -5))

        self.cells["cytokines"].append(cyt1)
        self.cells["cytokines"].append(cyt2)
        self.cells["cytokines"].append(cyt3)
        self.cells["cytokines"].append(cyt4)


        

