from dataclasses import dataclass  
from decimal import Decimal
from math_functions import calculate_position
import pygame_functions

@dataclass
class Particle:
    position: tuple[Decimal,Decimal]
    velocity: tuple[Decimal,Decimal]
    sprite: pygame_functions.newSprite

    # Progress a particle to its next tick
    def move_particle(self, time_frame): # Progresses a particle one tick
        self.position = calculate_position(self.position, self.velocity, time_frame) # Calculate position
        pygame_functions.moveSprite(self.sprite, self.position[0], self.position[1], centre=True)
        # Execute movement on visual

