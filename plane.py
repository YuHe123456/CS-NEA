from dataclasses import dataclass
from decimal import Decimal

import math_functions as mf 
import validation_functions as vf
import file_functions as ff
import pygame_functions as pf

@dataclass(frozen=True)
class PlaneConstants:
       
    name: str

    # Lift and drag coefficient model

    lift_coefficient_gradient: Decimal 
    lift_coefficient_intercept: Decimal
    drag_coefficient_gradient: Decimal
    drag_coefficient_intercept: Decimal

    # Constant properties
    
    wing_area: Decimal
    frontal_area: Decimal
    mass: Decimal
    thrust: Decimal

@dataclass
class PlaneState:

    position: tuple[Decimal, Decimal]
    velocity: tuple[Decimal, Decimal]
    acceleration: tuple[Decimal, Decimal]
    direction: Decimal
    angle_of_attack: Decimal


@dataclass
class Plane:

    constants: PlaneConstants
    state: PlaneState
    sprite: pf.newSprite

    
    def __post_init__(self):
        
        pf.moveSprite(self.sprite,640,360,centre=True)


    def replace_constants(self, new_config: PlaneConstants) -> None:
        self.constants = new_config  # Replaces the constant config with a new one

    # A combined subprogram that runs every operation every tick

    def print_state(self) -> None:

        print(f"""
            Position: {self.state.position}
            Velocity: {self.state.velocity}
            Acceleration: {self.state.acceleration}
            Angle of Attack: {self.state.angle_of_attack}
            Direction: {self.state.direction}
            """)

    def sim_tick(self,time_frame):
        
        # Conditions calculation

        air_pressure = mf.calculate_air_pressure(self.state.position[1])
        temperature = mf.calculate_temperature(self.state.position[1])
        air_density = mf.calculate_air_density(air_pressure, temperature)

        airspeed = mf.calculate_air_speed(self.state.velocity)
        dynamic_pressure = mf.calculate_dynamic_pressure(air_density, airspeed)
        self.state.angle_of_attack = mf.calculate_angle_of_attack(self.state.velocity,self.state.direction)
        drag_coefficient = mf.calculate_coefficient(self.constants.drag_coefficient_gradient, self.constants.drag_coefficient_intercept, self.state.angle_of_attack)
        lift_coefficient = mf.calculate_coefficient(self.constants.lift_coefficient_gradient, self.constants.lift_coefficient_gradient, self.state.angle_of_attack)
        
        # Force calculation

        drag_vector = mf.calculate_drag_vector(dynamic_pressure, drag_coefficient, self.constants.frontal_area, self.state.direction, self.state.angle_of_attack)
        lift_vector = mf.calculate_lift_vector(dynamic_pressure, lift_coefficient, self.constants.wing_area, self.state.direction, self.state.angle_of_attack)
        weight_vector = mf.calculate_weight_vector(self.constants.mass)
        thrust_vector = mf.calculate_thrust_vector(self.constants.thrust, self.state.direction)

        forces = mf.sum_force_vectors([drag_vector,lift_vector,weight_vector,thrust_vector])

        self.state.acceleration = mf.calculate_acceleration(forces, self.constants.mass)

        # Velocity calculation

        self.state.velocity = mf.calculate_velocity(self.state.velocity, self.state.acceleration, time_frame)

        # Position calculation

        self.state.position = mf.calculate_position(self.state.position, self.state.velocity, time_frame)

