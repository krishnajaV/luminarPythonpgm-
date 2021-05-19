# Create a child class Bus that will inherit all of the variables and methods of Vehicle class ?
class Vehicle:
    def __init__(self, name, speed):
        self.name=name
        self.speed=speed
        print("name=",self.name)
        print("speed=",self.speed)
class Bus(Vehicle):
    def __init__(self,seat,type,name,speed):
        super().__init__(name,speed)
        self.seat = seat
        self.type = type
        print("name=", self.name)
        print("speed=", self.speed)
ob=Bus('44seat','tourist','srs','125m/s',)
