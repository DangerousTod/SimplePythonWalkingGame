#!/usr/in/python
# -*- coding: utf-8 -*-

import sys
import os
import time
import random
import math

direction_data = {}

hill = {}
mountain = {}

north_country = {}
nc_e = {}
nc_e1 = {}
nc_w = {}
nc_w1 = {}

valley = {}
beach = {}
river = {}

river_north = {}
river1_north = {}
river2_north = {}

too_far = {}

items = []
equipment_values = []
equipment_dict = {}

players = ['you']

# [0] is Attack, [1] is Defense, [2] is Description, [3] Health, [4] is Name, [5] is player or enemy
you = [3, 4, "You Are A Hansome Young Lad", 100, 'You ', 'player', equipment_values, equipment_dict]
your_equipment = ['hat', 'shirt', 'shoes', 'shortsword', 'potion']


hill_players = ['Cleo ', 'Artie ', 'Wilk ']

#--------------------PLAYER SECTION------------------------------#

cleo = [1, 4, 'A lovely young lady', 15, 'Cleo ', 'player', equipment_values,  equipment_dict]
artie = [6, 6, 'Sir Artie will have none of it, non withstanding', 99, 'Artie ', 'player', equipment_values,  equipment_dict]
wilk = [5, 2, 'An all-around great guy', 66, 'Wilk ', 'player', equipment_values, equipment_dict]

hill_enemies = ['Nasty ', 'Ugly ']

#---------------------ENEMY SECTION------------------------------#

# [0] is Attack, [1] is Defend, [2] is Description, [3] Health, [4] is Name, [5]is player or enemy
nasty = [2, 3, "What A Nasty Looking Dude", 60, "Nasty ", 'enemy', equipment_values, equipment_dict]
ugly = [3, 2, "Wow, So much Ugliness", 20, "Ugly ", 'enemy', equipment_values, equipment_dict] # health was 70

#-----------------ITEMS OR EQUIPMENT-----------------------------#

# equipment_keys = [head, chest, feet, hand, carried]
equipmet_values = ['', '', '', '', '']

# [0] Slot, [1] attack adjust, [2] defend adjust, [3] description, [4] name or short description

get_scarf = []
get_hat = []
get_helmet = []
get_shirt = []
get_coat = []
get_slippers = []
get_sandals = []
get_shoes = []
get_boots = []
get_rock = []
get_dagger = []
get_short_sword = []
get_sword = []
get_potion = []
get_key = []

item_dict = {

#        "items": (items := ['hat', 'scarf']),
#        slot,attack,defense,description,name

    "get_scarf" : (scarf := [0, 0, 0, 'A basic head covering that is wrapped around the head and neck', 'scarf']),

    "get_hat": (hat := [0, 0, 1, 'A basic head covering.', 'hat']),

    "get_helmet": (helmet := [0, 0, 2, 'A cap made of metal to protect your head.', 'helmet']),

    "get_shirt": (shirt := [1, 0, 1, 'A hand sewn garmet that covers your body almost entirely.', 'shirt']),

    "get_coat": (coat := [1, 0, 2, 'A sturdy, padded garmet that protects you from injuries.', 'coat']),

    "get_slippers": (slippers := [2, 0, 0, 'Soft, warm, and fuzzy; slippers are not so much shoes as they are a statement of your place in life.', 'slippers']),

    "get_sandals": (sandals := [2, 0, 0, 'Sandals protect the soles of your feet, but your toes and ankles show.', 'sandals']),

    "get_shoes": (shoes := [2, 0, 1, 'Basic footwear.', 'shoes']),

    "get_boots": (boots := [2, 0, 2, 'Shoes made of very tough leather.', 'boots']),

    "get_rock": (rock := [3, 1, 0, 'A hard knob of rock that fits your hand nicely.', 'rock']),

    "get_dagger": (dagger := [3, 1, 0, 'A small, very sharp length of metal that is wrapped with wire at one end for your to grip.', 'dagger']),

    "get_shortsword": (shortsword := [3, 2, 1, 'A heavy, short blade with a metal handle only as long as your forearm.', 'shortsword']),

    "get_sword": (sword := [3, 3, 2, 'A straight, sharp blade with a sturdy handle that is nearly as long as your arm.', 'sword']),

    "get_potion": (potion := [4, 0, 0, 'A basic head covering that is wrapped around the head and neck.', 'potion']),
    
    "get_key": (key := [4, 0, 0, 'A small metal key that will unlock a door or box.', 'key']),
    
    }

# equipment_dict = dict(zip(equipment_keys,equipment_values))

x = ''
y = ''
a = ''
f = []
g = ''
k = ''
pk = ''
del_item = ''

river_players = []
river_enemies = []

mountain_players = []
mountain_enemies = ['Ugly ']

valley_players = []
valley_enemies = []

beach_players = []
beach_enemies = []

river_north_players = []
river_north_enemies = []

river_north1_players = []
river_north1_enemies = []

river_north2_players = []
river_north2_enemies = []

north_country_players = []
north_country_enemies = ['Nasty ']

nc_e_players = []
nc_e_enemies = []

nc_e1_players = [] 
nc_e1_enemies = []

nc_w_players = []
nc_w_enemies = []

nc_w1_players = []
nc_w1_enemies = []

too_far_players = []
too_far_enemies = []

n = "n"
s = "s"
e = "e"
w = "w"
#look = "look"

q = "Q"
home = "home"
self = "self"

N = "n"
S = "s"
E = "e"
W = "w"
#LOOK = "look"

Q = "Q"
HOME = "home"
SELF = "self"

directions = ("n", "s", "e", "w")
look = ("look", "look ")
fight = ("fight ")
getItem = ("get", "get ")
options = ("look", "look ", "fight ", "get ")
entities = ('you', 'cleo', 'artie', 'wilk', 'ugly', 'nasty')
positive = ("y", "Y", "yes", "Yes", "YES", "ok", "okay", "k")
negative = ("n", "N", "no", "No", "NO", "negative", "x")
quit = ("q", "Q", "quit", "Quit", "QUIT", "stop", "STOP", "exit", "EXIT")

keys = [n, s, e, w, home, 'info', "players", "enemies"]

north_country_values = [ #	keys:
    'north_country', #nc_1	n
    'mountain',      #		s
    'north_country', #foothill	e
    'north_country', #cliff	w
    'north_country', # 		home
                       """
    The North Country

A thorny crossroads in the mountains. To the North are the snowy
peaks of distant mountains. To the South are jagged, grey mountain 
tops. To the East lay foothills. The trail to the West ventures 
across the face of a cliff.
                       """, #	info
    (north_country_players := (
    "north_country_players ", north_country_players)
    ), 			    #	"players"
    (north_country_enemies := (
    "north_country_enemies ", north_country_enemies)
    ),			    #	"enemies"
    ]

north_country = dict(zip(keys,north_country_values))

hill = {
    n: 'mountain',
    s: 'valley',
    e: 'beach',
    w: 'river',
    home: 'hill',
    'info':
    """
    High On A Hill

You are free as a bird. To the North you see a mountain range,
to the South a valley, to the East is beach, and to the West
you see a wide river.
    """,
    "players": (hill_players := (
    "hill_players ", hill_players)
    ),
    
    "enemies": (hill_enemies := (
    "hill_enemies ", hill_enemies)
    ),
    "items": (items := ['hat', 'scarf']),
    }
    
river = {
    e: 'hill',
    n: 'river_north',
    s: 'river',
    w: 'too_far',
    home: 'river',
    'info':
    """
    A Wide River

You find the bank of a wide, swift river. You cannot go
farther to the West. Turn back to the East, or follow
the bank to the North or South.
    """,
    "players": (river_players := (
    "river_players ", river_players)
    ),
    
    "enemies": (river_enemies := (
    "river_enemies ", river_enemies)
    ),
    "items": (items := []),
    }
    
mountain = {
    n: 'north_country',
    s: 'hill',
    e: 'mountain',
    w: 'mountain',
    home: 'mountain',
    'info':
    """
    In The Mountains

You climb into rugged mountains. If you go farther North
you will surely die. It is too cold for you there. You
can travel in the mountains choosing either East or West, 
or go to the South, returning to the hill country.
    """,
    
    "players": (mountain_players := (
    "mountain_players ", mountain_players)
    ),
    
    "enemies": (mountain_enemies := (
    "mountain_enemies ", mountain_enemies)
    ),
    "items": (items := []),
    }
    
valley = {
    n: 'hill',
    s: 'too_far',
    e: 'valley',
    w: 'valley',
    home: 'valley',
    'info':
    """
    A Shady Valley

You enter a cool, forested valley. To the North is the hill
country, and to either East or West are the pine trees and
singing birds of the valley. Do not dare to go any farther
South, it is not safe for travellers like yourself.
    """,
    "players": (valley_players := (
    "valley_players ", valley_players)
    ),
    
    "enemies": (valley_enemies := (
    "valley_enemies ", valley_enemies)
    ),
    "items": (items := []),
    }
    
beach = {
    n: 'beach',
    s: 'beach',
    e: 'too_far',
    w: 'hill',
    home: 'beach',
    'info':
    """
    Walk Along The Beach

You arrive at a long, lonesome beach. Your feet like the
crunch of the sand as you walk. To the East is a glittering
blue ocean. The water could be filled with sharks, you dare
not swim. You can return to the hill country if you go West, or
you can follow the beach to the North or South.
    """,
    "players": (beach_players := (
    "beach_players ", beach_players)
    ),
    
    "enemies": (beach_enemies := (
    "beach_enemies ", beach_enemies)
    ),
    "items": (items := []),
    }

#---------------RIVER NORTH SECTION-------------------
river_north = {
    e: 'too_far',
    n: 'river_north1',
    s: 'river',
    w: 'too_far',
    home: 'river_north',
    'info':
    """
    Walking Along The Bank Of A Wide River

You find the bank of a wide, swift river. You cannot go
farther to the West. It is too late to turn back. You must follow
the bank to the North or South.
    """,
    "players": (river_north_players := (
    "river_north_players ", river_north_players)
    ),
    
    "enemies": (river_north_enemies := (
    "river_north_enemies ", river_north_enemies)
    ),
    "items": (items := []),
    }

river_north1 = {
    e: 'too_far',
    n: 'river_north2',
    s: 'river_north',
    w: 'too_far',
    home: 'river_north1',
    'info':
    """
    Follow The River

You find the bank of a wide, swift river. You cannot go
farther to the West. You must follow the bank of the river, 
going either North or South.
    """,
    "players": (river_north1_players := (
    "river_north1_players ", river_north1_players)
    ),
    
    "enemies": (river_north1_enemies := (
    "river_north1_enemies ", river_north1_enemies)
    ),
    "items": (items := []),
    }

river_north2 = {
    e: 'too_far',
    n: 'too_far',
    s: 'river_north1',
    w: 'too_far',
    home: 'river_north2',
    'info':
    """
    Near The Village

You find the bank of a wide, swift river. You cannot go
farther to the West and the river becomes a waterfall; 
you cannot go North. You may follow the bank to the South.
But, to the East, you might see a town in the distance.
    """,
    "players": (river_north2_players := (
    "river_north2_players ", river_north2_players)
    ),
    
    "enemies": (river_north2_enemies := (
    "river_north2_enemies ", river_north2_enemies)
    ),
    "items": (items := []),
    }
#--------------END RIVER NORTH SECTION-----------------

#--------------START VILLAGE SECTION-------------------

#---------------END VILLAGE SECTION--------------------

#-------------------NO CRASH SECTION-------------------    
too_far = {
    n: 'too_far',
    s: 'too_far',
    e: 'too_far',
    w: 'too_far',
    home: 'too_far',
    'info':
    """
    Too Far

Sadly, you did not heed the warnings. You cannot turn back
now. You will have to choose: 'Q' to restart the game.
    """,
    "players": (too_far_players := (
    "too_far_players ", too_far_players)
    ),
    
    "enemies": (too_far_enemies := (
    "too_far_enemies ", too_far_enemies)
    ),
    }

def exit():
    print(
            """
        Ok, bye.
            """)
    sys.exit()
    
def nobody_by_that_name(a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data):
    print("    Nobody By That Name    ")
    time.sleep(1)
    lists(x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data)
    
def not_an_option(x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data):
    print(
        """\n    Not An Option    """)
    time.sleep(1)

    lists(x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data)

def move(x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data, new_input):
    new_location = (direction_data[new_input])
    new_data = eval(new_location)
    y = new_data.get('info')
    direction_data = new_data        
    info(x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data)
    
def get_new_item(x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data, new_input):
    
    if new_input == "get":
    
        it = direction_data.get('items')

        eq_location = list(it)

        format_eq_loc_list = " ".join(eq_location)    

        print("\nItems: ", format_eq_loc_list)
    
        get_item = input("What do you want to get?\n")
        
        if get_item in eq_location:
           
            get_me = list("get_" + get_item)
            get_me = "get_"
            getting = (get_me + get_item)
            now_get = item_dict.get(getting)

            
            item_slot = now_get[0]
            item_short = now_get[4]

            your_equipment[item_slot] = item_short
            del_item = item_short

    
            lists(x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data)
           
    else:

        not_an_option(x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data)

def fight_choice(x, y, a, f, g, k, pk, ready_p_list, enemy, opp_health, your_health, attack, defend, direction_data):
    fight_or_flight = input(
    "\nFight again, Yes, No or Quit?\n"
    ).lower()
    if fight_or_flight in positive:  	# 'Yes':
        fight(x, y, a, f, g, k, pk, ready_p_list, enemy, opp_health, your_health, attack, defend, direction_data)
    elif fight_or_flight in negative: 	#'No':

        lists(x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data)
    elif fight_or_flight in quit:
        exit()
    else:
        print("Sorry, I didn't get that.")
        fight_choice(x, y, a, f, g, k, pk, ready_p_list, enemy, opp_health, your_health, attack, defend, direction_data)

def fight(x, y, a, f, g, k, pk, ready_p_list, enemy, opp_health, your_health, attack, defend, direction_data):
    opponent = enemy[4]
    handle = enemy[5]
    p_killed = ''
    e_killed = ''
    if handle == 'player':
    
        p_killed = str(opponent)
        handle = ''
        
    elif handle == 'enemy':
    
        e_killed = str(opponent)
        handle = ''
        
    p_defend = int(-1)*abs(random.randint(3,7)*
    enemy[0] - random.randint(5,9)*defend)

    e_attack = abs(random.randint(5,9)*
    you[0] - random.randint(3,7)*enemy[1])
    
    print("\n")
    print(opponent, " total attack is ", e_attack)
    print("Your total defense is ", p_defend)
    

    e_damage = int(e_attack + p_defend)
    if e_damage <= 0:
        total_e_damage = 0
    elif e_damage >= 10:
        total_e_damage = 10
    else:
        total_e_damage = e_damage

    print("Damage is ", total_e_damage)
    
    p_health = your_health - total_e_damage
    your_health = p_health
    print("Your Health is ", p_health)
    if your_health <= 0:
         exit()

    #-----------------PLAYER ATTACK-----------------#

# your attack 3
# enemy defend 3
# 
    
    e_defend = int(-1)*abs(random.randint(5,9)*
    you[0] - random.randint(3,7)*enemy[1])

    p_attack = abs(random.randint(3,7)*
    enemy[0] - random.randint(5,9)*attack)
    
    print("\nYour total attack is ", p_attack)
    print(opponent, " total defense is ", e_defend)
    

    p_damage = int(p_attack + e_defend)
    if p_damage <= 0:
        total_p_damage = 0
    elif p_damage >= 10:
        total_p_damage = 10
    else:
        total_p_damage = p_damage

    print("Damage is ", total_p_damage)
    
    e_health = opp_health - total_p_damage
    opp_health = e_health
    print("Enemy Health is ", e_health)
    if opp_health <= 0:

        print("You have killed :", opponent)
        time.sleep(1)
        x = direction_data.get('info')
        print(x)
        if len(e_killed) > 1:
            k = e_killed
        elif len(p_killed) > 1:
            pk = p_killed        
            ready_p_list.remove(pk)

            pk = ''
        format_list = " ".join(ready_p_list)
        lists(x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data)
    else:
        fight_choice(x, y, a, f, g, k, pk, ready_p_list, enemy, opp_health, your_health, attack, defend, direction_data)

def look(x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data, new_input):
    if len(new_input) > 5:
        description = new_input[5:]
        if str(description) in entities:
            e_description = eval(description)
            print_look = e_description[2]
            print("\n")
            print(print_look)

            time.sleep(1)
            info(x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data)
        elif len(new_input) == 4:
            print(x)
            choices(x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data)
        else:
            nobody_by_that_name(x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data)

def choices(x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data):
    new_input = input(
    "\nChoose From: n, s, e, w, look, get, fight, or q: \n"
    ).lower()

    if "look " in new_input:
        look(x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data, new_input)
    elif new_input == "look":
        print(x)
        time.sleep(1)
        lists(x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data)
    elif "fight " in new_input:
        if len(new_input) > 6:
            fight_me = new_input[6:]
            
#------------EVALUATION OF CHOSEN OPPONENT TYPO-------------------

            if str(fight_me) in entities:
                if str(fight_me) != 'you':
                
                    for each in your_equipment:
                        modifiers = [f'get_{e}' for e in your_equipment]

                        bonus0 = modifiers[0]
                        bonus1 = modifiers[1]
                        bonus2 = modifiers[2]
                        bonus3 = modifiers[3]
                        bonus4 = modifiers[4]
                        
                        get_attk_bonus0 = []
                        get_attk_bonus0 = item_dict.get(bonus3)
                        attk_bonus0 = get_attk_bonus0[1]

                        
                        attk0 = int(attk_bonus0)
                        
                        get_def_bonus0 = []
                        get_def_bonus0 = item_dict.get(bonus0)
                        defend_bonus0 = get_def_bonus0[2]
                        
                        defend0 = int(defend_bonus0)
                        
                        get_def_bonus1 = []
                        get_def_bonus1 = item_dict.get(bonus1)
                        defend_bonus1 = get_def_bonus1[2]
                        
                        defend1 = int(defend_bonus1)
                        
                        get_def_bonus2 = []
                        get_def_bonus2 = item_dict.get(bonus2)
                        defend_bonus2 = get_def_bonus2[2]

                        
                        defend2 = int(defend_bonus2)

                        enemy = eval(fight_me)
                        opp_health = enemy[3]
                        your_health = you[3]
                        
                        print("\n")
                        print(enemy[0], "Enemy Attack")
                        print(enemy[1], "Enemy Defend")
                        print(opp_health, "Enemy Health\n")
    
                        base_attack = you[0]
                        base_defend = you[1]
                        
                        attack = int(base_attack) + attk0
                        defend = int(base_defend) + defend0 + defend1 + defend2

                        print(attack, "Your Attack")
                        print(defend, "Your Defend")
                        print(your_health, "Your Health")
                        fight_input = input("\n Proceed with Combat, Yes or No?\n")
                        if fight_input in positive:
                            fight(x, y, a, f, g, k, pk, ready_p_list, enemy, opp_health, your_health, attack, defend, direction_data)
                        elif fight_input in negative:
                            lists(x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data)
                        else:
                            print("Please answer with a Yes or a No")
                            lists(x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data)
                if str(fight_me) == 'you':
                     print('Do Not Fight Yourself')

                     lists(x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data)
    
            else:
                nobody_by_that_name(x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data)

    elif new_input in quit:
        exit()
#*-----------------------MOVE-SECTION----------------------*
    elif new_input in directions:

        move(x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data, new_input)

#*--------------------END-MOVE-SECTION----------------------*    
    elif new_input in getItem:
     
        
        get_new_item(x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data, new_input)
    
    else:
        not_an_option(x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data)

def lists(x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data):

    it = direction_data.get('items')
    eq_location = list(it)

    if del_item:
        eq_location.remove(del_item)
        format_eq_loc_list = " ".join(eq_location)
        print("\nItems: ", format_eq_loc_list)
        del_item = ''
    else:
        format_eq_loc_list = " ".join(eq_location)    
        print("\nItems: ", format_eq_loc_list)
    
    
    print_your_equipment = " ".join(your_equipment)
    
    print("\nYour equipment: ", print_your_equipment)
    
    if y:
        ready_p_list.remove(you[4])

    y = str(you)
    a = direction_data.get('home')
    b = str(a)
    location_home_players = "_players "
    c = (a + "" + location_home_players)

    e = direction_data.get('players')
    new_list = list(e)
    to_remove = str(c)
    new_list.remove(to_remove)
    new_list[0].append(you[4])

    ready_p_list = new_list.pop(0)

    location_home_enemies = "_enemies "
    g = (a + "" + location_home_enemies)
    f = direction_data.get('enemies')
    e_list = list(f)
    e_to_remove = str(g)
    e_list.remove(e_to_remove)
    
#    e_list[0].append("Stinky")

    ready_e_list = e_list.pop(0)
    
    if len(pk) > 1:

        ready_p_list.remove(pk)

        format_p_list = " ".join(ready_p_list)
        print("\nPlayers: ", format_p_list)
        pk = ''
    else:
        format_p_list = " ".join(ready_p_list)
        print("\nPlayers: ", format_p_list)

    if len(k) > 1:

        ready_e_list.remove(k)

        format_e_list = " ".join(ready_e_list)
        print("Enemies: ", format_e_list)
        k = ''
    else:
        format_e_list = " ".join(ready_e_list)
        print("Enemies: ", format_e_list)

    choices(x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data)
    
def info(x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data):    
    x = direction_data.get('info')
    print(x)
    lists(x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data)

def start():
    os.system('clear')
    y = ''
    x = ''
    a = ''
    f = []
    g = ''
    k = ''
    pk = ''
    ready_p_list = []
    equipment_values = []
    del_item = ''
    start_location = hill
    direction_data = start_location
#    print(len(list(cleo)))
    info(x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data)

start()
