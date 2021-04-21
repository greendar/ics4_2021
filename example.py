class Vehicle:
    def __init__(self, driver, colour, wheels):
        self.driver = driver
        self.wheels = wheels
        self.colour = colour
        self.name = 'vehicle'
        self.horn = 'honk'

    def __str__(self):
        return f"{self.driver} is driving the {self.colour} {self.wheels} wheeled {self.name}."

    def setColour(self, colour):
        self.colour = colour

    def honkHorn(self):
        print(self.horn)

class Bike(Vehicle):
    def __init__(self, driver, colour, wheels = 2):
        self.driver = driver
        self.wheels = wheels
        self.colour = colour
        self.name = 'bike'
        self.horn = 'ring'

class Car(Vehicle):
    def __init__(self, driver, colour, wheels = 4):
        self.driver = driver
        self.wheels = wheels
        self.colour = colour
        self.name = 'car'
        self.passengers = 0
        self.horn = 'beep'

    def addPassengers(self, new):
        self.passengers += new

class Truck(Vehicle):
    def __init__(self, driver, colour, wheels = 4):
        self.driver = driver
        self.wheels = wheels
        self.colour = colour
        self.name = 'truck'
        self.cargo = []
        self.horn = 'awooga'

    def addCargo(self, newCargo):
        self.cargo.append(newCargo)



if __name__ == '__main__':
    pass
