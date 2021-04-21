class Monster:
    def __init__(self, name, attack, damage, defense, health):
        self.name = name
        self.attack = attack
        self.damage = damage
        self.defense = defense
        self.health = health

    def printMonster(self):
        print(self.name)
        print('Attack: ', self.attack)
        print('Damage: ', self.damage)
        print('Defense: ', self.defense)
        print('Health: ', self.health)


if __name__ == '__main__':
    m = Monster('Ghoul', 5, 9, 10, 12)
    m.printMonster()
