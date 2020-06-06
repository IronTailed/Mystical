import random


#enemy classes-------------------------------------------------------------------------------------------------------------------------------------------------------------
class Bandit:
    def __init__(self):
        self.name = 'Bandit'
        self.damage = random.randint(1,2)
        self.hp = 4
        self.loot = random.randint(2,3)
        self.is_boss = False
        self.sentient = True

class Drunk:
    def __init__(self):
        self.name = 'Drunk'
        self.damage = random.randint(1,2)
        self.hp = 4
        self.loot = random.randint(2,3)
        self.is_boss = False
        self.sentient = False
#lvl 5
class Troll: 
    def __init__(self):
        self.name = 'Troll'
        self.damage = random.randint(3,4)
        self.hp = 8
        self.loot = random.randint(3,6)
        self.is_boss = False
        self.sentient = True

class Lich:
    def __init__(self):
        self.name = 'Lich'
        self.damage = random.randint(3,5)
        self.hp = 4
        self.loot = random.randint(3,7)
        self.is_boss = False
        self.sentient = False
#lvl 20
class Wyvern:
    def __init__(self):
        self.name = 'Wyvern'
        self.damage = random.randint(4,7)
        self.hp = 27
        self.loot = random.randint(6,9)
        self.is_boss = False
        self.sentient = False

class Chimera:
    def __init__(self):
        self.name = 'Chimera'
        self.damage = random.randint(3,5)
        self.hp = 70
        self.loot = random.randint(6,9)
        self.is_boss = False
        self.sentient = False

#lvl 35
class Boss_1:
    def __init__(self):
        self.name = 'Mydrias, the Deceiver'
        self.damage = random.randint(10,17)
        self.hp = 100
        self.loot = 25
        self.is_boss = True
        self.sentient = False
#lvl 36
class Shapeshifter:
    def __init__(self):
        self.name = 'Shapeshifter'
        self.damage = random.randint(6,8)
        self.hp = 80
        self.loot = random.randint(10,13)
        self.is_boss = False
        self.sentient = True

class Sprite:
    def __init__(self):
        self.name = 'Sprite'
        self.damage = random.randint(15,16)
        self.hp = 45
        self.loot = random.randint(10,13)
        self.is_boss = False
        self.sentient = True
#lvl 50
class Boss_2:
    def __init__(self):
        self.name = 'Ilvisar, the Unbroken'
        self.damage = random.randint(16,18)
        self.hp = 150
        self.loot = 40
        self.is_boss = True
        self.sentient = False

