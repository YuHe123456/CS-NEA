from dataclasses import dataclass
import pygame_functions as pf
import plane

MENU_BACKGROUND_COLOUR = "grey"
FLIGHT_BACKGROUND_COLOUR = "darkblue"
class Screen: # Represents a screen of the program (of which there are 3)

    def __init__(self,elements):

        self.elements = elements

    def activate_screen(self):

        pf.setBackgroundColour(MENU_BACKGROUND_COLOUR)
        print("background coloour set screen")
        for element in self.elements:
            pf.showLabel(element)
    
    def deactivate_screen(self):
        for element in self.elements:
            pf.hideLabel(element)

class FlightScreen: # Represents the simulation flight screen

    def __init__(self,plane,elements):
        self.plane_object = plane
        self.elements = elements
        self.particles = []

    def activate_screen(self):

        pf.setBackgroundColour(FLIGHT_BACKGROUND_COLOUR)

        for element in self.elements:
            pf.showLabel(element)

        pf.showSprite(self.plane_object.sprite)
        self.particles = []

    def deactivate_screen(self):
        
        for element in self.elements:
            pf.hideLabel(element)

        pf.hideSprite(self.plane_object.sprite)
        for particle in self.particles:
            pf.hideSprite(particle.sprite)

class MenuScreen(Screen): # Represents the main menu

    def __init__(self,elements):

        super().__init__(elements)


class SettingScreen(Screen): # Represents the settings screen

    def __init__(self,elements,variable_boxes):

        super().__init__(elements)
        self.variable_boxes = variable_boxes
    
    def activate_screen(self):
        super().activate_screen()
        for box in self.variable_boxes:
            pf.showTextBox(box)
    
    def deactivate_screen(self):
        super().deactivate_screen()
        for box in self.variable_boxes:
            pf.hideTextBox(box)


    

    