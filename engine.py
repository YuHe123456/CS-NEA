import time

class Engine:
    def __init__(self):
        pass
  
    def apply_force(target, x_force, y_force):
        
        object_mass = target.mass

        x_acc = x_force / object_mass
        y_acc = y_force / object_mass

        

class Object:
    def __init__(self,mass):

        self.x_pos = 0
        self.y_pos = 0

        self.x_vel = 0
        self.y_vel = 0

        self.x_acc = 0
        self.y_acc = 0

        self.mass = mass

    def update_pos(self, x_pos, y_pos):

        if isinstance(x_pos, (int, float)) and isinstance(y_pos, (int, float)):

            self.x_pos += x_pos 
            self.y_pos += y_pos

        else:
            raise ValueError("Update_pos failed: wrong type input")


    def update_vel(self, x_vel, y_vel):

        if isinstance(x_vel, (int, float)) and isinstance(y_vel, (int, float)):
            self.x_vel += x_vel 
            self.y_vel += y_vel 


    def update_acc(self, x_acc, y_acc):
        self.x_acc = x_acc
        self.y_acc = y_acc



    def update(self, dt):

        self.x_vel += self.x_acc * dt
        self.y_vel += self.y_acc * dt

        self.x_pos += self.x_vel * dt
        self.y_pos += self.y_vel * dt

        

    def print_pos(self):

        print("X: ", self.x_pos)
        print("Y: ", self.y_pos)

        print()
    
    def print_vel(self):

        print("X_vel", self.x_vel)
        print("Y_vel", self.y_vel)
    

my_object = Object(2)

my_object.print_pos()



