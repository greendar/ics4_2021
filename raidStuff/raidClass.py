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
        return fileName0, fileName1



    def raidZeroRead(fN0, fN1):
        tempFile0 = open(fN0, 'r')
        tempFile1 = open(fN1, 'r')

        tempStr0 = tempFile0.read()
        tempStr1 = tempFile1.read()

        i = 0
        tempStr = ""
        for letter in tempStr0:
            tempStr += letter
            tempStr += tempStr1[i]
            i += 1

        return tempStr






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
