import random

"""
Classes in our game:
    Warrior   *** STR
    Mage      *** INT
    Assasin   *** DEX
    Cleric    *** WIS
    Bard      *** CHR
    Orc       *** CON

"""
classes = ('Warrior', 'Mage', 'Assasin', 'Cleric', 'Bard', 'Orc')

def d6():
    return random.randint(1,6)

def fourD6MinusLow():
    rolls = []
    for i in range(4):
        rolls.append(d6())
    rolls.sort(reverse = True)
    rolls.pop()
    return sum(rolls)

def getStats():
    stats = []
    for i in range(6):
        stats.append(fourD6MinusLow())
    stats.sort()
    return stats

def getClass():
    return random.choice(classes)


class Hero:
    classStats = {'Warrior': 'str', 'Mage': ' int'} # does this do anything??????????
    # yes it is for future where the assign stats method can be drastically reduced
    # in size

    def __init__(self, name):
        self.name = name
        self.heroType = getClass()
        self.statDict = {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'chr': 0}
        self.stats = getStats()
        self.assignStats()
        self.strength = self.statDict['str']
        self.dexterity = self.statDict['dex']
        self.constitution = self.statDict['con']
        self.intelligence = self.statDict['int']
        self.wisdom = self.statDict['wis']
        self.charisma = self.statDict['chr']
        self.inventory = Inventory()


    def printHero(self):
        print(self.name, self.heroType)
        print('Str: ', self.strength)
        print('Int: ', self.intelligence)
        print('Wis: ', self.wisdom)
        print('Dex: ', self.dexterity)
        print('Con: ', self.constitution)
        print('Chr: ', self.charisma)
        print()
        self.inventory.printInventory()


    def assignStats(self):
        if self.heroType == 'Warrior':
            self.statDict['str'] = self.stats.pop()
            random.shuffle(self.stats)
            for stat in self.statDict:
                if self.statDict[stat] == 0:
                    if len(self.stats) == 0:
                        break
                    else:
                        self.statDict[stat] = self.stats.pop()
            return self.statDict

        elif self.heroType == 'Mage':
            self.statDict['int'] = self.stats.pop()
            random.shuffle(self.stats)
            for stat in self.statDict:
                if self.statDict[stat] == 0:
                    if len(self.stats) == 0:
                        break
                    else:
                        self.statDict[stat] = self.stats.pop()

        elif self.heroType == 'Assasin':
            self.statDict['dex'] = self.stats.pop()
            random.shuffle(self.stats)
            for stat in self.statDict:
                if self.statDict[stat] == 0:
                    if len(self.stats) == 0:
                        break
                    else:
                        self.statDict[stat] = self.stats.pop()

        elif self.heroType == 'Cleric':
            self.statDict['wis'] = self.stats.pop()
            random.shuffle(self.stats)
            for stat in self.statDict:
                if self.statDict[stat] == 0:
                    if len(self.stats) == 0:
                        break
                    else:
                        self.statDict[stat] = self.stats.pop()

        elif self.heroType == 'Bard':
            self.statDict['chr'] = self.stats.pop()
            random.shuffle(self.stats)
            for stat in self.statDict:
                if self.statDict[stat] == 0:
                    if len(self.stats) == 0:
                        break
                    else:
                        self.statDict[stat] = self.stats.pop()
        elif self.heroType == 'Orc':
            self.statDict['con'] = self.stats.pop()
            random.shuffle(self.stats)
            for stat in self.statDict:
                if self.statDict[stat] == 0:
                    if len(self.stats) == 0:
                        break
                    else:
                        self.statDict[stat] = self.stats.pop()
        else:
            print('how did this happen') # ***********************************


class Inventory:
    def __init__(self):
        self.armour = None
        self.weapon = None
        self.potion = None

    def giveArmour(self, armour):
        self.armour = armour

    def giveWeapon(self, weapon):
        self.weapon = weapon

    def givePotion(self, potion):
        self.potion = potion

    def printInventory(self):
        print('Armour: ', self.armour)
        print('Weapon: ', self.weapon)
        print('Potion: ', self.potion)






if __name__ == '__main__':
    a = Hero('Bob')
    a.inventory.giveArmour('Netherite')
    a.inventory.givePotion('Healing')
    a.inventory.giveWeapon('Bow')
    a.printHero()
