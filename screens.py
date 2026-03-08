from dataclasses import dataclass
import pygame_functions as pf
import plane

class Screen: # Represents a screen of the program (of which there are 3)

    def __init__(self,elements):

        self.elements = elements

    def activate_screen(self):
        for element in self.elements:
            pf.showSprite(element.sprite)
    
    def deactivate_screen(self):
        for element in self.elements:
            pf.hideSprite(element.sprite)

class FlightScreen(): # Represents the simulation flight screen

    def __init__(self,plane):
        self.plane_object = plane
        self.particles = []

    def activate_screen(self):
        pf.showSprite(self.plane_object)
        self.particles = []

    def deactivate_screen(self):
        
        pf.hideSprite(self.plane_object)
        for particle in self.particles:
            pf.hideSprite(particle.sprite)

class MenuScreen(Screen): # Represents the main menu

    def __init__(self,elements):

        super().__init__(elements)


class SettingScreen(Screen): # Represents the settings screen

    def __init__(self,elements):

        super().__init__(elements)


    

    