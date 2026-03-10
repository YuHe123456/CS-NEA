from pygame_functions import *
from pathlib import Path
from particle import Particle, spawn_particle
from decimal import Decimal
from screens import * 
from plane import Plane, PlaneConstants, PlaneState
import file_functions as ff
import validation_functions as vf
import time

TIME_FRAME = Decimal("0.01666666667")
BUTTON_COLOUR = "white"
TITLE_COLOUR = "black"

base = Path(__file__).parent
sprite_path = base / "sprites"
plane_sprite = sprite_path / "plane_side_view.png"
particle_sprite = sprite_path / "white_dot.png"
preset_path = base / "presets" / "presets.csv"

setAutoUpdate(False)


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
title_label = makeLabel("Flight Simulation",60,400,200,fontColour=TITLE_COLOUR)

# Settings Buttons
back_to_menu = makeLabel("Back to Menu",30,10,10,fontColour=BUTTON_COLOUR)

BOX_X_START = 100
BOX_Y_START = 100

save_button = makeLabel("Save",22,BOX_X_START,BOX_Y_START+450,BUTTON_COLOUR)
load_button = makeLabel("Load",22,BOX_X_START+100,BOX_Y_START+450,BUTTON_COLOUR)

lift_coefficient_gradient_textbox = makeTextBox(BOX_X_START,BOX_Y_START,400,startingText="Lift Coefficient Gradient",maxLength=15)
lift_coefficient_intercept_textbox = makeTextBox(BOX_X_START,BOX_Y_START+50,400,startingText="Lift Coefficient Intercept",maxLength=15)
drag_coefficient_gradient_textbox = makeTextBox(BOX_X_START,BOX_Y_START+100,400,startingText="Drag Coefficient Gradient",maxLength=15)
drag_coefficient_intercept_textbox = makeTextBox(BOX_X_START,BOX_Y_START+150,400,startingText="Drag Coefficient Intercept",maxLength=15)
wing_area_textbox = makeTextBox(BOX_X_START,BOX_Y_START+200,400,startingText="Wing Area",maxLength=15)
frontal_area_textbox = makeTextBox(BOX_X_START,BOX_Y_START+250,400,startingText="Frontal Area",maxLength=15)
mass_textbox = makeTextBox(BOX_X_START,BOX_Y_START+300,400,startingText="Mass",maxLength=15)
thrust_textbox = makeTextBox(BOX_X_START,BOX_Y_START+350,400,startingText="Thrust",maxLength=15)
name_textbox = makeTextBox(BOX_X_START,BOX_Y_START+400,400,startingText="Name",maxLength=15)

temp_lift_coefficient_gradient = plane_constants.lift_coefficient_gradient
temp_lift_coefficient_intercept = plane_constants.lift_coefficient_intercept
temp_drag_coefficient_gradient = plane_constants.drag_coefficient_gradient
temp_drag_coefficient_intercept = plane_constants.drag_coefficient_intercept
temp_wing_area = plane_constants.wing_area
temp_frontal_area = plane_constants.frontal_area
temp_mass = plane_constants.mass
temp_thrust = plane_constants.thrust
temp_name = plane_constants.name


temp_lift_coefficient_gradient_label = makeLabel(str(temp_lift_coefficient_gradient),22,BOX_X_START + 410, BOX_Y_START+5, fontColour=BUTTON_COLOUR)
temp_lift_coefficient_intercept_label = makeLabel(str(temp_lift_coefficient_intercept),22,BOX_X_START + 410, BOX_Y_START+55, fontColour=BUTTON_COLOUR)
temp_drag_coefficient_gradient_label = makeLabel(str(temp_drag_coefficient_gradient),22,BOX_X_START + 410, BOX_Y_START+105, fontColour=BUTTON_COLOUR)
temp_drag_coefficient_intercept_label = makeLabel(str(temp_drag_coefficient_intercept),22,BOX_X_START + 410, BOX_Y_START+155, fontColour=BUTTON_COLOUR)
temp_wing_area_label = makeLabel(str(temp_wing_area),22,BOX_X_START + 410, BOX_Y_START+205, fontColour=BUTTON_COLOUR)
temp_frontal_area_label = makeLabel(str(temp_frontal_area),22,BOX_X_START + 410, BOX_Y_START+255, fontColour=BUTTON_COLOUR)
temp_mass_label = makeLabel(str(temp_mass),22,BOX_X_START + 410, BOX_Y_START+305, fontColour=BUTTON_COLOUR)
temp_thrust_label = makeLabel(str(temp_thrust),22,BOX_X_START + 410, BOX_Y_START+355, fontColour=BUTTON_COLOUR)
temp_name_label = makeLabel(temp_name,22,BOX_X_START + 410, BOX_Y_START+405, fontColour=BUTTON_COLOUR)

variable_boxes_elements_list = [lift_coefficient_gradient_textbox, lift_coefficient_intercept_textbox,
                                drag_coefficient_gradient_textbox,drag_coefficient_intercept_textbox,
                                wing_area_textbox,frontal_area_textbox,mass_textbox,thrust_textbox, 
                                name_textbox]

variable_boxes_label_list = [temp_lift_coefficient_gradient_label,temp_lift_coefficient_intercept_label, 
                             temp_drag_coefficient_gradient_label,temp_drag_coefficient_intercept_label,
                             temp_wing_area_label,temp_frontal_area_label,temp_mass_label,
                             temp_thrust_label,temp_name_label, save_button, load_button]

flight_screen = FlightScreen(plane_object,[back_to_menu])
settings_screen = SettingScreen([back_to_menu],variable_boxes_elements_list, variable_boxes_label_list)
menu_screen = MenuScreen([start_button,settings_button,title_label])

activeScreen = "menu" # menu, settings or flight
menu_screen.activate_screen()

updateDisplay()

while True:

    match activeScreen:

        case "menu":

            if spriteClicked(settings_button): # Switch to settings 
                activeScreen = "settings"
                menu_screen.deactivate_screen()
                settings_screen.activate_screen()

            if spriteClicked(start_button): # Switch to flight screen 
                activeScreen = "flight"
                menu_screen.deactivate_screen()
                flight_screen.activate_screen()

        case "settings":

            if spriteClicked(back_to_menu): # Back to menu, for both settings and flight
                activeScreen = "menu"
                settings_screen.deactivate_screen()
                menu_screen.activate_screen()

            if spriteClicked(lift_coefficient_gradient_textbox): # Takes and validates user input
                user_input = vf.validate_coefficient(textBoxInput(lift_coefficient_gradient_textbox))

                if user_input != False:
                    temp_lift_coefficient_gradient = user_input
                    changeLabel(temp_lift_coefficient_gradient_label, str(user_input))


            if spriteClicked(lift_coefficient_intercept_textbox):
                user_input = vf.validate_intercept(textBoxInput(lift_coefficient_intercept_textbox))

                if user_input != False:
                    temp_lift_coefficient_intercept = user_input
                    changeLabel(temp_lift_coefficient_intercept_label, str(user_input))


            if spriteClicked(drag_coefficient_gradient_textbox):
                user_input = vf.validate_coefficient(textBoxInput(drag_coefficient_gradient_textbox))

                if user_input != False:
                    temp_drag_coefficient_gradient = user_input
                    changeLabel(temp_drag_coefficient_gradient_label, str(user_input))


            if spriteClicked(drag_coefficient_intercept_textbox):
                user_input = vf.validate_intercept(textBoxInput(drag_coefficient_intercept_textbox))

                if user_input != False:
                    temp_drag_coefficient_intercept = user_input
                    changeLabel(temp_drag_coefficient_intercept_label, str(user_input))


            if spriteClicked(wing_area_textbox):
                user_input = vf.validate_scalar(textBoxInput(wing_area_textbox))

                if user_input != False:
                    temp_wing_area = user_input
                    changeLabel(temp_wing_area_label, str(user_input))


            if spriteClicked(frontal_area_textbox):
                user_input = vf.validate_scalar(textBoxInput(frontal_area_textbox))

                if user_input != False:
                    temp_frontal_area = user_input
                    changeLabel(temp_frontal_area_label, str(user_input))


            if spriteClicked(mass_textbox):
                user_input = vf.validate_scalar(textBoxInput(mass_textbox))

                if user_input != False:
                    temp_mass = user_input
                    changeLabel(temp_mass_label, str(user_input))


            if spriteClicked(thrust_textbox):
                user_input = vf.validate_scalar(textBoxInput(thrust_textbox))

                if user_input != False:
                    temp_thrust = user_input
                    changeLabel(temp_thrust_label, str(user_input))

            if spriteClicked(name_textbox):
                user_input = vf.validate_name(textBoxInput(name_textbox))

                if user_input != False:
                    temp_name = user_input
                    changeLabel(temp_name_label, str(user_input))

            if spriteClicked(save_button):
                
                ff.add_line(preset_path,[temp_name,temp_lift_coefficient_gradient,temp_lift_coefficient_intercept,
                                         temp_drag_coefficient_gradient,temp_drag_coefficient_intercept,
                                         temp_wing_area,temp_frontal_area,temp_mass,temp_thrust])
                plane_object.constants = ff.search_for_line(ff.load_file(preset_path), temp_name)

                print(plane_constants.mass)


        case "flight":

            if spriteClicked(back_to_menu):
                activeScreen = "menu"
                flight_screen.deactivate_screen()
                menu_screen.activate_screen()

        case _:
            pass

    updateDisplay()

    tick(60)





