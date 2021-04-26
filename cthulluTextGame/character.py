import random
import os
from config.data import names, gear

def getName():
    return random.choice(nameList)

def d6():
    return random.randint(1,6)

def fourD6MinusLow():
    rolls = []
    for i in range(4):
        rolls.append(d6())
    rolls.sort(reverse = True)
    rolls.pop()
    return sum(rolls)



class Hero:
    def __init__(self):
        self.name = getName()
        self.hitPoints =  fourD6MinusLow() + d6()
        self.sanity = fourD6MinusLow() + d6()
        self.strength = fourD6MinusLow()
        self.willPower = fourD6MinusLow()
        self.inventory = []

    def __str__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        stringOut = self.name +"\n"
        stringOut += f"Hit Points: {self.hitPoints}   Sanity: {self.sanity}" + "\n"
        stringOut += f"Strength: {self.strength}     Will Power: {self.willPower}" + "\n"
        stringOut += "Inventory:  "
        for inventoryItem in self.inventory:
            stringOut += f"{inventoryItem}, "
        stringOut += "and that's it.\n"
        return stringOut

    def giveItem(self, item):
        self.inventory.append(item)

    def dropItem(self):  # not done
        menuCounter = 1
        for invetoryItem in self.inventory:
            print(f"{menuCounter}. {invetoryItem}")
            menuCounter += 1

        choice = input("Which item would you like to drop?: ")

        try:
            choice = int(choice)
            temp = self.inventory[choice - 1]
            self.inventory.remove(self.inventory[choice - 1])
            print(temp, "removed")
            temp = input('Hit ENTER to continue')

        except ValueError:
            if choice in self.inventory:
                self.inventory.remove(choice)
                print(choice, "removed")
                temp = input('Hit ENTER to continue')

        except IndexError:
            print("Sorry that does not exist.")
            temp = input('Hit ENTER to continue')
            self.dropItem()






if __name__ == "__main__":
    bob = gear['Knife'].split(', ')
    print( bob, bob[1])
    a = Item('Knife', bob[0], bob[1], bob[2], bob[3], bob[4], bob[5], bob[6])
    print(a)
