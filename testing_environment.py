# SUBPROGRAM CODE HERE
import math

class Engine:
    def __init__(self):
        pass
  
    def update_plane(self, target, x_y_tuple):

        x,y = x_y_tuple

        target.set_acc(x,y)




class Object:

    def __init__(self,mass):

        self.x_pos = 0
        self.y_pos = 0

        self.x_vel = 0
        self.y_vel = 0

        self.x_acc = 0
        self.y_acc = 0

        self.mass = mass

    def set_pos(self, x_pos, y_pos):

        if isinstance(x_pos, (int, float)) and isinstance(y_pos, (int, float)):

            self.x_pos = x_pos 
            self.y_pos = y_pos

        else:
            raise ValueError("Update_pos failed: wrong type input")
    
    def set_vel(self, x_vel, y_vel):

        if isinstance(x_vel, (int, float)) and isinstance(y_vel, (int, float)):

            self.x_vel = x_vel 
            self.y_vel = y_vel 

        else:
            raise ValueError("Update_vel failed: wrong type input")
        
    def set_acc(self, x_acc, y_acc):

        if isinstance(x_acc, (int, float)) and isinstance(y_acc, (int, float)):

            self.x_acc = x_acc 
            self.y_acc = y_acc

        else:
            raise ValueError("Update_vel failed: wrong type input")

    def print_properties(self):
        print(f"X pos: {self.x_pos}     Y pos: {self.y_pos}")
        print(f"X vel: {self.x_vel}     Y vel: {self.y_vel}")
        print(f"X acc: {self.x_acc}     Y acc: {self.y_acc}")


engine = Engine()

my_object = Object(1)

test_data = [
    (5,5),
    (-5,-5),
    ("Fail","Fail")
]

for test in test_data:
    engine.update_plane(my_object, test)
    my_object.print_properties() 

