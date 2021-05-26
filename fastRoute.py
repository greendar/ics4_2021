import random

numPoints = 3

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def distFromPoint(self: ****************)

class RandPoint(Point):
    def __init__(self):
        self.x = random.randint(0,10)
        self.y = random.randint(0,10)

origin = Point(0, 0)

pList = [origin]

for i in range(3):
    a = RandPoint()
    pList.append(a)
    del a

pList.append(Point(10,10))

for item in pList:
    print(item)

outList = []

for i in pList:
    for j in pList:
        if j == i:
            continue
        for k in p
