import random
from classespkg import *

P1 = Player()
proximity = ''
possible_skills = {'Punch':2, 'Fireball':4, 'TimeBend': 6}
current_skill = 'Punch' #default current_skill is punch
upgrade_count = 0

#actions-------------------------------------------------------------------------------------------------------------------------------------------------------------------


def find():
    '''This function will spawn an ememy'''
    global proximity
    if proximity == '':

        if P1.level <= 4:
            x = random.randint(1,2)
            if x == 1:
                proximity = Bandit()
            if x == 2:
                proximity = Drunk()
        elif P1.level <= 19:
            x = random.choice([True, False])
            if x:
                proximity = Troll()
            else:
                proximity = Lich()
        elif P1.level <= 34:
            x = random.choice([True,False])
            if x:
                proximity = Chimera()
            else:
                proximity = Wyvern()
        elif P1. level == 35:
            proximity = Boss_1()
        elif P1. level >= 36:
            x = random.choice([True,False])
            if x:
                proximity = Shapeshifter()
            else:
                proximity = Sprite()

        if proximity.is_boss == False:
            print('You find a %s. They look angry.' % proximity.name)
        elif proximity.name == 'Mydrias, the Deceiver':
            print('''
Mydrias the Deceiver looks down at you from its perch on the mountain.
You have only heard of this dragon in legends.
You quake with fear as Mydrias draws closer...
Towards the inevitable....
''')
    else:
        print('Proximity is not empty! There is a %s!' % proximity.name)

def def_skill():
    '''This function sets a default skill to use.'''
    global current_skill
    skill = input('What skill would you like to set as your default?')
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
    if proximity == '':
        print('There\'s nothing to attack! proximity is empty!')
    else:
        if current_skill == 'TimeBend':
            proximity.damage = proximity.damage - 1
        proximity.hp = proximity.hp - P1.skills[current_skill] #subtracts health here of the enemy
        print('You hit %s for %s damage. Its health is %s.' % (proximity.name, P1.skills[current_skill], proximity.hp))
        P1.hp = P1.hp - proximity.damage
        print ('%s hit you for %s damage. Your Health is %s' % (proximity.name, proximity.damage, P1.hp)) #subtracts health of the player.
        if P1.hp <= 0:
            game_over()


        if proximity.hp <= 0:
            print('You have killed the %s' % proximity.name)
            print('You loot %s gold coins off the %s' % (proximity.loot, proximity.name))
            P1.gold = P1.gold + proximity.loot
            P1.level = P1.level + 1
            P1.maxhp = P1.maxhp + 1  
            print('You have leveled up. Your current level is %s' % P1.level)
            print('The area is now clear.')
            proximity = ''

def learn():
    '''This function will let you learn a skill!'''
    global P1
    skill = input('What skill would you like to learn?')
    if skill not in possible_skills:
        print('This skill is unknown even to the great sages of the land.')
    else:
        if skill in possible_skills:
            if skill == 'Fireball' and P1.level >= 5:
                P1.skills.update({'Fireball':4})
                print('You have learned the skill Fireball!')
            elif skill == 'TimeBend' and P1.level >= 10:
                P1.skills.update({'TimeBend' : 6})
                print('You have learned the skill TimeBend!')
            else: 
                print('You are not high enough level to learn this skill!')

def game_over():
    global P1
    print('You have died. You were level %s' % P1.level)
    print('You had learned the following skills:')
    for key in P1.skills.keys():
        print(key)
    quit()

def exit():
    x = input('Would you like to quit? Type \'Y\' or \'N\' ')
    if x == 'Y' or x == 'Yes':
        game_over()
    else: 
        print('Whew!')


def heal():
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
    global current_skill
    global P1
    global upgrade_count
    upgrade_cost = 3 + 4 * upgrade_count
    a = input('The master mage says: Would you like to upgrade your current default skill, %s? This will cost %s. Type \'Y\' or \'N\' . ' % (current_skill,upgrade_cost))
    if a in  ['Y','Yes'] and P1.gold > upgrade_cost:
        P1.skills[current_skill] = round(P1.skills[current_skill] * 1.5)
        print('''The mage chants. 
        You see energy running through your body. 
        Your veins course with power. 
        You have successfully upgraded your skill %s. It now does %s damage. 
        Congratulations!''' % (current_skill, P1.skills[current_skill]))
        P1.gold = P1.gold - upgrade_cost
        upgrade_count += 1
    elif a in ['N', 'No']:
        print('The mage says: \' Come back another time!\' ')
    elif P1.gold <= upgrade_cost:
        print('''The mage shakes his head.
        Gruffly, he barks: \"This stuff isn\'t free, you know.\"
        ''')

def help():
   print('''A text-based rpg. WIP

You are in a strange land. Try to survive.

Use find, or \'f\' to find enemies, then \'attack\', or \'a\' , to attack them using your default weapon.

Use \'heal\' or \'h\'  to heal in exchange for gold.

You will unlock new skills every couple levels. You may learn these skills using \'learn\' or \'l\'

At level 5 you may learn Fireball and at 10 you may learn TimeBend. 

Set your current skill via \'default skill\' or \'ds\'. Defaults to Punch. 

You may upgrade your current skill via \'upgrade\' or \'u\'. The cost increases every time.

You may quit using \'quit\', \'exit\', or \'q\'.

You may view your information using \'status\' or \'s\'.

You may access this help screen again using \'help\' or \'i\'.

You may beg using \'beg\' or \'b\' when you are not in combat. Beware! Not all are charitable...

Skills: 
Punch[2]: The quick jab that Grandpa taught you.
Fireball[4]: The workhorse spell of wizards everywhere.
TimeBend[6]: By bending time you are able to both harm your enemy and reduce incoming damage by 1.

''')

def status():
    global P1
    print(''' 

Your name is %s

You know the skills: 
%s

Your current skill is : %s

You have %s gold.

You have %s hp.

Your maximum hp is %s.

You have %s levels.

You have %s defense.
'''

% (P1.name, P1.skills, current_skill, P1.gold, P1.hp, P1.maxhp, P1.level, P1.defense))


def beg():
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
            if P1.hp <= 0:
                game_over()
    else: 
        print('''
The proximity is not empty! 
There is a %s in the proximity!

''' % proximity.name)





def main():
    global P1
    P1 = Player()
    proximity = ''
    possible_skills = {'Punch':2, 'Fireball':4, 'TimeBend': 6}
    current_skill = 'Punch' #default current_skill is punch
    print('You are in a mysterious land. Survive.')
    name = input('*An old man approaches you*. In a deep voice he asks: What is your name?')
    print ('''Ah yes, your name is %s. I knew your father many years ago.
Good luck on your journey. Type \'help\' for help.
        ''' % name)
    P1.name = name


    while True:
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






if __name__ == '__main__':
    main()














