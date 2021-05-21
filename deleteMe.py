import random
import string

testText = "the quick brown fox jumped over the lazy dog"

def cleanText(textFile):
    f = open(textFile, 'r')
    fileCont = f.read()
    stringOut = ""
    i = 0
    for letter in fileCont:
        if ord(letter) <= 122 and ord(letter) >= 97:
            stringOut += letter
            i += 1
        if i == 60:
            stringOut += "\n"
            i = 0

    return stringOut


def ceaserCypher(stringIn, shift):
    stringOut = ""
    for letter in stringIn:
        if letter == " ":
            stringOut += " "
        else:
            newIndex = ord(letter) + shift
            if newIndex > 122:
                newIndex = newIndex % 123 + 97
            stringOut += chr(newIndex)
    return stringOut


cleanText('randomText.txt')
