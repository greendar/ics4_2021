import math

path = [1, 87, 19, 91, 99, 100]
squareWidth = 200

def radToDeg(radIn):
	return radIn * 180/math.pi

def pythag(a, b):
    brain.print('pythag', a, b, '\n')
    return math.sqrt(a**2 + b**2)

"""
def findRoute(toSquare, fromSquare):
    # dir in degrees   mag in mm

    # figure out x
    diffX = toSquare%10 - fromSquare%10

    # figure out y
    diffY = toSquare//10 - fromSquare//10


    mag = 200 * pythag(diffX, diffY)

    dir = radToDeg(math.atan(diffX/diffY))

    return dir, mag
"""
def diffX(toSquare, fromSquare):
    x = toSquare%10 - fromSquare%10
    if toSquare%10 == 0:
        x += 10
    return x


def diffY(toSquare, fromSquare):
    y = toSquare//10 - fromSquare//10
    if toSquare%10 == 0:
        y -= 1
    return y

def findHeading(toSquare, fromSquare):
    #toSquare += 1   # *****************
    # figure out x
    x = diffX(toSquare, fromSquare)
    y = diffY(toSquare, fromSquare)
    """
    diffX = toSquare%10 - fromSquare%10

    # figure out y
    diffY = toSquare//10 - fromSquare//10

    """
    if toSquare//10 == fromSquare//10:
        if toSquare > fromSquare:
            heading = 90
        elif toSquare < fromSquare:
            heading = 270
        else:
            heading = 0

    if toSquare//10 > fromSquare//10:
        heading = 0
        dir = radToDeg(math.atan(x/y))
        heading = dir

    if toSquare//10 < fromSquare//10:
        heading = 180
        dir = radToDeg(math.atan(x/y))
        heading = 180 + dir
    brain.print('heading:', heading, '\n')
    return heading

def findMagnitude(toSquare, fromSquare):
    x = diffX(toSquare, fromSquare)
    y = diffY(toSquare, fromSquare)

    mag = 200 * pythag(x, y)
    brain.print('       mag', mag, '\n')
    return mag



def when_started1():
    global currentNum, numOne, path
    pen.move(DOWN)
    brain.clear()
    drivetrain.set_drive_velocity(300, PERCENT)
    drivetrain.set_turn_velocity(300, PERCENT)
    i = 0
    for i in range(len(path)):
        brain.print('Going to', path[i+1], '\n')
        current = path[i]
        goTo = path[i+1]
        goDir = findHeading(goTo, current)
        goMag = findMagnitude(goTo, current)
        drivetrain.turn_to_heading(goDir, DEGREES)
        drivetrain.drive_for(FORWARD, goMag, MM)
        if i < len(path):
            i += 1
        wait(0.5, SECONDS)


vr_thread(when_started1())
