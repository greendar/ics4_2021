from raidClass import Raid
from songs import allstar

aString = "1234567890abcdefghijklmnopqrstuvwxyz"


f0, f1 = Raid.raidZeroWrite(allstar, "newFile")

combine = Raid.raidZeroRead(f0, f1)

g = open('output.txt', 'w')
g.write(combine)
g.close()
