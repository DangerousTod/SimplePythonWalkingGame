#!/usr/in/python
# -*- coding: utf-8 -*-

import sys
import os
import time
import walkerTest

def playerlist_read():
    saved_players = []
    filepn = "my_playerfile.txt"
    with open(filepn, 'r', encoding='utf-8') as playerfilepn:
        contents = playerfilepn.readlines()
        content = contents[:]
        
        if len(content) <= 0:
            print("\nNo Saved Players\n")
            time.sleep(1)
            walkerTest.make_new_player()

        else:
            for line in content:
                freshline = eval(line)
                playerline = freshline[0]
                print(playerline)
                playereq = freshline[1]

                saved_players.append(playerline)
                available_players = saved_players

            choose_player = input('\nAll Saved Players\n')
            available_players = saved_players[:]

            if choose_player in available_players:

                you = freshline[1]
                your_equipment = freshline[2]
                lighthouseQuest = freshline[3]
                run = True
                walkerTest.save_start(you, your_equipment, lighthouseQuest)
                
            elif choose_player == '':
                print('\n No Match, Try Again\n')
                time.sleep(1)
                playerlist_read()
            else:
                print('\n No Match, Try Again\n')
                playerlist_read()
                   
#playerlist_read()
