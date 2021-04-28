#CSV Convert
#m04 d28 y2021
#


"""
opens CSV File and exports data from file as an list with lists or simpley a 2D list

To Do List:
 - will only read a line if it ends \n or just a new line [[[FIXED]]]
 - check to see what else these functions need to ignore [[[NEED TO DO!]]]
 - make code faster and more efficient [[[NOT DONE]]]
 - make a do it all function [[[NOT DONE]]]
"""

#The Do it all Function
def getCSV2DarrayData(csvfilename):
    csv2Dlist = []
    csv2Dlist = csvConvert("items.csv")
    #print(csv2Dlist)
    #print()
    csv2Dlist = checkforBooleanInString2dList(csv2Dlist)
    #print(csv2Dlist)
    #print()
    csv2Dlist = checkforINTorFloatInString2dList(csv2Dlist)
    #print(csv2Dlist)
    #print()
    csv2Dlist = checkforEmptySTRInString2dList(csv2Dlist)
    #print(csv2Dlist)
    #print()
    #print(csv2Dlist)
    #print()
    csv2Dlist = checkifItemIsUnfinished(csv2Dlist)
    csv2Dlist = formatItemsForGearPY(csv2Dlist)
    
    
    import Gear
    #print(csvListReturned)
    #print()
    csv2Dlist = Gear.items
    del Gear
    import os
    if os.path.exists("Gear.py"):
        os.remove("Gear.py")
    else:
        print("The file does not exist")
    
    
    
    return csv2Dlist




def csvConvert(csvfilename):
    """
    -opens file via {csvfilename} then returns a 2D list based on csv data given
    -any extra fomating i.e. like colour may not be notice by these functions and may break stuff
        try to keep the tables plain and simple.
    -i never seen what the file looks like on more detailed csv files
    """
    savedFileLines = []
    csvfile = open(csvfilename, 'r')
    print(csvfile.read())
    csvfile.close()
    
    csvfile = open(csvfilename, 'r')
    while True:#will only break out if it does not see a new line in the current line
        lineRead = csvfile.readline()
        if lineRead.find("\n")==-1:
            currentlineData = lineRead.split(',')#splits into list by the ","
            if len(currentlineData)==0:
                break
            if len(currentlineData)==1 and len(currentlineData[0])==0:
                #breaks if current line array has 1 empty element
                break
            savedFileLines.append(currentlineData)
            break
        lineRead = lineRead.replace("\n", "")#removes newlines
        currentlineData = lineRead.split(',')#splits into list by the ","
        savedFileLines.append(currentlineData)
    csvfile.close()
    csvData = savedFileLines
    return csvData


def checkforBooleanInString2dList(list2dInput):
    """
    makes any form 
    """
    for y in range(len(list2dInput)):
        for x in range(len(list2dInput[y])):
            if list2dInput[y][x]=='':
                continue
            if str(type(list2dInput[y][x])) == "<class 'str'>":
                if list2dInput[y][x].upper()=="TRUE":
                    list2dInput[y][x] = True
                elif list2dInput[y][x].upper()=="FALSE":
                    list2dInput[y][x] = False
    list2dOutput = list2dInput
    return list2dOutput


def checkforINTorFloatInString2dList(list2dInput):
    for y in range(len(list2dInput)):
        for x in range(len(list2dInput[y])):
            if list2dInput[y][x]=='':
                continue
            if str(type(list2dInput[y][x])) == "<class 'str'>":
                """
                uses .upper() to check for numbers only
                """
                if list2dInput[y][x].upper() == list2dInput[y][x]:
                    strVerInput = str(list2dInput[y][x]) #is now only called once and used twice
                    floatVerInput = float(list2dInput[y][x]) #is now only called once and used twice
                    intVerInput = int(list2dInput[y][x]) #is now only called once and used twice
                    if str(floatVerInput) == strVerInput:
                        #print("is Float")
                        list2dInput[y][x] = floatVerInput
                    elif str(intVerInput) == strVerInput:
                        #print("is INT")
                        list2dInput[y][x] = intVerInput
    list2dOutput = list2dInput
    return list2dOutput

def checkforEmptySTRInString2dList(list2dInput):
    """
    looks for '' and replaces it with None
    """
    for y in range(len(list2dInput)):
        for x in range(len(list2dInput[y])):
            if list2dInput[y][x]=='':
                list2dInput[y][x] = None
                continue
    list2dOutput = list2dInput
    return list2dOutput
    





def checkifItemIsUnfinished(list2dInput):
    errorLogfile = open("ItemErrorLog.txt", 'w+')
    for y in range(1, len(list2dInput)):
        skipItemFlag = False
        for x in range(len(list2dInput[y])):
            if list2dInput[y][x]==None:
                errorLogfile.write(f"!!!Missing!!! The Item [{str(list2dInput[y][0])}] was not given a value for it's [{str(list2dInput[0][x])}].\n")
                skipItemFlag = True
            if (skipItemFlag):
                continue
            print(list2dInput[y][x])
    errorLogfile.close()
    list2dOutput = list2dInput
    return list2dOutput



"""
format:
gear = {
    'Knife': "False, True, 10, 4, False, False, -1"

}

"""
def formatItemsForGearPY(list2dInput):
    gearPYfile = open("Gear.py", 'w+')
    gearPYfile.write("items = {\n")
    itemList = []
    for y in range(1, len(list2dInput)):
        skipItemFlag = False
        ItemName = "'"
        ItemStats = "'"
        for x in range(len(list2dInput[y])):
            if list2dInput[y][x]==None:
                skipItemFlag = True
            if (skipItemFlag):
                continue
        if (skipItemFlag):
            continue
        else:
            ItemName += str(list2dInput[y][0]) + "': "
            for x in range(1, len(list2dInput[y])-1):
                ItemStats += str(list2dInput[y][x]) + ", "
            for x in range(len(list2dInput[y])-1, len(list2dInput[y])):
                ItemStats += str(list2dInput[y][x]) + "'"
            print(ItemName)
            print(ItemStats)
            finishedITEMdata = "\t" + ItemName + ItemStats
            itemList.append(str(finishedITEMdata))
            print(finishedITEMdata)
            print(itemList)
            
            
            
            print()
        if (skipItemFlag):
            continue
    for i in range(len(itemList)):
        if i!=(len(itemList)-1):
            gearPYfile.write(itemList[i] + ",\n")
        else:
            gearPYfile.write(itemList[i] + "\n")
            

    gearPYfile.write("}\n")
    gearPYfile.close()
    list2dOutput = list2dInput
    return list2dOutput







if __name__ == "__main__":
    csvListReturned = getCSV2DarrayData("items.csv")
    print(csvListReturned)
    print()
    
    
    
    








    
