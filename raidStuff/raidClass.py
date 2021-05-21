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


"""
    def raidZeroRead(fileName):
        #Darrien's Solution
        
        raidType = 'raid0'
        raidSize = 2
        #fileNames[raidSize] = ["" for i in range(raidSize)]
        #print(fileNames)
        fileName0 = 'data/' + fileName + raidType + '-' + "0.txt"
        fileName1 = 'data/' + fileName + raidType + '-' + "1.txt"
        f1 = open(fileName0, 'r')
        f2 = open(fileName1, 'r')
        file_string_01 = f1.read()
        file_string_02 = f2.read()
        f1.close()
        f2.close()

        dataout = ""
        while True:
            if len(file_string_01) != 0:
                dataout += file_string_01[0]
            if len(file_string_02) != 0:
                dataout += file_string_02[0]
            #print(dataout, file_string_01 ,file_string_02)

            file_string_01 = file_string_01[1:]
            file_string_02 = file_string_02[1:]
            if (len(file_string_01)==0) and (len(file_string_02)==0):
                break
        return dataout
"""

    def raidZeroRead(fN0, fN1):
        tempFile0 = open(fN0, 'r')
        tempFile1 = open(fN1, 'r')

        tempStr0 = tempFile0.read()
        tempStr1 = tempFile1.read()
        tempFile0.close()
        tempFile1.close()

        i = 0
        tempStr = ""
        for letter in tempStr0:
            tempStr += letter
            tempStr += tempStr1[i]   # index type error here if tempStr1 is shorter than tempStr0
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
