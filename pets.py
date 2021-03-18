class Pet:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Hey there")


class Dog(Pet):
    def speak(self):
        print("Woof")


if __name__ == '__main__':
    a = Pet('Goldy')
    a.speak()
    b = Dog('Spot')
    b.speak()
