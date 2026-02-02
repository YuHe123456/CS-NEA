from pygame_functions import *
from pathlib import Path
from particle import Particle
from decimal import Decimal
import time

base = Path(__file__).parent
sprite_path = base / "sprites"
plane_sprite = sprite_path / "plane_side_view.png"
particle_sprite = sprite_path / "white_dot.png"

screen = screenSize(1280,720,fullscreen=False)
setBackgroundColour("darkblue")


plane_visual = makeSprite(plane_sprite)
showSprite(plane_visual)

air_particle = Particle((Decimal("600"),Decimal("300")), (Decimal("1000"),Decimal("-1000")), makeSprite(particle_sprite))
showSprite(air_particle.sprite)
transformSprite(air_particle.sprite,0,0.1)
timer = 0
angle = 0
while True:

    air_particle.move_particle(Decimal("0.01666666667"))
    print(timer)
    timer += 1
    moveSprite(plane_visual,640,360,centre=True)
    transformSprite(plane_visual,angle,1)
    angle += 1
    updateDisplay()
    tick(60)





