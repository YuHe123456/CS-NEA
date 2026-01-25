from decimal import Decimal, getcontext

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

num1 = Decimal("0.8")
num2 = Decimal("125")

# Calculate the dynamic pressure using air density and the airspeed

def calculate_dynamic_pressure(air_density,airspeed):

    dynamic_pressure = Decimal("0.5") * air_density * airspeed**2

    return dynamic_pressure

print(calculate_dynamic_pressure(num1,num2))
