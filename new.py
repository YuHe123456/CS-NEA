from decimal import Decimal, getcontext

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


num1 = Decimal("132.324")
num2 = Decimal("384.239084")
num3 = Decimal("32.3294")

# Calculates the acceleration of the aircraft, given a specific force and the mass of the aircraft.

def calculate_acceleration(force, mass):

    x_force,y_force = force # Decompose force (tuple) into its components.

    x_acc = x_force / mass # Acceleration is directly set to the force / mass, not added.
    y_acc = y_force / mass 

    return (x_acc, y_acc)

print(calculate_acceleration((num1,num2),num3))