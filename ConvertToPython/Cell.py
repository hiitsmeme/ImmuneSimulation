import pyray as pr
import random

class Cell:
    def __init__(self, screen_width: int, screen_height: int,  posx: int, posy: int, radius: int, color):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.color = color

        self.radius = radius

        self.posx = posx
        self.posy = posy
        
        self.position = (self.posx, self.posy)

    # ---------- methods ----------- #
    def getPosition(self) -> dict:
        return self.position
    
    def updatePosition(self, update_factor_x, update_factor_y) -> None:
        # update randomly for now
        random_num_x = random.randint(0,11) # get num to be threshold
        random_num_y = random.randint(0,11)

        # update self.posx
        if (self.posx + update_factor_x <= self.screen_width - self.radius and random_num_x <= 50):
            self.posx += update_factor_x 
        elif self.posx - update_factor_x >= self.radius:
            self.posx -= update_factor_x

        # update self.posy
        if self.posy + update_factor_y <= self.screen_height - self.radius and random_num_y > 50:
            self.posy += update_factor_y 
        elif self.posy - update_factor_y >= self.radius:
            self.posy -= update_factor_y

        # update position
        self.position = (self.posx, self.posy)
    
    def draw(self):
        pr.draw_circle(self.posx, self.posy, self.radius, self.color)