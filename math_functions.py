from decimal import Decimal, getcontext
from math import sin, cos, radians, atan, degrees, pi

g = Decimal("9.81")

# Contains all of the simulation calculations of the program. 

# Calculates the next position of the aircraft given a velocity and a time elapsed variable.

def calculate_position(current_pos, velocity, time_frame):

    # Organise arg tuples into individual variables for readability

    x_vel,y_vel = velocity      # Velocity vector of plane object
    x_pos,y_pos = current_pos   # Position vector of plane object

    # Add the velocity * time passed to position (distance travelled = speed * time)

    x_pos += x_vel * time_frame  # Time frame determines how much in-sim time has passed
    y_pos += y_vel * time_frame

    return (x_pos,y_pos)

# Calculates the veloity of the aircraft on the next tick, given acceleration and time elapsed.

def calculate_velocity(current_vel, acceleration, time_frame):

    # Organise arg tuples into individual variables for readability

    x_acc,y_acc = acceleration # Acceleration vector
    x_vel,y_vel = current_vel  # Velocity vector

    x_vel += x_acc * time_frame
    y_vel += y_acc * time_frame

    return (x_vel,y_vel)


# Calculates the acceleration of the aircraft, given a specific force and the mass of the aircraft.

def calculate_acceleration(force, mass):

    x_force,y_force = force # Decompose force (tuple) into its components.

    x_acc = x_force / mass # Acceleration is directly set to the force / mass, not added.
    y_acc = y_force / mass 

    return (x_acc, y_acc)

# Calculates the temperature at a given altitude

def calculate_temperature(altitude):

    SEA_LEVEL_TEMPERATURE = Decimal("288.15") # Temperature at sea level in Kelvin (K)
    LAPSE_RATE = Decimal("0.0065") # Decrease in K per meter

    temperature = SEA_LEVEL_TEMPERATURE - (altitude*LAPSE_RATE)

    return temperature

# Calculates the air pressure using the temperature, altitude and several constants

def calculate_air_pressure(altitude):

    sea_level_pressure = Decimal("101325") # measured in Pascals (Newtons / meter)
    lapse_rate = Decimal("0.0065")
    molar_gas_constant = Decimal("8.31446") 
    gravitational_acceleration = Decimal("9.81") # Measured in meters per second squared.
    sea_level_temperature = Decimal("288.15")
    molar_mass_air = Decimal("0.0289652")

    bracket = (1 - (lapse_rate * altitude / sea_level_temperature))
    exponent = gravitational_acceleration * molar_mass_air / (molar_gas_constant * lapse_rate)

    air_pressure = sea_level_pressure * bracket**exponent

    return air_pressure

# Calculates the air density using the air pressure and temperature. 

def calculate_air_density(air_pressure, temperature):

    specific_gas_constant = Decimal("287.05")

    air_density = air_pressure / (specific_gas_constant * temperature)

    return air_density

# Calculates the magnitude of speed of an aircraft

def calculate_air_speed(velocity):

    x_vel,y_vel = velocity

    airspeed_squared = x_vel**2 + y_vel**2 # Follows Pythagoras: a^2 + b^2 = c^2

    return airspeed_squared**Decimal("0.5") # Roots the c^2


# Calculate the dynamic pressure using air density and the airspeed

def calculate_dynamic_pressure(air_density,airspeed):

    dynamic_pressure = Decimal("0.5") * air_density * airspeed**2

    return dynamic_pressure

# Calculates the drag vector given a set of variables 

def calculate_drag_vector(dynamic_pressure, drag_coefficient, frontal_area, direction, angle_of_attack) -> tuple:

    drag_magnitude = dynamic_pressure * drag_coefficient * frontal_area
    drag_direction = direction + Decimal(degrees(angle_of_attack)) - 180 # Drag acts opposite to movement direction

    return (drag_magnitude,drag_direction)

# Calculates the lift vector given a similar variable set

def calculate_lift_vector(dynamic_pressure, lift_coefficient, wing_area, direction, angle_of_attack) -> tuple:

    lift_magnitude = dynamic_pressure * lift_coefficient * wing_area
    lift_direction = direction + Decimal(degrees(angle_of_attack)) + 90

    return (lift_magnitude,lift_direction)

# Calculates the coefficient given an intercept and gradient linear model

def calculate_coefficient(gradient,intercept,angle_of_attack) -> Decimal:

    coefficient = intercept + (gradient * angle_of_attack)

    return coefficient

# Calculate weight vector given a mass 

def calculate_weight_vector(mass):

    return (mass * g, -90)

# Calculate the thrust vector 

def calculate_thrust_vector(thrust, direction):
    return (thrust, direction)

# Sums a set of force vectors consisting of magnitude and direction 

def sum_force_vectors(force_vectors) -> tuple:

    x_force = 0
    y_force = 0
    
    for force_vector in force_vectors:

        magnitude,direction = force_vector[0],radians(force_vector[1])

        x_force += magnitude * Decimal(cos(direction))  # Sums forces and adds their components to x and y
        y_force += magnitude * Decimal(sin(direction))
    
    return (Decimal(x_force), Decimal(y_force))

# Calculate the angle of attack

def calculate_angle_of_attack(velocity,direction):
    
    gradient = (0 if velocity[0] == 0 else velocity[1]/velocity[0])

    angle_of_attack = Decimal(atan(gradient)) - Decimal(radians(direction))

    return angle_of_attack

if __name__ == "__main__":

    forces_list = [
        (10, 0), (10, 120), (10, 240)
    ]
    
    print(sum_force_vectors(forces_list))
