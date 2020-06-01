import random

#enemy classes-------------------------------------------------------------------------------------------------------------------------------------------------------------
class Bandit:
    def __init__(self):
        self.name = 'Bandit'
        self.damage = 2
        self.hp = 4
        self.loot = random.randint(1,3)

class Drunk:
    def __init__(self):
        self.name = 'Drunk'
        self.damage = 1
        self.hp = 5
        self.loot = random.randint(1,3)

class Troll: 
    def __init__(self):
        self.name = 'Troll'
        self.damage = 4
        self.hp = 8
        self.loot = random.randint(2,4)

class Lich:
    def __init__(self):
        self.name = 'Lich'
        self.damage = 6
        self.hp = 2
        self.loot = random.randint(3,4)
