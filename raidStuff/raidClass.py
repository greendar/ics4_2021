import os

class Raid:
    def raidZeroWrite(dataIn, fileName):
        raidType = 'raid0'
        fileName0 = 'data/' + fileName + raidType + '-' + "0.txt"
        fileName1 = 'data/' + fileName + raidType + '-' + "1.txt"
        f1 = open(fileName0, 'w')
        f2 = open(fileName1, 'w')

        dataIn = iter(dataIn)

        for char in dataIn:
            f1.write(char)
            try:
                f2.write(next(dataIn))
            except StopIteration:
                pass
        f1.close()
        f2.close()

    def raidZeroRead():


    def raidOne(dataIn, fileName):
        raidType = 'raid1'
        fileName0 = fileName + raidType + '-' + "0.txt"
        fileName1 = fileName + raidType + '-' + "1.txt"
        f1 = open(fileName0, 'w')
        f2 = open(fileName1, 'w')

        for char in dataIn:
            f1.write(char)
            f2.write(char)
        f1.close()
        f2.close()
