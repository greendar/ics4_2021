class Shape:
    def __init__(self):
        self.name = ''


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.name = 'Rectangle'

    def __str__(self):
        return f"The rectangle is {self.width}x{self.height} with the bottom left corner at ({self.x}, {self.y})"


if __name__ == '__main__':
    a = Rectangle(2, 3, 4, 5)
    print(a)
