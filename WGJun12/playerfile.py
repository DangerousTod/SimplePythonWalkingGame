import time

import walkerTest
#import my_playername
#import my_playerfile

#[								]
#[file_path = "my_file.txt"					]
#[   my_list = [1, "apple", 3.14, True]				]
#[								]
#[   string_list = [str(item) for item in my_list]		]
#[   data_to_write = "\n".join(string_list)			]
#[								]
#[   with open(file_path, "w") as file:				]
#[       file.write(data_to_write)				]
#[								]

#you = [6, 6, 'furry in a bad way', 122, 'You', 'player', [], {}, 'howlard']
#your_equipment = ['hat', 'shirt', 'boots', 'shortsword', 'key', ' ']

#with fopen(rw)

def playerlist_write(you, your_equipment):

    save_my_player = you[8]
    print_you = you[0:]
    print_your_equipment = your_equipment[0:]

    saving_now = (save_my_player, print_you, print_your_equipment)
 #   print(saving_now, "saving from playerfile")
    save_name_is = saving_now[0]
  #  print(save_name_is, "save name is")

    filep = "my_playerfile.txt"

#    with open(filep, 'r', encoding='utf-8') as playerfilef:
    
#        read_p_file_lines = playerfilef.readlines()
#        reading_lines = read_p_file_lines[:]
#        print(read_p_file_lines[0], "r p file at zero")
        
    with open(filep, "r", encoding='utf-8') as playerfilefb:
    
        read_p_file_lines = playerfilefb.readlines()
#        print(read_p_file_lines, "lines to print")
        reading_lines = read_p_file_lines[:]
 #       print(reading_lines, "first reading lines")
        if reading_lines:
        
            
            with open(filep, "w", encoding='utf-8') as playerfilef:
        
 #               print("checkedy check check")
     #           print(save_name_is, "save the name")
      #          print(reading_lines, "print the lines")
                for line in reading_lines:
       #             print("reading the lines")
        #            print(line, "this is a line")
            #make line equal to line
                    write_line = eval(line)
  #                  print(write_line, "this is also a line")
                    cut_line = write_line[0]
   #                 print(cut_line, "the cut line here")
                    if cut_line.strip("\n") != save_name_is:
                        playerfilef.write(line)
                        save_me = str(saving_now)         
                        playerfilef.write(save_me)
                        walkerTest.do_exit()
                            
        else:
            save_me = str(saving_now)         
            playerfilefb.write(save_me)
  #          print("exit two")
            walkerTest.do_exit()
            
def playername_write(you, your_equipment):
    playername = you[8]
    playerstring = str(playername)
    saving_name = (playerstring)
    
    print(playerstring, "saving from playerfile")
    
    saved_players = []

    filepn = "my_playername.txt"

    with open(filepn, 'r+', encoding='utf-8') as playerfilenf:
           
        current_players = playerfilenf.readlines()
        
        if current_players:
            playerfilenf.write('\n**Next*Player**\n')
            playerfilenf.write(saving_name)

            playerlist_write(you, your_equipment)

        else:
            playerfilenf.write(playername)
            playerlist_write(you, your_equipment)


#[7, 7, "mean, green, killin' machine", 125, 'You', 'player', [], {}, 'wally']
#['helmet', 'coat', 'boots', 'sword', 'key', 'potion']

def playerlist_read():

    filepn = "my_playername.txt"

    with open(filepn, 'r', encoding='utf-8') as playerfilepn:
        content = playerfilepn.readline()
        choose_player = input('\nChoose a character from this list:\n')
        
        for line in content:
            print(line)
        
            if len(content) == 0:
                print("No Saved Players\n")
                walkerTest.start()
        
            elif choose_player == '':
                print('\n No Match, Try Again\n')
                time.sleep(1)
                walkergame.do_exit()
            elif choose_player not in content:
                print('\n No Match, Try Again\n')
                playerlist_read()

            else:
                findp = "my_playerfile.txt"
                with open(findp, 'r', encoding='utf-8') as findpf:
                    find_player = findpf.readlines()
                
                    for player in find_player:
                        finding_p = list(player)
                        finding_player = str(finding_p[0])
                        if finding_player == choose_player:
                            you = finding_p[0:8]
                            your_equipment = finding_p[9:]

                            run = True
                            walkerTest.save_start(you, your_equipment)

