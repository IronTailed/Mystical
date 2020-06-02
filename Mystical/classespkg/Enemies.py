import random


#enemy classes-------------------------------------------------------------------------------------------------------------------------------------------------------------
class Bandit:
    def __init__(self):
        self.name = 'Bandit'
        self.damage = random.randint(1,2)
        self.hp = 4
        self.loot = random.randint(2,3)
        self.is_boss = False

class Drunk:
    def __init__(self):
        self.name = 'Drunk'
        self.damage = random.randint(1,2)
        self.hp = 4
        self.loot = random.randint(2,3)
        self.is_boss = False

class Troll: 
    def __init__(self):
        self.name = 'Troll'
        self.damage = random.randint(3,4)
        self.hp = 8
        self.loot = random.randint(3,6)
        self.is_boss = False

class Lich:
    def __init__(self):
        self.name = 'Lich'
        self.damage = random.randint(3,5)
        self.hp = 4
        self.loot = random.randint(3,7)
        self.is_boss = False

class Wyvern:
    def __init__(self):
        self.name = 'Wyvern'
        self.damage = random.randint(8,10)
        self.hp = 35
        self.loot = random.randint(6,9)
        self.is_boss = False

class Chimera:
    def __init__(self):
        self.name = 'Chimera'
        self.damage = random.randint(5,7)
        self.hp = 70
        self.loot = random.randint(6,9)
        self.is_boss = False


class Boss_1:
    def __init__(self):
        self.name = 'Mydrias, the Deceiver'
        self.damage = random.randint(10,17)
        self.hp = 100
        self.loot = 25
        self.is_boss = True

class Shapeshifter:
    def __init__(self):
        self.name = 'Shapeshifter'
        self.damage = random.randint(13,15)
        self.hp = 80
        self.loot = random.randint(10,13)
        self.is_boss = False

class Sprite:
    def __init__(self):
        self.name = 'Sprite'
        self.damage = random.randint(15,17)
        self.hp = 45
        self.loot = random.randint(10,13)
        self.is_boss = False

class Boss_2:
    def __init__(self):
        self.name = 'Ilvisar, the Unbroken'
        self.damage = random.randint(20,25)
        self.hp = 200
        self.loot = 40
        self.is_boss = True

