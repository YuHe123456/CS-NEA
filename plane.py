from dataclasses import dataclass
from decimal import Decimal

import math_functions
import validation_functions
import file_functions

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

    def replace_constants(self, new_config: PlaneConstants) -> None:
        self.constants = new_config  # Replaces the constant config with a new one