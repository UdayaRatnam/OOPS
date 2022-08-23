class Vehicle:
    def __init__(self,name , capacity = 0, mileage = 0, wheels = 0):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity
        self.wheels = wheels
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def setMileage(self, mile):
        self.mileage = mile
    def getMileage(self):
        return self.mileage
    def setCapacity(self,cap):
        self.capacity = cap
    def getCapacity(self):
        return self.capacity
    def setWheels(self, num):
        self.wheels = num
    def getWheels(self):
        return self.wheels
    def displayInfo(self):
        print("Vehicle Name: %s\nCapacity: %d\nMileage: %.2f mph\nWheels: %d\n"  % (self.name, self.capacity, self.mileage, self.wheels))
class Car(Vehicle):
    def __init__(self,name,capacity=0, mileage = 0, wheels = 0):
        super().__init__(name,mileage,capacity,wheels)
        super().setCapacity(5)
        super().setWheels(4)
    def displayInfo(self):
        print("Car Name: %s\nWheels: %d\nCapacity: %d\nMileage: %.2f mph\n" % (self.name,self.wheels,self.capacity,self.mileage))

class Bus(Vehicle):
    def __init__(self,name,capacity=0, mileage = 0, wheels = 0):
        super().__init__(name,mileage,capacity,wheels)
        super().setCapacity(55)
        super().setWheels(6)
    def displayInfo(self):
        print("Bus Name: %s\nWheels: %d\nCapacity: %d\nMileage: %.2f mph\n" % (self.name,self.wheels,self.capacity,self.mileage))
class Truck(Vehicle):
    def __init__(self,name,capacity=0, mileage = 0, wheels = 0):
        super().__init__(name,mileage,capacity,wheels)
        super().setCapacity(3)
        super().setWheels(18)
        self.cargo = 0
    def setCargo(self, weight):
        self.cargo = weight
    def getCargo(self):
        return self.cargo
    def displayInfo(self):
        print("Truck Name: %s\nWheels: %d\nCapacity: %d\nMileage: %.2f mph\nCargo: %.3f tons\n" % (self.name, self.wheels, self.capacity, self.mileage, self.cargo))