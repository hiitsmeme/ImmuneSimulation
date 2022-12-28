class Tracker:
    def __init__(self, cells, screen_width, screen_height, creator):
        self.cells = cells
        self.creator = creator

        self.screen_width = screen_width
        self.screen_height = screen_height

    # ------------methods---------- #

    # checks for overlap between cell and bacteria
    def killBacteria(self, enemies: list, immune_cells: list) -> None:
        for cell in immune_cells:
            for i, enemy in enumerate(enemies):
                if cell.killBacteria(enemy):
                    enemies.pop(i)

                    # release cytokines
                    self.creator.createCytokines(cell)

    def killCytokines(self, cytokines) -> None:
        for i, cyto in enumerate(cytokines):
            if cyto.posx <= 10 or cyto.posx >= self.screen_width - 10:
                cytokines.pop(i)
            elif cyto.posy <= 10 or cyto.posy >= self.screen_height - 10:
                cytokines.pop(i)

    def killMacrophages(self, macrophages) -> None:
        for i, macro in enumerate(macrophages):
            if macro.suicide():
                macrophages.pop(i)


        
                    
        
