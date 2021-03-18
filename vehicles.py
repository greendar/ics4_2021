class Vehicle:
    def __init__(self, driverName, name = 'Vehicle', numTires = 0):
        self.driverName = driverName
        self.name = name
        self.numTires = numTires
        self.Cargo = False

    def __str__(self):
        return f"{self.name} {self.numTires} {self.driverName}"

    def setColour(self, colour):
        self.colour = colour

class Bike(Vehicle):
    def __init__(self, driverName):
        super().__init__(self, driverName)

if __name__ == "__main__":
    a = Vehicle(4, "Bob")
    print(a)
    b = Bike("Sally")
    print(b)
