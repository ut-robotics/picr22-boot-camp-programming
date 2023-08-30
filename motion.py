from statistics import mean 

class IRobotMotion:
    def open(self):
        pass
    def close(self):
        pass
    def move(self, x_speed, y_speed, rot_speed):
        pass

class PrintingMotion(IRobotMotion):
    def open(self):
        print("Starting up!")

    def close(self):
        print("Shutting down...")

    # simple logic to print what the mainboard would recieve
    def move(self, x_speed, y_speed, rot_speed):
        print(f"Rotation speed: {rot_speed}; Side speed: {x_speed}; Forward speed: {y_speed}")
