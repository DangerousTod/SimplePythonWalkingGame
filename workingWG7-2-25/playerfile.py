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

def playerlist_write(you, your_equipment, lighthouseQuest):
    print("check point")
    save_my_player = you[8]
    print_you = you[0:]
    print_your_equipment = your_equipment[0:]
    print_your_lighthouseQuest = lighthouseQuest[0:]

    saving_now = (save_my_player, print_you, print_your_equipment, print_your_lighthouseQuest)
    print(type(saving_now))
    save_name_is = saving_now[0]
    filep = "my_playerfile.txt"

    with open(filep, "r", encoding='utf-8') as playerfilefb:
    
        read_p_file_lines = playerfilefb.readlines()
        reading_lines = read_p_file_lines[:]
  
        filtered_lines = [line for line in reading_lines if save_name_is not in line]
            
        with open(filep, "w", encoding='utf-8') as playerfilef:
            playerfilef.writelines(filtered_lines)
      
            save_me = str(saving_now)         
            playerfilef.write(save_me)
            playerfilef.write("\n")
            walkerTest.do_exit()

