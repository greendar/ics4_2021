class Vehicle:
    def __init__(self, driver, colour, wheels):
        self.driver = driver
        self.wheels = wheels
        self.colour = colour
        self.name = 'vehicle'

    def __str__(self):
        return f"{self.driver} is driving the {self.colour} {self.wheels} wheeled {self.name}."

    def setColour(self, colour):
        self.colour = colour

class Bike(Vehicle):
    def __init__(self, driver, colour, wheels = 2):
        self.driver = driver
        self.wheels = wheels
        self.colour = colour
        self.name = 'bike'

class Car(Vehicle):
    def __init__(self, driver, colour, wheels = 4):
        self.driver = driver
        self.wheels = wheels
        self.colour = colour
        self.name = 'car'
        self.passengers = 0

    def addPassengers(self, new):
        self.passengers += new

class Truck(Vehicle):
    def __init__(self, driver, colour, wheels = 4):
        self.driver = driver
        self.wheels = wheels
        self.colour = colour
        self.name = 'truck'
        self.cargo = []

    def addCargo(self, newCargo):
        self.cargo.append(newCargo)

class ElCamino(Truck, Car):
    def __init__(self, driver, colour, wheels = 4):
            self.driver = driver
            self.wheels = wheels
            self.colour = colour
            self.name = 'El Camino'
            self.passengers = 0
            self.cargo = []



if __name__ == '__main__':
    a = ElCamino('Jessie', 'black')
    a.addCargo('potatoes')
    a.addCargo('beans')
    a.addPassengers(3)
    print(a)
    print(a.passengers)
    print(a.cargo)
    a.setColour('blue')
    print(a)
