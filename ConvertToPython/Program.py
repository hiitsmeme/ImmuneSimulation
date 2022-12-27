import pyray as pr
import random

from Bacteria import Bacteria
from Macrophage import Macrophage
from Tracker import Tracker
from Creator import Creator

# ---------- global vars ------------ #
screen_width = 800
screen_height = 800

# dictionary that contains all elements to be rendered

# create new objects
bac1 = Bacteria(screen_width, screen_height, int(screen_width / 2), int(screen_height / 2), 5)
bac2 = Bacteria(screen_width, screen_height, int(screen_width / 2), int(screen_height / 2), 5)
bac3 = Bacteria(screen_width, screen_height, int(screen_width / 2), int(screen_height / 2), 5)

macro1 = Macrophage(screen_width, screen_height, int(screen_width / 2 + 20), int(screen_height / 2), 10)
macro2 = Macrophage(screen_width, screen_height, int(screen_width / 2 + 20), int(screen_height / 2), 10)

cells = {
    "bacteria": [bac1, bac2, bac3],
    "macrophages": [macro1, macro2]
}

# create tracker instance
my_tracker = Tracker(cells)

# create Creator instance
my_creator = Creator(cells, screen_width, screen_height)

# ------------------------------------ #


# open window
pr.init_window(800, 800, "ImmuneSimulation")
pr.set_target_fps(60)


# game loop
while not pr.window_should_close():

    # ------------- create cells -----------------#
    my_creator.createBacteria((int(screen_width / 2), int(screen_height / 2)), 5)


    # -------------- draw cells --------------- #
    pr.begin_drawing()
    pr.clear_background(pr.RAYWHITE)

    # draw all bacteria
    for bac in cells["bacteria"]:
        bac.draw()
    
    # draw all macrophages
    for macro in cells["macrophages"]:
        macro.draw()

    pr.end_drawing()

    # ----------------------------------------- #

    # ----------- update positions ------------ #
    for bac in cells["bacteria"]:
        update_factor_x = random.randint(-5,5)
        update_factor_y = random.randint(-5,5)
        bac.updatePosition(update_factor_x, update_factor_y)

    for macro in cells["macrophages"]:
        update_factor_x = random.randint(-5,5)
        update_factor_y = random.randint(-5,5)
        macro.updatePosition(update_factor_x, update_factor_y)
    # ----------------------------------------- #

    # ------------ check for kills ----------#
    my_tracker.killBacteria(cells["bacteria"], cells["macrophages"])

pr.close_window()


