from config.data import names, gear

"""
class Item:
    def __init__(self, name, light, melee, range, damage, healing, armour, uses):
        self.name = name   : str
        self.light = light : bool
        self.melee = melee : bool
        self.range = range : int
        self.damage = damage   : int   # think about it
        self.healing = healing  : bool
        self.armour = armour    : bool
        self.uses = uses        : int

"""

def returnBool(boolIn):
    if boolIn == "True":
        return True
    elif boolIn == "False":
        return False
    else:
        # Make this better #################################
        print("The input should have been either true or false but it was not.")


class Item:
    def __init__(self, name, light, melee, range, damage, healing, armour, uses):
        self.name = name
        self.light = light
        self.melee = melee
        self.range = range
        self.damage = damage
        self.healing = healing
        self.armour = armour
        self.uses = uses

    def __str__(self):
        stringOut = ""
        stringOut += f"Name: {self.name} \n"
        stringOut += f"Light: {self.light} \n"
        stringOut += f"Melee: {self.melee} \n"
        stringOut += f"Range: {self.range} \n"
        stringOut += f"Damage: {self.damage} \n"
        stringOut += f"Healing: {self.healing} \n"
        stringOut += f"Armour: {self.armour} \n"
        stringOut += f"Uses: {self.uses} \n"
        return stringOut



if __name__ == "__main__":
    bob = gear['Knife'].split(', ')
    print( bob, bob[1])
    a = Item('Knife',
        returnBool(bob[0]),
        returnBool(bob[1]),
        int(bob[2]),
        int(bob[3]),
        returnBool(bob[4]),
        returnBool(bob[5]),
        int(bob[6])
        )
    print(a)

"""
items

Flash Light / Lantern / Candle / Torch
area light

Sword / Mace / Bat / Whip / Torch
melee weapons

Pistol / Cross Bow / Shot Gun / Throwing Knives / Blow Gun / Flamethrower / Torch
ranged weapons

First Aid Kit / Band Aid / Gauze / Glowing Salt Pyramid of Healing / Rubbing Alcohol / Pain Killers / Suture Kit
healing stuff

Land Mine / Grenade
boomy stuff

Leather Jacket / Motor Cycle Helmet / Steel Toed Boots / Leather Chaps

Food types
"""
