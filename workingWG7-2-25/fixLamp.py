#!/usr/in/python
# -*- coding: utf-8 -*-

### Light match in burn tube BEFORE pumping fuel.

### need wrench

### need manual

### manual takes place of wrench

### need wire

### (manual,havewire,openengine,installwire,havematch,lightmatch,closeengine,pumpoil)

### lighthouseQuest(F,F,F,F,F,F,F,F)
### set lighthouseQuest[0,1,4] = T
### player must have manual, wire, and match
### ready list is [T,T,F,F,T,F,F,F]
### 
### if "F" <= 6 and room.get == sub_basement :
###     input = ("<. ")
###     if input == "fix engine" :
###         if lighthouseQuest[0] == False :
###             print("You do not have the manual")
###         elif lighthouseQuest[0] == True :
###             print("""
###     You skim the manual. It suggests that a fuse or wire has been damaged.
###             """)
###             if lighthouseQuest[1] == False :
###                 print("You should look for a bit of wire")
###             elif lighthouseQuest[1] == True :
###                 print("""
###     You pull on a handle on the engine lid. The burnt wire is easy to reach
### now. Do you want to proceed? Y/N
###                 """)
###             input = ("<. ")
###             if input == Y :
###                 lighthouseQuest[2] = T
###                 print("You are ready to install the wire.")
###                 input = ("<. ")
###                 if input == "install wire" or "install the wire":
###                     print("You install the wire")
###                     lighhouseQuest[3] = T
###                     if lighthouseQuest[4] == T :
###                         lighthouseQuest[5] = T
###                         input = "You light the match\nThe manual says you close the engine cover\n<. "
###                         if input == "" and time.sleep(5) :
###                             print("The match burns out")
###                             lighthouseQuest[5] = F
###                             lighthouseQuest[4] = F
###                         elif input == "close engine cover" :
###                             lighthouseQuest[6] = T
###                             print("You close the engine cover")
###                     elif lighthouseQuest[4] == F :
###                         print("You need to find the match")
###                 else:
###                     input = ("Command Not Recognized\n<. ")
###             elif input == N :
###                 walkerTest.look()
###             else:
###                 input = ("Y or N\n<. ")
###         else:
###             input = ("Command Not Recognized\n<. ")
###     elif input == "pump oil" and lighthouseQuest[ : ] == T,T,T,T,T,T,T,F :
###         lighthouseQuest[7] = T
###         print("You pump the oil and the Lighthouse Lamp shines again")
###     else:
###         input = ("Command Not Recognized\n<. ")
### 
### 
### 
### 
### 











### step one:

### open engine lid

### step two:

### fix broken connection

### delete wire

### need match

### step three:

### light match

### close engine lid

### step four:

### pump oil


