from pygame_functions import *
from pathlib import Path
from particle import Particle, spawn_particle
from decimal import Decimal
from screens import * 
from plane import Plane, PlaneConstants, PlaneState
import file_functions as ff
import time

TIME_FRAME = Decimal("0.01666666667")

base = Path(__file__).parent
sprite_path = base / "sprites"
plane_sprite = sprite_path / "plane_side_view.png"
particle_sprite = sprite_path / "white_dot.png"
preset_path = base / "presets" / "presets.csv"

setAutoUpdate(False)

BUTTON_COLOUR = "white"

screen = screenSize(1280,720,fullscreen=False)

plane_sprite_obj = makeSprite(plane_sprite)
particle_sprite_obj = makeSprite(particle_sprite)

plane_state = PlaneState(
    position=(Decimal("0"), Decimal("0")),
    velocity=(Decimal("0"), Decimal("0")),
    acceleration=(Decimal("0"), Decimal("0")),
    direction=Decimal("0"),
    angle_of_attack=Decimal("0")
)

default_aircraft = "F-15"
plane_constants = ff.search_for_line(ff.load_file(preset_path), default_aircraft)

plane_object = Plane(constants=plane_constants, state=plane_state, sprite=plane_sprite_obj)


# Main Menu Buttons
start_button = makeLabel("Start",30,590,360,fontColour=BUTTON_COLOUR)
settings_button = makeLabel("Settings",30,570,420,fontColour=BUTTON_COLOUR)

# Settings Buttons
back_to_menu = makeLabel("Back to Menu",30,10,10,fontColour=BUTTON_COLOUR)

"""                name=output_list[0],
                lift_coefficient_gradient=output_list[1],
                lift_coefficient_intercept=output_list[2],
                drag_coefficient_gradient=output_list[3],
                drag_coefficient_intercept=output_list[4],
                wing_area=output_list[5],
                frontal_area=output_list[6],
                mass=output_list[7],
                thrust=output_list[8]
            )"""

BOX_X_START = 100
BOX_Y_START = 100

lift_coefficient_gradient_textbox = makeTextBox(BOX_X_START,BOX_Y_START,400,startingText="Lift Coefficient Gradient",maxLength=15)
lift_coefficient_intercept_textbox = makeTextBox(BOX_X_START,BOX_Y_START+50,400,startingText="Lift Coefficient Intercept",maxLength=15)
drag_coefficient_gradient_textbox = makeTextBox(BOX_X_START,BOX_Y_START+100,400,startingText="Drag Coefficient Gradient",maxLength=15)
drag_coefficient_intercept_textbox = makeTextBox(BOX_X_START,BOX_Y_START+150,400,startingText="Drag Coefficient Intercept",maxLength=15)
wing_area_textbox = makeTextBox(BOX_X_START,BOX_Y_START+200,400,startingText="Wing Area",maxLength=15)
frontal_area_textbox = makeTextBox(BOX_X_START,BOX_Y_START+250,400,startingText="Frontal Area",maxLength=15)
mass_textbox = makeTextBox(BOX_X_START,BOX_Y_START+300,400,startingText="Mass",maxLength=15)
thrust_textbox = makeTextBox(BOX_X_START,BOX_Y_START+350,400,startingText="Thrust",maxLength=15)


variable_boxes_elements_list = [lift_coefficient_gradient_textbox, lift_coefficient_intercept_textbox]
variable_boxes_elements_list.extend([drag_coefficient_gradient_textbox,drag_coefficient_intercept_textbox])
variable_boxes_elements_list.extend([wing_area_textbox,frontal_area_textbox,mass_textbox,thrust_textbox])

flight_screen = FlightScreen(plane_object,[back_to_menu])
settings_screen = SettingScreen([back_to_menu],variable_boxes_elements_list)
menu_screen = MenuScreen([start_button,settings_button])

activeScreen = "menu" # menu, settings or flight
menu_screen.activate_screen()

updateDisplay()

while True:

    match activeScreen:

        case "menu":

            if spriteClicked(settings_button):
                activeScreen = "settings"
                menu_screen.deactivate_screen()
                settings_screen.activate_screen()

            if spriteClicked(start_button):
                activeScreen = "flight"
                menu_screen.deactivate_screen()
                flight_screen.activate_screen()

        case "settings":

            if spriteClicked(back_to_menu):
                activeScreen = "menu"
                settings_screen.deactivate_screen()
                menu_screen.activate_screen()
                

        case "flight":

            if spriteClicked(back_to_menu):
                activeScreen = "menu"
                flight_screen.deactivate_screen()
                menu_screen.activate_screen()

        case _:
            pass

    updateDisplay()

    tick(60)





