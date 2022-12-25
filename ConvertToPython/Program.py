import pyray as pr
import random

from Bacteria import Bacteria
from Macrophage import Macrophage

# open window
pr.init_window(800, 800, "ImmuneSimulation")
pr.set_target_fps(60)

# create new objects
bac1 = Bacteria(800, 800)
bac2 = Bacteria(800, 800)
bac3 = Bacteria(800, 800)

macro1 = Macrophage(800, 800)
macro2 = Macrophage(800, 800)


# dictionary that contains all elements to be rendered
cells = {
    "bacteria": [bac1, bac2, bac3],
    "macrophages": [macro1, macro2]
}

# game loop
while not pr.window_should_close():
    # draw cells
    pr.begin_drawing()
    pr.clear_background(pr.RAYWHITE)

    # draw all bacteria
    for bac in cells["bacteria"]:
        bac.draw()
    
    # draw all macrophages
    for macro in cells["macrophages"]:
        macro.draw()

    pr.end_drawing()

    # update positions
    for bac in cells["bacteria"]:
        update_factor_x = random.randint(-5,5)
        update_factor_y = random.randint(-5,5)
        bac.updatePosition(update_factor_x, update_factor_y)

    for macro in cells["macrophages"]:
        update_factor_x = random.randint(-5,5)
        update_factor_y = random.randint(-5,5)
        macro.updatePosition(update_factor_x, update_factor_y)

pr.close_window()


