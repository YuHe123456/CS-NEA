from pygame_functions import *
from pathlib import Path
from particle import Particle, spawn_particle
from decimal import Decimal
from screens import * 
from plane import Plane, PlaneConstants, PlaneState
import time

TIME_FRAME = Decimal("0.01666666667")

base = Path(__file__).parent
sprite_path = base / "sprites"
plane_sprite = sprite_path / "plane_side_view.png"
particle_sprite = sprite_path / "white_dot.png"

setAutoUpdate(False)

screen = screenSize(1280,720,fullscreen=False)
setBackgroundColour("darkblue")


plane_sprite_obj = makeSprite(plane_sprite)

plane_state = PlaneState(
    position=(Decimal("0"), Decimal("0")),
    velocity=(Decimal("0"), Decimal("0")),
    acceleration=(Decimal("0"), Decimal("0")),
    direction=Decimal("0"),
    angle_of_attack=Decimal("0")
)

plane_constants = PlaneConstants(
    name="Placeholder",
    lift_coefficient_gradient="Placeholder",
    lift_coefficient_intercept="Placeholder",
    drag_coefficient_gradient="Placeholder",
    drag_coefficient_intercept="Placeholder",
    wing_area="Placeholder",
    frontal_area="Placeholder",
    mass="Placeholder",
    thrust="Placeholder"
)
plane_object = Plane(constants=plane_constants, state=plane_state, sprite=plane_sprite)

flight_screen = FlightScreen(plane=plane_object)

plane_visual = makeSprite(plane_sprite)


showSprite(plane_visual)
moveSprite(plane_visual,640,360,centre=True)

angle = 0
direction = 0

particle_list = []

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





