from math import * 
import time

# constants

#0.1066666,0.002625,2,0.034,56.5,7,18143.695,26500

boltzmann_constant = 1.38*(10**-23)
gravity = 9.81
air_mass = 4.8*(10**-26)
sea_level_pressure = 1013.25 * (10**2)
sea_level_temperature = 15
time_frame = 1
air_mass = 4.8 * 10**-26 

flight_active = False

#lift_coefficient_gradient, drag_coefficient_gradient, lift_coefficient_intercept, 
#drag_coefficient_intercept, wing_area, frontal_area, mass,thrust

class Aircraft:
  def __init__(self, preset):
    
    self.x_pos = 0
    self.y_pos = 0
    
    self.x_velocity = 0
    self.y_velocity = 0
    
    self.x_acceleration = 0
    self.y_acceleration = 0 
    
    self.x_force = 0
    self.y_force = 0
    
    self.direction = 0
    self.angle_of_attack = 0
    
    self.wing_area = preset[4]
    self.frontal_area = preset[5]
    
    print(self.frontal_area)
    
    self.mass = preset[6]
    self.weight = self.mass*9.81
    self.lift_coefficient_gradient = preset[0]
    self.drag_coefficient_gradient = preset[1]
    
    self.lift_coefficient_intercept = preset[2]
    self.drag_coefficient_intercept = preset[3]
    
    
    self.time_frame = time_frame
    
    self.thrust = preset[7]
    
  def main_loop(self):
    
    
    
    while flight_active:
    
      # Conditions Calculation
    
      dynamic_pressure = self.calculate_dynamic_pressure()
      
      # Force Calculation
      
      
      self.calculate_resultant_forces(dynamic_pressure)
      
      
      # Acceleration Calculation
      
      self.calculate_acceleration()
      
      # Velocity Calculation
      
      self.calculate_velocity()
      
      # Position Calculation
      
      self.calculate_position()
      print(self.x_pos,self.y_pos)
      
      time.sleep(1)
    
  def calculate_dynamic_pressure(self): # used
    
    dynamic_pressure = 0.5 * self.calculate_air_density() * (self.x_velocity**2 + self.y_velocity**2)
    return dynamic_pressure
  
  def calculate_acceleration(self): 
    
    
    self.x_acceleration = self.x_force/self.mass
    self.y_acceleration = self.y_force/self.mass
  
  def calculate_velocity(self):
    
    self.x_velocity = self.x_velocity + self.x_acceleration * self.time_frame
    self.y_velocity = self.y_velocity + self.y_acceleration * self.time_frame
  
  
  def calculate_position(self):
    
    self.x_pos = self.x_pos + self.x_velocity * self.time_frame
    self.y_pos = self.y_pos + self.y_velocity * self.time_frame

  def calculate_resultant_forces(self, dynamic_pressure):
    
    dynamic_pressure = self.calculate_dynamic_pressure()
    
    drag = self.calculate_drag_force(dynamic_pressure)
    lift = self.calculate_lift_force(dynamic_pressure)
    
    thrust = self.thrust 
    direction = radians(self.direction)
    aoa_radians = radians(self.angle_of_attack)
    
    self.x_force = (thrust * cos(self.direction))- (drag * cos(direction+aoa_radians)) - (lift * sin(self.direction))
    
    self.y_force = (lift * cos(direction)) + (thrust * sin(direction)) - (drag * sin(direction + aoa_radians))

  
  def calculate_lift_force(self, dynamic_pressure):
    
    lift_force = dynamic_pressure * self.wing_area * self.calculate_lift_coefficient()
    
    return lift_force
    

  def calculate_drag_force(self, dynamic_pressure):
    
    drag_force = dynamic_pressure * self.frontal_area * self.calculate_drag_coefficient()

    return drag_force 


  def calculate_air_pressure(self): # used 
    
    power = -(air_mass * gravity * self.y_pos)/(boltzmann_constant*self.calculate_temperature())
    
    air_pressure = sea_level_pressure * exp(power)
    
    print("air_pressure",air_pressure)
    
    return air_pressure

  def calculate_air_density(self):
    air_density = self.calculate_air_pressure() * (self.calculate_temperature() * 287)
    
    return air_density

  def calculate_temperature(self): # used 
    temperature = sea_level_temperature - (self.y_pos/1000 * 6.5) + 273.15
    return temperature


  def calculate_lift_coefficient(self): # used 
    lift_coefficient = (self.lift_coefficient_gradient * self.angle_of_attack) + self.lift_coefficient_intercept 
    print(lift_coefficient)
    return lift_coefficient
  
    
  def calculate_drag_coefficient(self): # used 
    drag_coefficient = (self.drag_coefficient_gradient * self.angle_of_attack) + self.drag_coefficient_intercept 
    
    return drag_coefficient
    
  def calculate_angle_of_attack(self):
    
    direction_of_movement = degrees(atan( (self.y_velocity)/(self.x_velocity) ))
    
    self.angle_of_attack = self.direction - direction_of_movement


def unpack_csv(index):
  f = open("presets.csv","r")
  presets = f.readlines() # list of presets
  presets = presets[index].strip().split(",")
  presets = [float(i) for i in presets]
  return presets

plane = Aircraft(unpack_csv(0))

flight_active = False

plane.main_loop()
