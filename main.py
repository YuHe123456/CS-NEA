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
    name="F-15",
    sprite=plane_sprite_obj,
    lift_coefficient_gradient=Decimal("0.1066666"),
    lift_coefficient_intercept=Decimal("0.002625"),
    drag_coefficient_gradient=Decimal("2"),
    drag_coefficient_intercept=Decimal("0.034"),
    wing_area=Decimal("56.5"),
    frontal_area=Decimal("20"),
    mass=Decimal("14000"),
    thrust=Decimal("210000")
)
plane_object = Plane(constants=plane_constants, state=plane_state, sprite=plane_sprite)

flight_screen = FlightScreen(plane=plane_object)

plane_visual = makeSprite(plane_sprite)
moveSprite(plane_visual,640,360,centre=True)

angle = 0
direction = 0

particle_list = []

while True:

    # Append particle with plane velocity and particle sprite new object
    # Move particles

    # Tilt left and right
    
    
    
    updateDisplay()
    tick(60)





