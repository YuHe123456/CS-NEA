from pygame_functions import *
from pathlib import Path
import time

base = Path(__file__).parent
sprite_path = base / "sprites"
plane_sprite = "plane_side_view.png"

screen = screenSize(1280,720,fullscreen=False)
setBackgroundColour("white")

hello_world_label = makeLabel("Hello world", 300, 300,100)


plane_visual = makeSprite(plane_sprite)
showSprite(plane_visual)
while True:
    moveSprite(plane_visual,300,300)
    tick(60)





