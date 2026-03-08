from dataclasses import dataclass  
from decimal import Decimal
from math_functions import calculate_position
import pygame_functions
import random 

SCALE = 0.01
MAX_VARIATION = 110
MIN_VARIATION = 90
X_RESOLUTION = 1280
Y_RESOLUTION = 720

@dataclass
class Particle:
    position: tuple[Decimal,Decimal]
    velocity: tuple[Decimal,Decimal]
    sprite: pygame_functions.newSprite

    def __post_init__(self):
        pygame_functions.transformSprite(self.sprite,0,SCALE)
        pygame_functions.moveSprite(self.sprite,self.position[0],self.position[1],centre=True)
        pygame_functions.showSprite(self.sprite)

    # Progress a particle to its next tick
    def move_particle(self, time_frame): # Progresses a particle one tick
        self.position = calculate_position(self.position, self.velocity, time_frame) # Calculate position
        pygame_functions.moveSprite(self.sprite, self.position[0], self.position[1], centre=True)
        # Execute movement on visual

        if self.position[0] < 0:
            pygame_functions.killSprite(self.sprite)

    def translate_particle(self,units):
        self.position = (self.position[0] + units, self.position[1])
        pygame_functions.moveSprite(self.sprite,self.position[0],self.position[1], centre=True)

    # Change the particle's velocity based on plane acceleration

    def accelerate_particle(self, plane_acceleration, time_frame):

        particle_acceleration = [-plane_acceleration[0],plane_acceleration[1]] # Inverts the plane acceleration 
        
        self.velocity[0] += (particle_acceleration[0]*time_frame)
        self.velocity[1] += (particle_acceleration[1]*time_frame)
        



# Spawn a single air particle

def spawn_particle(plane_velocity,sprite) -> Particle:

    x_velocity = (Decimal(random.randint(MIN_VARIATION,MAX_VARIATION))/Decimal("100")) * -plane_velocity[0]
    y_velocity = (Decimal(random.randint(MIN_VARIATION,MAX_VARIATION))/Decimal("100")) * plane_velocity[1]

    particle_velocity = [x_velocity, y_velocity]
    # Reverse particle movement direction

    position = [X_RESOLUTION, random.randint(-Y_RESOLUTION,2*Y_RESOLUTION)] # Spawn a resolution above or below
    new_particle = Particle(position,particle_velocity,sprite)

    return new_particle

