import random

def play():
    print('You are in a mysterious Dark Forest. Survive.')

name = input('What is your name?')
print ('Ah yes, your name is %s' % name)

turn = 0
proximity = ''
possible_skills = {'Punch':2, 'Fireball':4, 'TimeBend': 6}


class Player:
    def __init__(self):
        #using self.skills to store skills as well as attack values in a dictionary 
        self.skills = {'Punch':2}
        self.gold = 10
        self.hp = 10
        self.level = 1
        self.defense = 0
        self.maxhp = self.hp + self.level - 1
    
P1 = Player()

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
#actions-------------------------------------------------------------------------------------------------------------------------------------------------------------------


def find():
    '''This function will spawn an ememy'''
    global proximity
    if proximity == '':

        if P1.level <= 5:
            x = random.randint(1,2)
            if x == 1:
                proximity = Bandit()
            if x == 2:
                proximity = Drunk()
        elif P1.level <= 10:
            x = random.choice([True, False])
            if x:
                proximity = Troll()
            else:
                proximity = Lich()
        print('You find a %s. They look angry.' % proximity.name)
    else:
        print('Proximity is not empty!')

def attack(skill):
    '''This function will let you attack an enemy in the proximity'''
    global proximity
    global P1
    if proximity == '':
        print('There\'s nothing to attack! proximity is empty!')
    else:
        '''check if player has skill'''
        if skill in P1.skills:
            proximity.hp = proximity.hp - P1.skills[skill] #subtracts health here of the enemy
            print('You hit %s for %s damage. Its health is %s.' % (proximity.name, P1.skills[skill], proximity.hp))
            P1.hp = P1.hp - proximity.damage
            print ('%s hit you for %s damage. Your Health is %s' % (proximity.name, proximity.damage, P1.hp)) #subtracts health of the player.
            if P1.hp <= 0:
                game_over()


            if proximity.hp <= 0:
                print('You have killed the %s' % proximity.name)
                print('You loot %s gold coins off the %s' % (proximity.loot, proximity.name))
                P1.gold = P1.gold + proximity.loot
                print('You have leveled up.')
                P1.level = P1.level + 1
                print('The area is now clear.')
                proximity = ''
        else:
            print('Player does not have this skill!')

def learn(skill):
    '''This function will let you learn a skill!'''
    global P1

    if skill not in possible_skills:
        print('This skill is unknown even to the great sages of the land.')
    else:
        if skill in possible_skills:
            if skill == 'Fireball' and P1.level >= 5:
                P1.skills.update({'Fireball':4})
                print('You have learned the skill Fireball!')
            if skill == 'TimeBend' and P1.level >= 10:
                P1.skills.update({'TimeShift' : 8})
                print('You have learned the skill TimeBend!')

def game_over():
    global P1
    print('You have died. You were level %s' % P1.level)
    print('You had learned the following skills:')
    for key in P1.skills.keys():
        print(key)
    quit()


def heal():
    global P1
    if P1.gold < 6:
        print('You can\'t pay the healer! You don\'t have enough coins!')
    elif P1.hp == P1.maxhp:
        print('You are at your max hp already!')
    else:
        price = 0.2 * P1.gold
        rprice = round(price)
        x = random.randint(1,2)
        heal_amt = 0.2 * P1.maxhp
        r_heal_amt = round(heal_amt)
        if rprice == 0:
            print('You can\'t pay the healer! You don\'t have enough coins!')
        else:
            if x == 1:
                tprice = rprice + 1
                P1.gold -= tprice
                P1.hp += r_heal_amt
                if P1.hp > P1.maxhp:
                    P1.hp = P1.maxhp
                print('You were healed by %s. Your current hp is %s. It costed %s gold.' % (r_heal_amt,P1.hp, tprice))

            if x == 2:
                tprice = rprice - 1
                P1.gold -= tprice
                P1.hp += r_heal_amt
                if P1.hp > P1.maxhp:
                    P1.hp = P1.maxhp

                print('You were healed by %s. Your current hp is %s. It costed %s gold.' % (r_heal_amt,P1.hp, tprice))


    
