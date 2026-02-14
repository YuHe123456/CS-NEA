from pygame_functions import *
from pathlib import Path
from particle import Particle, spawn_particle
from decimal import Decimal
import time

base = Path(__file__).parent
sprite_path = base / "sprites"
plane_sprite = sprite_path / "plane_side_view.png"
particle_sprite = sprite_path / "white_dot.png"

setAutoUpdate(False)
TIME_FRAME = Decimal("0.01666666667")

screen = screenSize(1280,720,fullscreen=False)
setBackgroundColour("darkblue")


plane_visual = makeSprite(plane_sprite)


showSprite(plane_visual)
moveSprite(plane_visual,640,360,centre=True)

angle = 0
direction = 0

plane_velocity = [Decimal("0"),Decimal("0")]

particle_list = []

acceleration = [Decimal("100"), Decimal("10")]

while True:

    particle_list.append(spawn_particle(plane_velocity,makeSprite(particle_sprite)))

    for particle in particle_list:
        particle.move_particle(TIME_FRAME)
        particle.accelerate_particle(acceleration,TIME_FRAME)

    if keyPressed("right") and direction < 8:
        direction += 1
        transformSprite(plane_visual,direction,1)

    if keyPressed("left") and direction > -8:
        direction -= 1
        transformSprite(plane_visual,direction,1)  
    
    plane_velocity[0] = plane_velocity[0] + acceleration[0]*TIME_FRAME
    plane_velocity[1] = plane_velocity[1] + acceleration[1]*TIME_FRAME
    
    updateDisplay()
    tick(60)





