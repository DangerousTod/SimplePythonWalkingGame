#!/usr/in/python
# -*- coding: utf-8 -*-

from network import Network
import playerfile
import oldplayerget

import sys
import os
import time
import random
import math

direction_data = {}
fresh_data = {}

sub_basement = {}
basement = {}
machinery = {}
posting = {}
engine = {}
tank = {}
wires = {}
observation_room = {}

keepers_quarters = {}
cabinet = {}
chest = {}
bunk = {}
lamp = {}
panel = {}
manual = {}
shelf = {}
home = {}
look = {}

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
lighthouseQuest = [False,False,False,False,False,False,False,False]
equipment_dict = {}

players = ['you']

# [0] is Attack, [1] is Defense, [2] is Description, [3] Health, [4] is Name, [5] is player or enemy
#you = [3, 4, "You Are A Hansome Young Lad", 100, 'You ', 'player', equipment_values, equipment_dict]
#your_equipment = ['hat', 'shirt', 'shoes', 'shortsword', 'potion']


hill_players = ['Cleo ', 'Artie ', 'Wilk ']

#--------------------PLAYER SECTION------------------------------#

cleo = [1, 4, 'A lovely young lady', 15, 'Cleo ', 'player', equipment_values,  equipment_dict, 'Cleo']
artie = [6, 6, 'Sir Artie will have none of it, non withstanding', 99, 'Artie ', 'player', equipment_values,  equipment_dict, 'Artie']
wilk = [5, 2, 'An all-around great guy', 66, 'Wilk ', 'player', equipment_values, equipment_dict, 'Wilk']

hill_enemies = ['Nasty ', 'Ugly ']

#---------------------ENEMY SECTION------------------------------#

# [0] is Attack, [1] is Defend, [2] is Description, [3] Health, [4] is Name, [5]is player or enemy
nasty = [2, 3, "What A Nasty Looking Dude", 60, "Nasty ", 'enemy', equipment_values, equipment_dict, 'Nasty']
ugly = [3, 2, "Wow, So much Ugliness", 20, "Ugly ", 'enemy', equipment_values, equipment_dict, 'Ugly'] # health was 70

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

get_wrench = []
get_wire = []
get_match = []

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

    "get_wire" : (wire := [5, 0, 0, 'A small bundle of userful wire','wire']),
    "get_match" : (match := [5, 0, 0, 'A tight-rolled paper tube','match']),
    "get_wrench" : (wrench := [4, 2, 2, 'A forged iron tool for twisting metal', 'wrench']),

    
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

sub_basement_players = []
sub_basement_enemies = []

basement_players = []
basement_enemies = []

machinery_players = []
machinery_enemies = []

posting_players = []
posting_enemies = []

engine_players = []
engine_enemies = []

tank_players = []
tank_enemies = []

wires_players = []
wires_enemies = []

observation_room_players = []
observation_room_enemies = []

#exit = {}

keepers_quarters_players = []
keepers_quarters_enemies = []

cabinet_players = []
cabinet_enemies = []

chest_players = []
chest_enemies = []

shelf_players = []
shelf_enemies = []

bunk_players = []
bunk_enemies = []

lamp_players = []
lamp_enemies = []

panel_players = []
panel_enemies = []

manual_players = []
manual_enemies = []

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

talk = ["hello", "Hi, How are you?", "nice day...", "Sure is!"]

n = "n"
s = "s"
e = "e"
w = "w"
up = "up"
down = "down"
exit = "exit"
lighthouse = "lighthouse"
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
#lighthouse elements
machinery = "machinery"
posting = "posting"
engine = "engine"
tank = "tank"
wires = "wires"
cabinet = "cabinet"
chest = "chest"
bunk = "bunk"
panel = "panel"
manual = "manual"
shelf = "shelf"
home = "home"
room = "room"
look = "look"


directions = ("home","room","n", "s", "e", "w","lighthouse","up","down","exit","machinery","posting","engine","tank","wires","cabinet","chest","bunk","panel","manual","shelf")
look = ("look", "look ")
fight = ("fight ")
getItem = ("get", "get ")
message = ("talk", "t", "say", "print")
options = ("look", "look ","talk", "fight ", "get ","up","down","look","exit")
entities = ['you', 'cleo', 'artie', 'wilk', 'ugly', 'nasty']
positive = ("y", "Y", "yes", "Yes", "YES", "ok", "okay", "k")
negative = ("n", "N", "no", "No", "NO", "negative", "x")
back = ("b", "B", "back", "BACK", "return")
quit = ("q", "Q", "quit", "Quit", "QUIT", "stop", "STOP")

keys = [n, s, e, w, home, 'info', "players", "enemies"]

#########################################################################





sub_basement = {
    up : 'basement',
    down : 'sub_basement',
    posting : 'posting',
    engine : 'engine',
    tank : 'tank',
    wires : 'wires',
    home : 'sub_basement',
    'info':
    """
    Sub Basement Of The Lighthouse

This is the storage space for machinery and fuel. An important
looking posting nearly covers an entire wall. The engine that
keeps the lighthouse lamp turning is here. A large fuel tank
sits beside it.

Directions:
up: Basement
    """,

    "players": (sub_basement := (
    "sub_basement_players ", sub_basement_players)
    ),
    
    "enemies": (sub_basement := (
    "sub_basement_enemies ", sub_basement_enemies)
    ),
    "items": (items := []),
    }

tank = {
    up : 'basement',
    down : 'sub_basement',
    room : 'sub_basement',
    home : 'tank',
    'info' :
    """
    Lighthouse Fuel Tank

A quick inspection of the fuel tank tells you that someone
stopped the flow of fuel to the engine. It has plenty of
fuel, luckily. If only you could twist the valve on the main
fuel line.

Directions:
Up: Basement
    """,
    
    "players": (tank := (
    "tank_players ", tank_players)
    ),
    
    "enemies": (tank := (
    "tank_enemies ", tank_enemies)
    ),
    "items": (items := []),
    
    }
    
engine = {
    up : 'basement',
    down : 'sub_basement',
    room : 'sub_basement',
    home : 'engine',
    'info' :
    """
    Lighthouse Engine

You have to marvel at the size of the engine in the
sub basement of the lighthouse. It might have only two
pistons, but the pistons are monsters. It is cold and
silent. Besides cutting off the flow of fuel, it looks
to you as if someone sabotaged the engine. You notice
cut wires.

Directions:
Up: Basement
    """,
    
    "players": (engine := (
    "engine_players ", engine_players)
    ),
    
    "enemies": (engine := (
    "engine_enemies ", engine_enemies)
    ),
    "items": (items := []),
    }
    
wires = {
    up : 'basement',
    down : 'sub_basement',
    room : 'sub_basement',
    home : 'wires',
    'info' :
    """
    Sabotage In The Lighthouse

You examine the wires. Sure enough, the engine still has
spark. But a few of the wires are missing.

Directions:
Up: Basement
    """,
    
    "players": (wires := (
    "wires_players ", wires_players)
    ),
    
    "enemies": (wires := (
    "wires_enemies ", wires_enemies)
    ),
    "items": (items := []),
    }


posting = {
    up : 'basement',
    down : 'sub_basement',
    room : 'sub_baement',
    home : 'posting',
    'info' :
    """
    The Writing On The Wall
    
Light match in burn tube BEFORE pumping fuel.
    """,
    
    "players": (posting := (
    "posting_players ", posting_players)
    ),
    
    "enemies": (posting := (
    "posting_enemies ", posting_enemies)
    ),
    "items": (items := []),
    }
basement = {
    up : 'observation_room',
    down : 'sub_basement',
    machinery : 'machinery',
    home : 'basement',
    'info':
    """
    Basement Of The Lighthouse

A storage space for the necessities of a full-time light
house keeper. In the corner is a pile of replacement 
parts for the machinery that should keep the Lighthouse
lit.

Directions:
Up: Observation Room or Down: Sub Basement
    """,
    
    "players": (basement := (
    "basement_players ", basement_players)
    ),
    
    "enemies": (basement := (
    "basement_enemies ", basement_enemies)
    ),
    "items": (items := []),
}


machinery = {
    up : 'basement',
    down : 'sub_basement',
    room : 'sub_basement',
    home : 'machinery',
    'info' :
    """
    Junk On The Floor

Replacement parts and broken bits from the inner-
workings of the Light House. Most of the items have
a small tag tied with a string. On one of the nearly-
legible tags you notice a strand of numbers similar
to those printed on a panel in the Observation Room.
    """,
    "players": (machinery := (
    "machinery_players ", machinery_players)
    ),
    
    "enemies": (machinery := (
    "machinery_enemies ", machinery_enemies)
    ),
    "items": (items := []),
    }

observation_room = {
    exit : 'mountain4u',
    up : 'keepers_quarters',
    down : 'basement',
    shelf : 'shelf',
    home : 'observation_room',
    'info':
    """
    Observation Room Of The Lighthouse
    
A window of thick glass gives a clear view of the sea
from the entry to the Lighthouse. Maps and log books
clutter the many shelves below the windows.

Directions:
Exit, Up: Keepers Quarters, or Down: Basement
    """,
    
    "players": (observation_room := (
    "observation_room_players ", observation_room_players)
    ),
    
    "enemies": (observation_room := (
    "observation_room_enemies ", observation_room_enemies)
    ),
    "items": (items := []),
    }

shelf = {
    up : 'keepers_quarters',
    down : 'basement',
    look : 'observation_room',
    room : 'observation_room',
    home : 'shelf',
    'info' : 
    """
    Searching The Shelves In The Observation Room

Log books and maps spill onto the floor. It may as well
be Greek for as much as you can make of it. But what is
this? A cigar-shaped paper cone?

    You found the match!
    Good Job!

Directions:
Up: Keepers Quarters or Down: Basement
    """,
    
    "players": (shelf := (
    "shelf_players ", shelf_players)
    ),
    
    "enemies": (shelf := (
    "shelf_enemies ", shelf_enemies)
    ),
    "items" : (items := ['match']),
    }

keepers_quarters = {
    up : 'lamp',
    down : 'observation_room',
    cabinet : 'cabinet',
    chest : 'chest',
    bunk : 'bunk',
    home : 'keepers_quarters',
    'info':
    """
    Keepers Quarters Of The Lighthouse

Small bunk and personal effects of a full-time lighthouse
keepers. Under a pile of clothes you notice large tool
chest. Cabinet doors line the opposite wall.

Directions:
Up: Lamp or Down: Observation Room
    """,
    "players": (keepers_quarters := (
    "keepers_quarters_players ", keepers_quarters_players)
    ),
    
    "enemies": (keepers_quarters := (
    "keepers_quarters_enemies ", keepers_quarters_enemies)
    ),
    "items": (items := []),
    }

cabinet = {
    up : 'lamp',
    down :'observation_room',
    look : 'keepers_quarters',
    home : 'cabinet',
    room : 'keepers_quarters',
    'info' :
    """
    Keeper's Cabinet

In the lighthouse keeper's cabinet you find dried fruit,
moldy crackers, and empty bottles.

Directions:
Up: Lamp Room or Down: Observation Room
    """,
    "players": (cabinet := (
    "cabinet_players ", cabinet_players)
    ),
    
    "enemies": (cabinet := (
    "cabinet_enemies ", cabinet_enemies)
    ),
    "items": (items := []),
    }
    
chest = {
    up : 'lamp',
    down :'observation_room',
    look : 'keepers_quarters',
    home : 'chest',
    room : 'keepers_quarters',
    'info' :
    """
    Keeper's Tool Chest

Although you expect a jackpost of tools and manuals,
the tool chest is practically empty.

Directions:
Up: Lamp Room or Down: Observation Room
    """,
    "players": (chest := (
    "chest_players ", chest_players)
    ),
    
    "enemies": (chest := (
    "chest_enemies ", chest_enemies)
    ),
    "items": (items := []),
    }
    
bunk = {
    up : 'lamp',
    down :'observation_room',
    look : 'keepers_quarters',
    home : 'bunk',
    room : 'keepers_quarters',
    'info' :
    """
    Under Keeper's Bunk

The keeper's bunk rests on something. Out of curiousity you pull
whatever it is into a position so as to look inside.

    Bingo!
    You found the wrench!

Directions:
Up: Lamp Room or Down: Observation Room
    """,
    "players": (bunk := (
    "bunk_players ", bunk_players)
    ),
    
    "enemies": (bunk := (
    "bunk_enemies ", bunk_enemies)
    ),
    "items" : (items := ['wrench']),
    }

lamp = {
    up : 'lamp',
    down : 'keepers_quarters',
    panel : 'panel',
    manual : 'manual',
    home : 'lamp',
    'info':
    """
    Lamp Room Of The Lighthouse

Top of the Lighthouse. The beacon must shine and rotate
slowly to warn ships of the dangerous rocks near the
coast. Youcan grab the chrome handles below the beacon to
turn it by hand, but it will stop turning after a few 
minutes if the engine is not running.
Many of the cabinets and panels stand empty and open,
probably damaged by storms over the years. One of the
panels has a latch. 

Directions:
Down: Keepers Quarters
    """,
    "players": (lamp := (
    "lamp_players ", lamp_players)
    ),
    
    "enemies": (lamp := (
    "lamp_enemies ", lamp_enemies)
    ),
    "items": (items := []),
    }
    
panel = {
    up : 'lamp',
    down : 'keepers_quarters',
    look : 'lamp',
    home : 'panel',
    room : 'lamp',
    'info' :
    """
    A Metal Panel In The Lamp Room

You unlatch the panel to find a manual on a chain beside
a bundle of wire.

    What luck!
    You are looking for wire to fix the engine!

Directions:
Down: Keeper's Quarters
    """,
    "players": (panel := (
    "panel_players ", panel_players)
    ),
    
    "enemies": (panel := (
    "panel_enemies ", panel_enemies)
    ),
    "items": (items := ['wire']),
    }

manual = {
    up : 'lamp',
    down : 'keepers_quarters',
    look : 'lamp',
    room : 'lamp',
    home : 'manual',
    'info' : 
    """
    A Light Keeper's Manual

You thumb through the keeper's manual. The word 'match'
catches your eye. According to the manual the match you
are in need of is much fatter than an every day match.
It must be more like a cigar than a match. You will know
it when you see it, you hope.

Directions:
Down: Keeper's Quarters
    """,
    "players": (manual := (
    "manual_players ", manual_players)
    ),
    
    "enemies": (manual := (
    "manual_enemies ", manual_enemies)
    ),
    "items": (items := []),
    }


#########################################################################

hill = {
    n: 'mountain7n',
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
#########################MOUNTAIN###############################################

mountain7n = {
    n: 'mountain6n',
    s: 'hill',
    e: 'mountain7o',
    w: 'mountain7m',
    home: 'mountain7n',
    'info':
    """
    Near The Hills

You climb into rugged mountains. You fear to go too far North,
you will surely die. It is too cold for you there. You
can travel in the mountains choosing either East or West, 
or go to the South, returning to the hill country.
    """,
    
    "players": (mountain7n_players := (
    "mountain7n_players ", mountain_players)
    ),
    
    "enemies": (mountain7n_enemies := (
    "mountain7n_enemies ", mountain_enemies)
    ),
    "items": (items := ['rock']),
    }
mountain7m = {
    n: 'mountain6m',
    s: 'mountain7m',
    e: 'mountain7n',
    w: 'mountain7m',
    home: 'mountain7m',
    'info':
    """
    Near The Hills

You climb into rugged mountains. You fear to go too far North,
you will surely die. It is too cold for you there. You
can travel in the mountains choosing either East or West, 
or go to the South, returning to the hill country.
    """,
    
    "players": (mountain7m_players := (
    "mountain7m_players ", mountain_players)
    ),
    
    "enemies": (mountain7m_enemies := (
    "mountain7m_enemies ", mountain_enemies)
    ),
    "items": (items := []),
    }
mountain7o = {
    n: 'mountain6o',
    s: 'mountain7o',
    e: 'mountain7o',
    w: 'mountain7n',
    home: 'mountain7o',
    'info':
    """
    Near The Hills

You climb into rugged mountains. You fear to go too far North,
you will surely die. It is too cold for you there. You
can travel in the mountains choosing either East or West, 
or go to the South, returning to the hill country.
    """,
    
    "players": (mountain7o_players := (
    "mountain7o_players ", mountain_players)
    ),
    
    "enemies": (mountain7o_enemies := (
    "mountain7o_enemies ", mountain_enemies)
    ),
    "items": (items := []),
    }
mountain6n = {
    n: 'mountain6n',
    s: 'mountain7n',
    e: 'mountain6o',
    w: 'mountain6m',
    home: 'mountain6n',
    'info':
    """
    Near The Hills

You climb into rugged mountains. You fear to go too far North,
you will surely die. It is too cold for you there. You
can travel in the mountains choosing either East or West, 
or go to the South, returning to the hill country.
    """,
    
    "players": (mountain6n_players := (
    "mountain6n_players ", mountain_players)
    ),
    
    "enemies": (mountain6n_enemies := (
    "mountain6n_enemies ", mountain_enemies)
    ),
    "items": (items := ['sword']),
    }
mountain6m = {
    n: 'mountain6m',
    s: 'mountain7m',
    e: 'mountain6n',
    w: 'mountain6m',
    home: 'mountain6m',
    'info':
    """
    Near The Hills

You climb into rugged mountains. You fear to go too far North,
you will surely die. It is too cold for you there. You
can travel in the mountains choosing either East or West, 
or go to the South, returning to the hill country.
    """,
    
    "players": (mountain6m_players := (
    "mountain6m_players ", mountain_players)
    ),
    
    "enemies": (mountain6m_enemies := (
    "mountain6m_enemies ", mountain_enemies)
    ),
    "items": (items := []),
    }
mountain6o = {
    n: 'mountain6o',
    s: 'mountain7o',
    e: 'mountain6p',
    w: 'mountain6n',
    home: 'mountain6o',
    'info':
    """
    Near The Hills

You climb into rugged mountains. You fear to go too far North,
you will surely die. It is too cold for you there. You
can travel in the mountains choosing either East or West, 
or go to the South, returning to the hill country.
    """,
    
    "players": (mountain6o_players := (
    "mountain6o_players ", mountain_players)
    ),
    
    "enemies": (mountain6o_enemies := (
    "mountain6o_enemies ", mountain_enemies)
    ),
    "items": (items := []),
    }
#######################THE#PASS#######################################

mountain6p = {
    n: 'mountain5p',
    s: 'mountain6p',
    e: 'mountain6q',
    w: 'mountain6o',
    home: 'mountain6p',
    'info':
    """
    In The Mountains

You climb into rugged mountains. You fear to go too far North,
you will surely die. It is too cold for you there. You
can travel in the mountains choosing either East or West, 
or go to the South, returning to the hill country.
    """,
    
    "players": (mountain6p_players := (
    "mountain6p_players ", mountain_players)
    ),
    
    "enemies": (mountain6p_enemies := (
    "mountain6p_enemies ", mountain_enemies)
    ),
    "items": (items := []),
    }
mountain6q = {
    n: 'mountain5q',
    s: 'mountain6q',
    e: 'mountain6r',
    w: 'mountain6p',
    home: 'mountain6q',
    'info':
    """
    In The Mountains

You climb into rugged mountains. You fear to go too far North,
you will surely die. It is too cold for you there. You
can travel in the mountains choosing either East or West, 
or go to the South, returning to the hill country.
    """,
    
    "players": (mountain6q_players := (
    "mountain6q_players ", mountain_players)
    ),
    
    "enemies": (mountain6q_enemies := (
    "mountain6q_enemies ", mountain_enemies)
    ),
    "items": (items := []),
    }
mountain6r = {
    n: 'mountain5r',
    s: 'mountain6r',
    e: 'mountain6r',
    w: 'mountain6q',
    home: 'mountain6r',
    'info':
    """
    In The Mountains

You climb into rugged mountains. You fear to go too far North,
you will surely die. It is too cold for you there. You
can travel in the mountains choosing either East or West, 
or go to the South, returning to the hill country.
    """,
    
    "players": (mountain6r_players := (
    "mountain6r_players ", mountain_players)
    ),
    
    "enemies": (mountain6r_enemies := (
    "mountain6r_enemies ", mountain_enemies)
    ),
    "items": (items := []),
    }
mountain5p = {
    n: 'mountain4p',
    s: 'mountain6p',
    e: 'mountain5q',
    w: 'too_far',
    home: 'mountain5p',
    'info':
    """
    In The Mountains

You climb into rugged mountains. You fear to go too far North,
you will surely die. It is too cold for you there. You
can travel in the mountains choosing either East or West, 
or go to the South, returning to the hill country.
    """,
    
    "players": (mountain5p_players := (
    "mountain5p_players ", mountain_players)
    ),
    
    "enemies": (mountain5p_enemies := (
    "mountain5p_enemies ", mountain_enemies)
    ),
    "items": (items := []),
    }
mountain5q = {
    n: 'mountain4q',
    s: 'mountain6q',
    e: 'mountain5r',
    w: 'mountain5p',
    home: 'mountain5q',
    'info':
    """
    In The Mountains

You climb into rugged mountains. You fear to go too far North,
you will surely die. It is too cold for you there. You
can travel in the mountains choosing either East or West, 
or go to the South, returning to the hill country.
    """,
    
    "players": (mountain5q_players := (
    "mountain5q_players ", mountain_players)
    ),
    
    "enemies": (mountain5q_enemies := (
    "mountain5q_enemies ", mountain_enemies)
    ),
    "items": (items := []),
    }
mountain5r = {
    n: 'mountain4r',
    s: 'mountain6r',
    e: 'mountain5rr',
    w: 'mountain5q',
    home: 'mountain5r',
    'info':
    """
    In The Mountains

You climb into rugged mountains. You fear to go too far North,
you will surely die. It is too cold for you there. You
can travel in the mountains choosing either East or West, 
or go to the South, returning to the hill country.
    """,
    
    "players": (mountain5r_players := (
    "mountain5r_players ", mountain_players)
    ),
    
    "enemies": (mountain5r_enemies := (
    "mountain5r_enemies ", mountain_enemies)
    ),
    "items": (items := []),
    }
mountain5rr = {
    n: 'too_far',
    s: 'too_far',
    e: 'mountain5s',
    w: 'mountain5r',
    home: 'mountain5rr',
    'info':
    """
    A High Mountain Pass

You climb into rugged mountains. You fear to go too far North,
you will surely die. It is too cold for you there. You
can travel in the mountains choosing either East or West, 
or go to the South, returning to the hill country.
    """,
    
    "players": (mountain5rr_players := (
    "mountain5rr_players ", mountain_players)
    ),
    
    "enemies": (mountain5rr_enemies := (
    "mountain5rr_enemies ", mountain_enemies)
    ),
    "items": (items := []),
    }
#######################FOREST########################################
mountain5s = {
    n: 'mountain4s',
    s: 'mountain6s',
    e: 'mountain5t',
    w: 'mountain5rr',
    home: 'mountain5s',
    'info':
    """
    A Snowy Forest

The mountainside is blanketed by pine trees and knotty old cedars.
You could wander for hours in icy timber in the mountains. Deer, 
elk, and wolves roam about. You can in any direction, but don't get
lost.
    """,
    
    "players": (mountain5s_players := (
    "mountain5s_players ", mountain_players)
    ),
    
    "enemies": (mountain5s_enemies := (
    "mountain5s_enemies ", mountain_enemies)
    ),
    "items": (items := []),
    }
mountain5t = {
    n: 'mountain4t',
    s: 'mountain6t',
    e: 'mountain5u',
    w: 'mountain5s',
    home: 'mountain5t',
    'info':
    """
    A Snowy Forest

The mountainside is blanketed by pine trees and knotty old cedars.
You could wander for hours in icy timber in the mountains. Deer, 
elk, and wolves roam about. You can in any direction, but don't get
lost.
    """,
    
    "players": (mountain5t_players := (
    "mountain5t_players ", mountain_players)
    ),
    
    "enemies": (mountain5t_enemies := (
    "mountain5t_enemies ", mountain_enemies)
    ),
    "items": (items := []),
    }
mountain5u = {
    n: 'mountain4u',
    s: 'mountain6u',
    e: 'mountain5u',
    w: 'mountain5t',
    home: 'mountain5u',
    'info':
    """
    A Snowy Forest

The mountainside is blanketed by pine trees and knotty old cedars.
You could wander for hours in icy timber in the mountains. Deer, 
elk, and wolves roam about. You can in any direction, but don't get
lost.
    """,
    
    "players": (mountain5u_players := (
    "mountain5u_players ", mountain_players)
    ),
    
    "enemies": (mountain5u_enemies := (
    "mountain5u_enemies ", mountain_enemies)
    ),
    "items": (items := []),
    }

mountain6s = {
    n: 'mountain5s',
    s: 'mountain6s',
    e: 'mountain6t',
    w: 'mountain6s',
    home: 'mountain6s',
    'info':
    """
    A Snowy Forest

The mountainside is blanketed by pine trees and knotty old cedars.
You could wander for hours in icy timber in the mountains. Deer, 
elk, and wolves roam about. You can in any direction, but don't get
lost.
    """,
    
    "players": (mountain6s_players := (
    "mountain6s_players ", mountain_players)
    ),
    
    "enemies": (mountain6s_enemies := (
    "mountain6s_enemies ", mountain_enemies)
    ),
    "items": (items := []),
    }
mountain6t = {
    n: 'mountain5t',
    s: 'mountain6t',
    e: 'mountain6u',
    w: 'mountain6s',
    home: 'mountain6t',
    'info':
    """
    A Snowy Forest

The mountainside is blanketed by pine trees and knotty old cedars.
You could wander for hours in icy timber in the mountains. Deer, 
elk, and wolves roam about. You can in any direction, but don't get
lost.
    """,
    
    "players": (mountain6t_players := (
    "mountain6t_players ", mountain_players)
    ),
    
    "enemies": (mountain6t_enemies := (
    "mountain6t_enemies ", mountain_enemies)
    ),
    "items": (items := []),
    }
mountain6u = {
    n: 'mountain5u',
    s: 'mountain6u',
    e: 'mountain6w',
    w: 'mountain6t',
    home: 'mountain6u',
    'info':
    """
    A Snowy Forest

The mountainside is blanketed by pine trees and knotty old cedars.
You could wander for hours in icy timber in the mountains. Deer, 
elk, and wolves roam about. You can in any direction, but don't get
lost.
    """,
    
    "players": (mountain6u_players := (
    "mountain6u_players ", mountain_players)
    ),
    
    "enemies": (mountain6u_enemies := (
    "mountain6u_enemies ", mountain_enemies)
    ),
    "items": (items := []),
    }
mountain6v = {
    n: 'mountain6v',
    s: 'mountain6v',
    e: 'mountain6w',
    w: 'mountain6u',
    home: 'mountain6v',
    'info':
    """
    A Snowy Forest

The mountainside is blanketed by pine trees and knotty old cedars.
You could wander for hours in icy timber in the mountains. Deer, 
elk, and wolves roam about. You can in any direction, but don't get
lost.
    """,
    
    "players": (mountain6v_players := (
    "mountain6v_players ", mountain_players)
    ),
    
    "enemies": (mountain6v_enemies := (
    "mountain6v_enemies ", mountain_enemies)
    ),
    "items": (items := []),
    }
mountain6w = {
    n: 'mountain6w',
    s: 'mountain6w',
    e: 'mountain6x',
    w: 'mountain6v',
    home: 'mountain6w',
    'info':
    """
    A Snowy Forest

The mountainside is blanketed by pine trees and knotty old cedars.
You could wander for hours in icy timber in the mountains. Deer, 
elk, and wolves roam about. You can in any direction, but don't get
lost.
    """,
    
    "players": (mountain6w_players := (
    "mountain6w_players ", mountain_players)
    ),
    
    "enemies": (mountain6w_enemies := (
    "mountain6w_enemies ", mountain_enemies)
    ),
    "items": (items := []),
    }
mountain6x = {
    n: 'mountain6x',
    s: 'mountain6x',
    e: 'mountain6x',
    w: 'mountain6w',
    home: 'mountain6x',
    'info':
    """
    A Snowy Forest

The mountainside is blanketed by pine trees and knotty old cedars.
You could wander for hours in icy timber in the mountains. Deer, 
elk, and wolves roam about. You can in any direction, but don't get
lost.
    """,
    
    "players": (mountain6x_players := (
    "mountain6x_players ", mountain_players)
    ),
    
    "enemies": (mountain6x_enemies := (
    "mountain6x_enemies ", mountain_enemies)
    ),
    "items": (items := []),
    }

##########################CLIMB#####################################

mountain4p = {
    n: 'too_far',
    s: 'mountain5p',
    e: 'mountain4q',
    w: 'mountain4o',
    home: 'mountain4p',
    'info':
    """
    Climbing A Mountain

You found a dangerous trail that leads toward the highest of
the mountain peaks. Icy slopes to the north and south give
you very little room for error.
    """,
    
    "players": (mountain4p_players := (
    "mountain4p_players ", mountain_players)
    ),
    
    "enemies": (mountain4p_enemies := (
    "mountain4p_enemies ", mountain_enemies)
    ),
    "items": (items := []),
    }
mountain4q = {
    n: 'too_far',
    s: 'mountain5q',
    e: 'mountain4r',
    w: 'mountain4p',
    home: 'mountain4q',
    'info':
    """
    Climbing A Mountain

You found a dangerous trail that leads toward the highest of
the mountain peaks. Icy slopes to the north and south give
you very little room for error.
    """,
    
    "players": (mountain4q_players := (
    "mountain4q_players ", mountain_players)
    ),
    
    "enemies": (mountain4q_enemies := (
    "mountain4q_enemies ", mountain_enemies)
    ),
    "items": (items := []),
    }
mountain4r = {
    n: 'too_far',
    s: 'mountain5r',#######################################
    e: 'too_far',
    w: 'mountain4q',
    home: 'mountain4r',
    'info':
    """
    Climbing A Mountain

You found a dangerous trail that leads toward the highest of
the mountain peaks. Icy slopes to the north and south give
you very little room for error.
    """,
    
    "players": (mountain4r_players := (
    "mountain4r_players ", mountain_players)
    ),
    
    "enemies": (mountain4r_enemies := (
    "mountain4r_enemies ", mountain_enemies)
    ),
    "items": (items := []),
    }
mountain4m = {
    n: 'mountain3c',
    s: 'too_far',
    e: 'mountain4n',
    w: 'too_far',
    home: 'mountain4m',
    'info':
    """
    Climbing A Mountain

You found a dangerous trail that leads toward the highest of
the mountain peaks. Icy slopes to the north and south give
you very little room for error. Though your eyes are blinded
by the glare from the ice, you think the path turns to the
North.
    """,
    
    "players": (mountain4m_players := (
    "mountain4m_players ", mountain_players)
    ),
    
    "enemies": (mountain4m_enemies := (
    "mountain4m_enemies ", mountain_enemies)
    ),
    "items": (items := []),
    }
mountain4n = {
    n: 'too_far',
    s: 'too_far',
    e: 'mountain4o',
    w: 'mountain4m',
    home: 'mountain4n',
    'info':
    """
    Climbing A Mountain

You found a dangerous trail that leads toward the highest of
the mountain peaks. Icy slopes to the north and south give
you very little room for error.
    """,
    
    "players": (mountain4n_players := (
    "mountain4n_players ", mountain_players)
    ),
    
    "enemies": (mountain4n_enemies := (
    "mountain4n_enemies ", mountain_enemies)
    ),
    "items": (items := []),
    }
mountain4o = {
    n: 'too_far',
    s: 'too_far',
    e: 'mountain4p',
    w: 'mountain4n',
    home: 'mountain4o',
    'info':
    """
    Climbing A Mountain

You found a dangerous trail that leads toward the highest of
the mountain peaks. Icy slopes to the north and south give
you very little room for error.
    """,
    
    "players": (mountain4o_players := (
    "mountain4o_players ", mountain_players)
    ),
    
    "enemies": (mountain4o_enemies := (
    "mountain4o_enemies ", mountain_enemies)
    ),
    "items": (items := []),
    }
#########################THE#PEAK##############################
mountain3c = {
    n: 'mountain2c',
    s: 'mountain4m',
    e: 'too_far',
    w: 'mountain3c',
    home: 'mountain3c',
    'info':
    """
    On A Mountain Top

From the peak of the mountain the world is a priceless vista.
Mountains and forest spread out beneath you. A river winds 
through unexplored lands and an Ocean waits for the most courageous
and brave. You are on the South East face of the peak. Be careful.
The trail you climbed to reach the mountain top is to the South.
    """,
    
    "players": (mountain3c_players := (
    "mountain3c_players ", mountain_players)
    ),
    
    "enemies": (mountain3c_enemies := (
    "mountain3c_enemies ", mountain_enemies)
    ),
    "items": (items := []),
    }
mountain3b = {
    n: 'mountain2b',
    s: 'too_far',
    e: 'mountain3c',
    w: 'too_far',
    home: 'mountain3b',
    'info':
    """
    On A Mountain Top

From the peak of the mountain the world is a priceless vista.
Mountains and forest spread out beneath you. A river winds 
through unexplored lands and an Ocean waits for the most courageous
and brave. You are on the South West face of the peak. Be careful.
    """,
    
    "players": (mountain3b_players := (
    "mountain3b_players ", mountain_players)
    ),
    
    "enemies": (mountain3b_enemies := (
    "mountain3b_enemies ", mountain_enemies)
    ),
    "items": (items := []),
    }
mountain2c = {
    n: 'too_far',
    s: 'mountain3c',
    e: 'too_far',
    w: 'mountain2b',
    home: 'mountain2c',
    'info':
    """
    On A Mountain Top

From the peak of the mountain the world is a priceless vista.
Mountains and forest spread out beneath you. A river winds 
through unexplored lands and an Ocean waits for the most courageous
and brave. You are on the North East face of the peak. Be careful.
    """,
    
    "players": (mountain2c_players := (
    "mountain2c_players ", mountain_players)
    ),
    
    "enemies": (mountain2c_enemies := (
    "mountain2c_enemies ", mountain_enemies)
    ),
    "items": (items := []),
    }
mountain2b = {
    n: 'too_far',
    s: 'mountain3b',
    e: 'mountain3c',
    w: 'too_far',
    home: 'mountain2b',
    'info':
    """
    On A Mountain Top

From the peak of the mountain the world is a priceless vista.
Mountains and forest spread out beneath you. A river winds 
through unexplored lands and an Ocean waits for the most courageous
and brave. You are on the North West face of the peak. Be careful.
    """,
    
    "players": (mountain2b_players := (
    "mountain2b_players ", mountain_players)
    ),
    
    "enemies": (mountain2b_enemies := (
    "mountain2b_enemies ", mountain_enemies)
    ),
    "items": (items := []),
    }
#####################WINDY#FACE################################
mountain4s = {
    n: 'too_far',
    s: 'mountain5s',
    e: 'mountain4t',
    w: 'too_far',
    home: 'mountain4s',
    'info':
    """
    Windy Ledge

The alpine forest opens up to reveal a cliff. You would have fallen
at least a thousand feet if you had taken one more step. It looks
like the only safe path is to the South, back into the evergreen
forest.
    """,
    
    "players": (mountain4s_players := (
    "mountain4s_players ", mountain_players)
    ),
    
    "enemies": (mountain4s_enemies := (
    "mountain4s_enemies ", mountain_enemies)
    ),
    "items": (items := []),
    }
mountain4t = {
    n: 'too_far',
    s: 'mountain5t',
    e: 'mountain4u',
    w: 'mountain4s',
    home: 'mountain4t',
    'info':
    """
    Windy Ledge

The alpine forest opens up to reveal a cliff. You would have fallen
at least a thousand feet if you had taken one more step. It looks
like the only safe path is to the South, back into the evergreen
forest.
    """,
    
    "players": (mountain4t_players := (
    "mountain4t_players ", mountain_players)
    ),
    
    "enemies": (mountain4t_enemies := (
    "mountain4t_enemies ", mountain_enemies)
    ),
    "items": (items := []),
    }
mountain4u = {
    n: 'too_far',
    s: 'mountain5u',
    e: 'too_far',
    w: 'mountain4t',
    lighthouse: 'observation_room',
    home: 'mountain4u',
    'info':
    """
    Windy Ledge

The alpine forest opens up to reveal a cliff. You would have fallen
at least a thousand feet if you had taken one more step. It looks
like the only safe path is to the South, back into the evergreen
forest, or you could try entering the lighthouse. If you listen close
you might hear the roaring of the sea.
    """,
    
    "players": (mountain4u_players := (
    "mountain4u_players ", mountain_players)
    ),
    
    "enemies": (mountain4u_enemies := (
    "mountain4u_enemies ", mountain_enemies)
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
#    n: exit(),
#    s: exit(),
#    e: exit(),
#    w: exit(),
    home: 'too_far',
    'info':
    """
    Too Far

Sadly, you did not heed the warnings. You cannot turn back
now. You will have to restart the game.
    """,
    "players": (too_far_players := (
    "too_far_players ", too_far_players)
    ),
    
    "enemies": (too_far_enemies := (
    "too_far_enemies ", too_far_enemies)
    ),
    "items": (items := []),
    }

#you = [3, 4, "You Are A Hansome Young Lad", 100, 'You ', 'player', equipment_values, equipment_dict, "yourname"]
#your_equipment = ['hat', 'shirt', 'shoes', 'shortsword', 'potion']

def do_exit():
     
        print(
            """
        Ok, bye.
            """)
        sys.exit()

def exit(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest):
    get_save_choice = input('\nYes For Save Your Player.\n')
    
#    if len(you) < 9:
#        print('No Character Found')
#        do_exit()
        
    if get_save_choice in negative:
        do_exit()
        
    elif get_save_choice in positive:
        print(lighthouseQuest)
        print(you)
        print(your_equipment)
        playerfile.playerlist_write(you, your_equipment, lighthouseQuest)
    
    else:
        print("Choice Unrecognized\n")
        exit(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest)
        

    
def nobody_by_that_name(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest):
    print("    Nobody By That Name    ")
    time.sleep(1)
    lists(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest)
    
def not_an_option(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest):
    print(
        """\n    Not An Option    """)
    time.sleep(1)

    lists(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest)

def talking(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest):
    
    new_message = input("\nWhat do you want to say? (Quit or Back)\n").lower()
    if new_message in quit:
        exit(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest)
    elif new_message in back:
        lists(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest)
    elif len(new_message) == '':
        print("Speak up!")
        lists(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest)

    else:

        talk.append(new_message)
        i_am = you[4]
        
        talk_stream = talk[-1]
        print("\nTalk Channel: " + i_am + ", "+ talk_stream)
        time.sleep(1)
        talking(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest)

def move(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest, new_input):

    try:
        new_location = (direction_data[new_input])

    except KeyError:
        print("""
        \n    Option Not Found.\n
        """)
        time.sleep(1)
        os.system("clear")
        choices(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest)
    else:
 #       print("direction_data move: ", direction_data)
        new_location = (direction_data[new_input])
        new_data = eval(new_location)

        x = new_data.get('info')
        direction_data = new_data        
        info(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest)

def get_new_item(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest, new_input):
    
    if new_input == "get":
    
        it = direction_data.get('items')

        eq_location = list(it)

        format_eq_loc_list = " ".join(eq_location)    

        print("\nItems: ", format_eq_loc_list)
    
        get_item = input("What do you want to get?\n").lower()
        
        if get_item in eq_location:
           
            get_me = list("get_" + get_item)
            get_me = "get_"
            getting = (get_me + get_item)
            now_get = item_dict.get(getting)

            
            item_slot = now_get[0]
            item_short = now_get[4]

            your_equipment[item_slot] = item_short
            del_item = item_short

    
            lists(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest)
           
        else:
            not_an_option(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest)

def fight_choice(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, enemy, opp_health, your_health, attack, defend, direction_data):
    fight_or_flight = input(
    "\nFight again, Yes, No or Quit?\n"
    ).lower()
    if fight_or_flight in positive:  	# 'Yes':
        fight(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, enemy, opp_health, your_health, attack, defend, direction_data)
    elif fight_or_flight in negative: 	#'No':

        lists(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest)
    elif fight_or_flight in quit:
        exit(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest)
    else:
        print("Sorry, I didn't get that.")
        fight_choice(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, enemy, opp_health, your_health, attack, defend, direction_data)

def fight(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, enemy, opp_health, your_health, attack, defend, direction_data):
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
         exit(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest)

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
        lists(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest)
    else:
        fight_choice(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, enemy, opp_health, your_health, attack, defend, direction_data)

def look(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest, new_input):
    if len(new_input) > 5:
        os.system('clear')
#        print(ready_p_list)
        description = new_input[5:]
        if str(description) in entities:
            e_description = eval(description)
            print_look = e_description[2]
            print("\n")
            
            print(print_look)

            time.sleep(1)
            lists(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest)

        elif len(new_input) == 4:
            os.system('clear')
            print(x)
            choices(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest)
        else:
            nobody_by_that_name(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest)

def choices(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest):
#    print("direction data choices before eval: ", direction_data)
    new_input = input(
    "\nChoose From: n, s, e, w, up, down, look, get, fight, talk, room, or q: \n"
    ).lower()

    if "look " in new_input:
        look(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest, new_input)
    elif new_input == "look":
        print(x)
        time.sleep(1)
        lists(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest)
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
                        
                        if get_attk_bonus0 is not None:                        
                            attk_bonus0 = get_attk_bonus0[1]
                        else:
                            attk_bonus0 = 0
                        attk0 = int(attk_bonus0)
                        
                        get_def_bonus0 = []
                        get_def_bonus0 = item_dict.get(bonus0)

                        if get_def_bonus0 is not None:
                            defend_bonus0 = get_def_bonus0[2]
                        else:
                            defend_bonus0 = 0
                        defend0 = int(defend_bonus0)
                        
                        get_def_bonus1 = []
                        get_def_bonus1 = item_dict.get(bonus1)
                        
                        if get_def_bonus1 is not None:                        
                            defend_bonus1 = get_def_bonus1[2]
                        else:
                            defend_bonus1 = 0
                        defend1 = int(defend_bonus1)
                        
                        get_def_bonus2 = []
                        get_def_bonus2 = item_dict.get(bonus2)
                        if get_def_bonus2 is not None:                        
                            defend_bonus2 = get_def_bonus2[2]
                        else:
                            defend_bonus2 = 0
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
                        fight_input = input("\n Proceed with Combat, Yes or No?\n").lower()
                        if fight_input in positive:
                            fight(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, enemy, opp_health, your_health, attack, defend, direction_data)
                        elif fight_input in negative:
                            lists(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest)
                        else:
                            print("Please answer with a Yes or a No")
                            lists(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest)
                if str(fight_me) == 'you':
                     print('Do Not Fight Yourself')

                     lists(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest)
    
            else:
                nobody_by_that_name(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest)

    elif new_input in quit:
        exit(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest)
#*-----------------------MOVE-SECTION----------------------*
    elif new_input in directions:

        move(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest, new_input)

#*--------------------END-MOVE-SECTION----------------------*    
    elif new_input in getItem:
     
        
        get_new_item(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest, new_input)
        
    elif new_input in message:
        talking(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest)
    
    else:
        not_an_option(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest)

def lists(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest):

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
#        print(ready_p_list)

    y = str(you)
#    print(y)

    a = direction_data.get('home')
    b = str(a)

    location_home_players = "_players "
    c = (a + "" + location_home_players)

    e = direction_data.get('players')

    new_list = list(e)
#    print(new_list)
    to_remove = str(c)
#    print(to_remove)

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

    choices(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest)
    
def info(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest):    
    x = direction_data.get('info')
    os.system('clear')
    print(x)
    lists(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest)
    
def save_start(you, your_equipment, lighthouseQuest):
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
#    lighthouseQuest = [False,False,False,False,False,False,False,False]
    del_item = ''
    start_location = hill
    direction_data = start_location
    info(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest)

def start(you, your_equipment):
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
    lighthouseQuest = [False,False,False,False,False,False,False,False]
    del_item = ''
    start_location = hill
    direction_data = start_location
#    print(len(list(cleo)))
    info(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest)

def make_player():
    new_player = input("\nYes: Make A New Player\nNo: Saved Player List\n").lower()
    if new_player in negative:
        print("\nChoose a player from this list: \n")
        oldplayerget.playerlist_read()
    elif new_player in positive:
        make_new_player()

def make_new_player():  
    make_player = input("\nNew Player!\nType out your name:\n")
    if len(make_player) < 15:
        print('\nOK, We will start fresh\n')
        time.sleep(1)
        print("\nHello, " + make_player + " and Welcome!\nDon't worry, this will be painless...")
        time.sleep(1)
        entities.append(make_player)
#        print(entities)
        get_new_attack(make_player)
    elif make_player in quit:
        exit(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest)
    else:
        print("\nName exceed maximum length\n")
        make_new_player()

you = []
your_equipment = []
lighhouseQuest = [False,False,False,False,False,False,False,False]

def get_new_attack(make_player):
    A_Range = range(2, 8)
    print("\nchoosing attack number\n")
    new_attack = input("Choose a number between 2 and 7\n").lower()

    if new_attack in quit:
        do_exit()
    
    elif int(new_attack) in A_Range:
        attack_int = int(new_attack)
        you.append(attack_int)
        get_new_defense(make_player, attack_int)

    else:
        get_new_attack(make_player)

def get_new_defense(make_player, attack_int):
    D_Range = range(2, 8)
    new_defend = input("Choose a number between 2 and 7\n").lower()
    if new_defend in quit:
        do_exit()
    
    elif int(new_defend) in D_Range:
        defend_int = int(new_defend)
        you.append(defend_int)
        get_new_description(make_player, attack_int, defend_int)
    else:
        get_new_defense(make_player, attack_int)

def get_new_description(make_player, attack_int, defend_int):
    new_description = input("\nWhat do you look like?\n").lower()
    if len(new_description) <= 41:
        my_description = new_description
        you.append(my_description)
        get_new_health(make_player, attack_int, defend_int, my_description)
    else:
        print("description too long\n")
        get_new_description(make_player, attack_int, defend_int)
    
def walkerrun(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest):
    os.system('clear')
    start_location = mountain4u
    direction_data = start_location
    y = ''
    x = direction_data.get('info')
    a = ''
    f = []
    g = ''
    k = ''
    pk = ''
    ready_p_list = []
    equipment_values = []
    
    del_item = ''
    while run:
        choices(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest)

    if new_description in quit:
        exit(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest)
    elif len(str(new_description)) < 41:
        my_description = str(new_description)
        you.append(my_description)
        get_new_health(make_player, attack_int, defend_int, my_description)
    
    else:
        print("\nTry again, perhaps with fewer characters\n")
        time.sleep(1)
        get_new_description(make_player, attack_int, defend_int)



def get_new_health(make_player, attack_int, defend_int, my_description):
    Range = range(75, 126)
    new_health = input("\nChoose a number between 75 and 125\n").lower()
    if new_health in quit:
        exit(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest)
    elif int(new_health) in Range:
        my_health = int(new_health)
        you.append(my_health)
        attribute_list = ["You", "player", equipment_values, equipment_dict]

        you.extend(attribute_list)
        you.append(make_player)

#your_equipment = ['hat', 'shirt', 'shoes', 'shortsword', 'potion']
        
        get_new_eq(you)
    
    else:
        get_new_health(make_player, attack_int, defend_int, my_description)

def get_new_eq(you):
    your_equipment = []
    head = ['hat','scarf','helmet']
    new_head = input("\nChoose one from the following: hat, scarf, helmet\n").lower()
    if new_head in head:
        your_equipment.append(new_head)
    elif new_head in quit:
        print('Cannot Save Unfinished Character')
        time.sleep(1)
        do_exit()
    else:
        print("\nSorry, not available\n")
        your_equipment.append(' ')

    chest = ['shirt','coat']
    new_chest = input("\nChoose from the following: shirt, or coat\n").lower()
    if new_chest in chest:
        your_equipment.append(new_chest)
    elif new_chest in quit:
        print('Cannot Save Unfinished Player')
        do_exit()
    else:
        print("\nSorry, not available\n")
        your_equipment.append(' ')

    feet = [ 'slippers','sandals','shoes','boots']
    new_feet = input("\nChoose from the following: slippers, sandals, shoes, or boots\n").lower()
    if new_feet in feet:
        your_equipment.append(new_feet)
    elif new_feet in quit:
        print('Cannot Save Unfinished Player')
        time.sleep(1)
        do_exit()
    else:
        print("\nSorry, not available\n")
        your_equipment.append(' ')

    hand = ['rock','dagger','shortsword','sword']
    new_hand = input("\nChoose from the following: rock, dagger, shortsword, sword\n").lower()
    if new_hand in hand:
        your_equipment.append(new_hand)
    elif new_hand in quit:
        print('Cannot save unfinished player')
        time.sleep(1)
        exit()
    else:
        print("\nSorry, not available\n")
        your_equipment.append(' ')


    new_carry = input("\nPotion, Yes or No?\n").lower()
    if new_carry in quit:
        exit(you, x, y, a, f, g, k, pk, ready_p_list, your_equipment, del_item, direction_data,lighthouseQuest)
    elif new_carry in positive:
        lighhouseQuest = [False,False,False,False,False,False,False,False]
        new_carry = "potion"
        your_equipment.append("key")
        your_equipment.append(new_carry)

        print(you)
        print(your_equipment)
        print(lighthouseQuest)
        time.sleep(3)
        start(you, your_equipment)
    
    else:
        lighhouseQuest = [False,False,False,False,False,False,False,False]
        your_equipment.append("key")
        new_carry = ' '
        your_equipment.append(new_carry)
        
        print(you)
        print(your_equipment)
        print(lighthouseQuest)
        time.sleep(3)
        start(you, your_equipment)

def run():

    run = True
    while run:
#        print("running")
        make_player()
        make_new_player()
        get_new_attack(make_player)
        get_new_defense(make_player, attack_int)
        get_new_description(make_player, attack_int, defend_int)
        get_new_health(make_player, attack_int, defend_int, my_description)
        get_new_eq()
        start()











