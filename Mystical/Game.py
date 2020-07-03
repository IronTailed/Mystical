import random
from classespkg import *

P1 = Player()
'''The Player class'''
proximity = ''
possible_skills = {'punch':2, 'fireball':4, 'timebend': 6, 'hex':10}
current_skill = 'punch' #default current_skill is punch
upgrade_count = 0

#actions-------------------------------------------------------------------------------------------------------------------------------------------------------------------

def print_each(x):
    '''print_each prints each element of a list'''
    for element in x:
        return element


def find():
    '''This function will spawn an ememy. Spanws by level groups: 0-5, 5-20, 20-35, 35-50'''
    global proximity
    if proximity == '':

        if P1.location.name == 'road':
            x = random.randint(1,2)
            if x == 1:
                proximity = Bandit()
            if x == 2:
                proximity = Drunk()
        elif P1.location.name == 'field':
            proximity = Stag()
        elif P1.location.name == 'forest':
            x = random.choice([True, False])
            if x:
                proximity = Troll()
            else:
                proximity = Lich()
        elif P1.location.name == 'cave':
            x = random.choice([True,False])
            if x:
                proximity = Chimera()
            else:
                proximity = Wyvern()
        elif P1.location.name == 'otherworld':
            x = random.choice([True,False])
            if x:
                proximity = Shapeshifter()
            else:
                proximity = Sprite()
        elif P1.location.name == 'throne':
            proximity = Boss_2()
        elif P1.level > 50:
            print('That\'s all for now! Congrats on beating the current version of the game!')
            status()
            game_over()

        if proximity.is_boss == False and proximity.sentient == True:
            print('You find a %s. They look angry.' % proximity.name)
        elif proximity.is_boss == False and proximity.sentient == False:
            print('You find a %s. They quickly draw closer to attack you.' % proximity.name)
    else:
        print('Proximity is not empty! There is a %s!' % proximity.name)

def def_skill():
    '''This function sets a default skill to use.'''
    global current_skill
    skill = input('What skill would you like to set as your default?\n')
    skill = skill.lower()
    if skill in P1.skills and skill != current_skill:
        print('Your default skill has been changed from %s to %s.' % (current_skill, skill))
        current_skill = skill
    elif skill == current_skill:
        print('%s is already your default skill!' % skill)
    else:
        print('Player does not have access to these skills. Player has access to %s' % P1.skills.keys())


def attack():
    '''This function will let you attack an enemy in the proximity'''
    global proximity
    global P1
    global current_skill
    if proximity == '':
        print('There\'s nothing to attack! Your proximity is empty!')
    else:
        current_skill = current_skill.lower()
        if current_skill == 'timebend':
            proximity.damage = proximity.damage - 1
            if proximity.damage <= 0:
                proximity.damage = 0
        elif current_skill == 'hex':
            proximity.hp = round(proximity.hp * 0.5)
        proximity.hp = proximity.hp - P1.skills[current_skill] #subtracts health here of the enemy
        print('You hit %s for %s damage. Its health is %s.' % (proximity.name, P1.skills[current_skill], proximity.hp))
        P1.hp = P1.hp - proximity.damage
        print ('%s hit you for %s damage. Your Health is %s' % (proximity.name, proximity.damage, P1.hp)) #subtracts health of the player.
    


        if proximity.hp <= 0:
            if proximity.is_boss == False:
                print('You have killed the %s' % proximity.name)
                print('You loot %s gold coins off the %s' % (proximity.loot, proximity.name))
                P1.gold = P1.gold + proximity.loot
                print('The area is now clear.')
                P1.xp += proximity.xp
                print('You gained %s xp' % proximity.xp)
                proximity = ''
            else:
                if proximity.name == 'Mydrias, the Deceiver':
                    print('''Mydrias staggers....and collapses on the ground''')
                    print('You loot %s gold coins off the fallen Mydrias.' % (proximity.loot))
                    P1.gold = P1.gold + proximity.loot
                    P1.defboss1 = True
                    print('The area is now clear.')
                    proximity = ''
                if proximity.name == 'Ilvisar, the Unbroken':
                    print('''Ilvisar vanishes in a puff of smoke, leaving behind his armor.''')
                    print('You loot %s gold coins off the Ilvisar.' % (proximity.loot))
                    P1.gold = P1.gold + proximity.loot
                    P1.defboss2 = True
                    print('The area is now clear.')
                    proximity = ''



def learn():
    '''This function will let you learn a skill!'''
    global P1
    skill = input('What skill would you like to learn?\n')
    skill = skill.lower()
    if skill not in possible_skills:
        print('This skill is unknown even to the great sages of the land.')
    else:
        if skill in possible_skills:
            if skill == 'fireball' and P1.level >= 5:
                P1.skills.update({'fireball':4})
                print('You have learned the skill Fireball!')
            elif skill == 'timebend' and P1.level >= 15:
                P1.skills.update({'timebend' : 6})
                print('You have learned the skill TimeBend!')
            elif skill == 'hex' and P1.level > 35:
                P1.skills.update({'hex' : 10})
                print('You have learned the skill Hex!')
            else: 
                print('You are not high enough level to learn this skill!')

def game_over():
    '''Internal function to end the game in case of player death'''
    global P1
    print('You have died. You were level %s' % P1.level)
    print('You had learned the following skills:')
    for key in P1.skills.keys():
        print(key)
    quit()

def exit():
    '''Quits the game'''
    x = input('Would you like to quit? Type \'Y\' or \'N\' \n')
    x = x.lower()
    if x == 'y' or x == 'yes':
        game_over()
    else: 
        print('Whew!')


def heal():
    '''Heals the player for a price'''
    global P1
    if P1.hp == P1.maxhp:
        print('You are at your max hp already!')
    else:
        price = 0.2 * P1.gold
        rprice = round(price)
        x = random.randint(1,2)
        heal_amt = 0.2 * P1.maxhp
        r_heal_amt = round(heal_amt)
        if rprice == 0:
            print('You can\'t pay the healer! You don\'t have enough coins!')
        elif P1.gold < 6:
            tprice = 2
            P1.gold -= tprice
            P1.hp += r_heal_amt
            if P1.hp > P1.maxhp:
                P1.hp = P1.maxhp
            print('You were healed by %s. Your current hp is %s. It costed %s gold.' % (r_heal_amt, P1.hp, tprice))        
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

def upgrade():
    '''upgrades skill'''
    global current_skill
    global P1
    global upgrade_count
    upgrade_cost = 3 + 4 * upgrade_count
    a = input('The master mage says: Would you like to upgrade your current default skill, %s? This will cost %s. Type \'Y\' or \'N\' . \n' % (current_skill,upgrade_cost))
    a = a.lower()
    if a in  ['y','yes'] and P1.gold >= upgrade_cost:
        P1.skills[current_skill] = round(P1.skills[current_skill] * 1.5)
        print('''The mage chants. 
        You see energy running through your body. 
        Your veins course with power. 
        You have successfully upgraded your skill %s. It now does %s damage. 
        Congratulations!''' % (current_skill, P1.skills[current_skill]))
        P1.gold = P1.gold - upgrade_cost
        upgrade_count += 1
    elif a in ['n', 'no']:
        print('The mage says: \' Come back another time!\' ')
    elif P1.gold < upgrade_cost:
        print('''The mage shakes his head.
        Gruffly, he barks: \"This stuff isn\'t free, you know.\"
        ''')

def help():
    '''help function'''
    print('''A text-based rpg. WIP

You are in a strange land. Try to survive.

Use find, or \'f\' to find enemies, then \'attack\', or \'a\' , to attack them using your default weapon.

Use \'heal\' or \'h\'  to heal in exchange for gold.

You will unlock new skills every couple levels. You may learn these skills using \'learn\' or \'l\'
Mydrias the Deceiver
At level 5 you may learn Fireball, at 15 TimeBend, and at 36 Hex. 

Set your current skill via \'default skill\' or \'ds\'. Defaults to Punch. 

You may upgrade your current skill via \'upgrade\' or \'u\'. The cost increases every time.

You may quit using \'quit\', \'exit\', or \'q\'.

You may view your information using \'status\' or \'s\'.

You may access this help screen again using \'help\' or \'i\'.

You may beg using \'beg\' or \'b\' when you are not in combat. Beware! Not all are charitable...

You may attempt a negotiation using \'negotiate\' or \'n\' when you are in combat. 

Skills: 
Punch[2]: The quick jab that Grandpa taught you.
Fireball[4]: The workhorse spell of wizards everywhere.
TimeBend[6]: By bending time you are able to both harm your enemy and reduce incoming damage by 1 each time you cast TimeBend.
Hex[10] : You cast a vile hex on the enemy that reduces their health, then damages them for 10 hp.

''')

def status():
    '''this function returns player info'''
    global P1
    print(''' 

Your name is %s

You current location is the %s

You know the skills: 
%s

Your current skill is : %s

You have %s gold.

You have %s hp.

Your maximum hp is %s.

You have %s levels.

'''

% (P1.name, P1.location.name, P1.skills, current_skill, P1.gold, P1.hp, P1.maxhp, P1.level))


def beg():
    '''This function allows the player to beg for gold'''
    global P1
    global proximity
    b = random.randint(1,2)
    if proximity == '':
        if b == 1:
            gift_amt = random.randint(2,5)
            P1.gold += gift_amt
            print('''
You get %s! What a generous soul! 
You now have %s gold.

    ''' % (gift_amt,P1.gold))

        elif b == 2:
            beat_amt = random.randint(5,30)
            P1.hp -= beat_amt
            print('''
Some meanie beat you up! 
You lost %s hp! Your hp is %s 
    
    ''' % (beat_amt, P1.hp))
    else: 
        print('''
The proximity is not empty! 
There is a %s in the proximity!

''' % proximity.name)


def level():
    #used for testing
    global P1
    x = input('To what level do you want to go to?\n')
    P1.level =  int(x)


def negotiate():
    '''This function allows the player to negotiate with enemies'''
    global proximity
    global P1
    if proximity == '':
        print('Proximity is empty!')
    else:
        if proximity.is_boss == True:
            print('You cannot negotiate with %s!' % proximity.name)
        elif proximity.sentient == False:
            print('%s is not sentient! Your attempts at negotiation fail!' % proximity.name)
            P1.hp -= proximity.damage
            print('%s hits you for %s damage! Your health is %s' % (proximity.name, proximity.damage, P1.hp))
        elif proximity.sentient == True:
            needed_bribe = round(0.5 * proximity.loot)
            x = input('''Would you like to offer a bribe in your negotiation? \n
Please enter \'Y\' or \'N\'.\n''')
            x = x.lower()
            if x in ['y', 'yes']:
                bribe_amt  = input ('''Please enter the amount of the bribe.\n''')
                try:
                    if type(eval(bribe_amt)) == int:
                        y = int(bribe_amt)
                        if y <= 0:
                            print('You can\'t do that!')
                        else:
                            if P1.gold < y:
                                print('You do not have enough gold!')
                            elif y < needed_bribe:
                                a = random.choice([True,False])
                                if a:
                                    print('Bribe successful! You have made the %s go away!' % proximity.name)
                                    proximity = ''
                                    print('You used %s gold for the bribe.' % y)
                                    P1.gold -= y
                                else:
                                    print('Bribe unsuccessful!')
                                P1.gold -= y
                            elif y >= needed_bribe:
                                print('Bribe successful! You have made the %s go away!' % proximity.name)
                                proximity = ''
                                print('You used %s gold for the bribe.' % y)
                                P1.gold -= y
                except NameError:
                    print('Please enter an integer bribe!')
            elif x in ['n', 'no']: 
                print('You choose to negotiate with the %s, sans bribe.' % proximity.name) 
                print('')
                a = random.choice([True,False])
                if a:
                    print('Negotiation successful! You have made the %s go away!' % proximity.name)
                    proximity = ''
                else:
                    print('Negotiation unsuccessful!')
                    P1.hp -= proximity.damage
                    print('%s hits you for %s damage! Your health is %s.' % (proximity.name, proximity.damage, P1.hp))
            else: 
                print('That was not a valid input! Try again.')
def move():
    global P1
    global Locations
    print('Your current location is the %s.\n You are adjacent to %s.' % (P1.location.name, P1.location.adjacent))
    x = input('Where would you like to go?\n')
    org_location_name = P1.location.name
    x = x.lower()
    if x in P1.location.adjacent:
        if P1.location.name == 'road':
            if x == 'field' and P1.level >= 0:
                P1.location = Field() 
            elif x == 'forest' and P1.level >= 5:
                P1.location = Forest()
        if P1.location.name == 'field':
            if x == 'road' and P1.level >= 0:
                P1.location = Road()
        if P1.location.name == 'forest':
            if x == 'road':
                P1.location = Road()
            if x == 'cave' and P1.level >= 20:
                P1.location = Cave()


        if P1.location.name == 'otherworld':
            if x == 'cave':
                P1.location = Cave()

       

        if P1.location.name == org_location_name:
            print('You fail to move! Try leveling up first!')
        else:
            print('You moved to %s' % P1.location.name)


    else:
        print('You cannot move there. You may move to the following locations if your level allows: \n%s' % P1.location.adjacent )





def main():
    global P1
    P1 = Player()
    proximity = ''
    possible_skills = {'Punch':2, 'Fireball':4, 'TimeBend': 6}
    current_skill = 'Punch' #default current_skill is punch
    print('You are in a mysterious land. The enemies seem to keep on coming. Survive.')
    name = input('*An old man approaches you*. In a deep voice he asks: What is your name?\n')
    print ('''Ah yes, your name is %s. I knew your father many years ago.
Good luck on your journey. Type \'help\' for help.
        ''' % name)
    P1.name = name


    while True:
        if P1.hp<=0:
            game_over()

        if P1.xp > P1.xpthreshold:
            P1.level_up()


        if P1.location.name == 'cave' and P1.defboss1 == False and P1.level >= 35 and proximity == '':
            proximity = Boss_1()
            print('''
    Mydrias the Deceiver looks down at you from its perch on the mountain.
    You have only heard of this dragon in legends.
    You quake with fear as Mydrias draws closer...
    Towards the inevitable....
            ''')

        if P1.location.name == 'throne' and P1.defboss2 == True and P1.level >= 50 and proximity == '':
            proximity = Boss_2()
            print('''
Before you, flickering in and out of existence,
stands a wind spirit - Ilvisar, the Unbroken.
It smirks. You wonder:
How many mortals had those hands killed?
            
            ''')
        z = input()
        z = z.lower()
        if z in ['spawn', 'find','hunt','f']:
            find()
        elif z in ['hit', 'kill', 'fight', 'attack','a']:
            attack()
        elif z in ['help', 'info','i']:
            help()
        elif z in ['status','s']:
            status()
        elif z in ['heal', 'healer','h']:
            heal()
        elif z in ['quit', 'leave','exit','q']:
            exit()
        elif z in ['learn', 'l']:
            learn()
        elif z in ['def_skill', 'default skill', 'def skill', 'change skill', 'ds']:
            def_skill()
        elif z in ['upgrade', 'u']:
            upgrade()
        elif z in ['beg', 'b']:
            beg()
        elif z in ['negotiate', 'n']:
            negotiate()
        elif z in ['move', 'm']:
            move()
        elif z in [ 'level']:
            level()
        else:
            print('I don\'t understand your command! Type \'help\' for info!')




if __name__ == '__main__':
    main()














