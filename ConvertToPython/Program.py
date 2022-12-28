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

cells = {
    "bacteria": [],
    "macrophages": [],
    "cytokines": []
}

# create Creator instance
my_creator = Creator(cells, screen_width, screen_height)

# create tracker instance
my_tracker = Tracker(cells, screen_width, screen_height, my_creator)

# keep track of frame number
frame_counter = 0

# ------------------------------------ #


# open window
pr.init_window(800, 800, "ImmuneSimulation")
pr.set_target_fps(60)


# game loop
while not pr.window_should_close():
    # update frame counter
    frame_counter += 1

    # ------------- create cells ----------------- #
    my_creator.createBacteria((int(screen_width / 2), int(screen_height / 2)))
    
    # create macrophage every 30 frames
    if not frame_counter % 50:
        my_creator.createMacrophage()
    # -------------------------------------------- #


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

    # draw all cytokines
    for cyto in cells["cytokines"]:
        cyto.draw()
    # ----------------------------------------- #

    # ----------- update positions ------------ #
    # update bacteria
    for bac in cells["bacteria"]:
        update_factor_x = random.randint(-5,5)
        update_factor_y = random.randint(-5,5)
        bac.updatePosition(update_factor_x, update_factor_y)

    # update macrophages
    for macro in cells["macrophages"]:
        update_factor_x = random.randint(-5,5)
        update_factor_y = random.randint(-5,5)

        # check for cytokines
        # if cells["cytokines"]:
        #     for cyto in cells["cytokines"]:
        #         if macro.encounterCytokine(cyto):
        #             macro.updatePosition(update_factor_x, update_factor_y, cyto)
        # else:
        macro.updatePosition(update_factor_x, update_factor_y)
    
    # update cytokines
    for cyto in cells["cytokines"]:
        cyto.updatePosition()
    # ----------------------------------------- #

    # ------------ check for kills ---------- #
    my_tracker.killBacteria(cells["bacteria"], cells["macrophages"])

    # check if any macrophages have killed too many bacteria
    my_tracker.killMacrophages(cells["macrophages"])

    # check if cytokines are at the border
    my_tracker.killCytokines(cells["cytokines"])
    # --------------------------------------- #

pr.close_window()


