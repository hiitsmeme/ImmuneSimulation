class Tracker:
    def __init__(self, cells):
        self.cells = cells

    # ------------methods---------- #

    # checks for overlap between cell and bacteria
    def killBacteria(self, enemies: list, immune_cells: list) -> None:
        for cell in immune_cells:
            for i, enemy in enumerate(enemies):
                if cell.killBacteria(enemy):
                    enemies.pop(i)

        
                    
        
