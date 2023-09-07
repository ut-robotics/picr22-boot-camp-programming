from statistics import mean 

class IRobotMotion:
    def open(self):
        pass
    def close(self):
        pass
    def move(self, x_speed, y_speed, rot_speed):
        pass

class PrintingMotion(IRobotMotion):
    ## change polarity if direction is not correct
    def __init__(self, polarity=1):
        self.polarity = polarity
    
    def open(self):
        print("Starting up!")

    def close(self):
        print("Shutting down...")

    # simple logic to print what the mainboard would recieve
    def move(self, x_speed, y_speed, rot_speed):
        direction = "left" if rot_speed * self.polarity > 0 else "right"
        print(f"Rotation direction: {direction};")
