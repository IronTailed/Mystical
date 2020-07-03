from .Locations import *

class Player:
    def __init__(self):
        #using self.skills to store skills as well as attack values in a dictionary
        self.name = ''
        self.skills = {'punch':2}
        self.gold = 10
        self.hp = 10
        self.level = 1
        self.xp = 0
        self.xpthreshold = 5
        self.defense = 0
        self.maxhp = self.hp + self.level - 1
        self.location = Road()
        self.visited = ['Road']
        self.turncount = 0
        #tracking progress
        self.defboss1 = False
        self.defboss2 = False

    def level_up(self): 
        self.xp = 0
        self.level += 1
        self.maxhp += 1
        self.gold += 2
        self.xpthreshold = round(self.xpthreshold*1.1)
        print('You levelled up! Your current level is: %s' % self.level)

    def adv_turn(self):
    	self.turncount += 1