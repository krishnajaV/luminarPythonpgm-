class Swift:
    def start(self):
        print("swift car start")
    def accelerate(self):
        print("swift car accelerate")
    def breaks(self):
        print("swift car break")
    def stop(self):
        print("swift car stop")
class Selton:
    def start(self):
        print("selton car start")

    def accelerate(self):
        print("swift car accelerate")

    def breaks(self):
        print("selton car break")

    def stop(self):
        print("selton car stop")
class Person:
    def drive(self,car):
        car.start()
        car.accelerate()
        car.breaks()
        car.stop()
p=Person();
sw=Swift()
p.drive(sw)