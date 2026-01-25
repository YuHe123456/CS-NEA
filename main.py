from pygame_functions import *
from pathlib import Path
import time

base = Path(__file__).parent
sprite_path = base / "sprites"
plane_sprite = sprite_path / "plane_side_view.png"

screen = screenSize(1280,720,fullscreen=False)
setBackgroundColour("white")

hello_world_label = makeLabel("Hello world", 100, 100,100)


plane_visual = makeSprite(plane_sprite)
showSprite(plane_visual)
endWait()
while True:
    moveSprite(plane_visual,1,1)



