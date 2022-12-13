import random

class Cell:
    def __init__(self, screen_width: int, screen_height: int, update_factor: int, color):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.update_factor = update_factor
        self.color = color

        self.radius = 5

        self.posx = float(screen_width / 2 + 20)
        self.posy = float(screen_height / 2+ 20)
        
        self.position = {'X' : self.posx, 'Y' : self.posy}

    # ---------- methods ----------- #
    def getPosition(self) -> dict:
        return self.position
    
    def updatePosition(self) -> None:
        # update randomly for now
        random_num_x = random.randint(0,11) # get num to be threshold
        random_num_y = random.randint(0,11)

        # update self.posx
        if (self.posx + self.updateFactor <= self.screen_width - self.radius and random_num_x <= 50):
            self.posx += self.update_factor 
        elif self.posx - self.update_factor >= self.radius:
            self.posx -= self.update_factor

        # update self.posy
        if self.posy + self.updateFactor <= self.screen_height - self.radius and random_num_y > 50:
            self.posy += self.update_factor 
        elif self.posy - self.update_factor >= self.radius:
            self.posy -= self.update_factor

        # update position dict
        self.position.X = self.posx
        self.position.Y = self.posy

    
    def draw(self):
        pass


    def equalPositions(self, other):
        if isinstance(other, Cell):
            if self.position.X == other.position.X and self.position.Y == other.position.Y:
                return True
            else:
                return False
        else:
            raise TypeError