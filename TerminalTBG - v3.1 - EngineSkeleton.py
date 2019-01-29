# name = Blancque
# project = Text Based Game
# start date = 15/1/19
from tkinter import *
import time
import os
import pygame
import winsound


#SLOW TYPE FUNCTION
def slowTyping(t):
  for x in t:
      print(x, end ="", flush=True)
      time.sleep(.04) #SET SPEED HERE
      
#FASTER TYPE FUNCTION
def fastTyping(t):
    for x in t:
        print(x, end="", flush=True)
        time.sleep(.01)#SET SPEED HERE



 

def startORexit():
   #pygame.init()
    #pygame.mixer.music.load("s1.ogg")
    #pygame.mixer.music.play(-1)





    
 
        

    fastTyping('\n                Programmed and Written by\n\n                      \n')
    fastTyping('          ____ ____ ____ ____ ____ ____ ____ ____ \n')
    fastTyping('         ||B |||l |||a |||n |||c |||q |||u |||e ||\n')
    fastTyping('         ||__|||__|||__|||__|||__|||__|||__|||__||\n')
    fastTyping('         |/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|\n')
    titleRefresh()
    
    print('\n                   Welcome to                                      ')
    fastTyping('\n') #INSERT ASCII TITLE HERE
    fastTyping('\n') #INSERT ASCII TITLE HERE
    fastTyping('\n') #INSERT ASCII TITLE HERE
    fastTyping('\n') #INSERT ASCII TITLE HERE
    fastTyping('\n') 
    fastTyping('\n')
    fastTyping('\n')
    slowTyping('\n\n                         1. Start              \n\n')
    slowTyping('                          2. Exit                  ')
    fastTyping('\n\n')

    selectionlist = ['1', '2', '3', '4']
    choice = selectchoice(selectionlist)

    if choice == '1':
        chapterOne(inv)
        os.system('cls')

    elif choice == '2':
        exit(0)

def chapterOne(inv):
    refresh()
    fastTyping('\n')
    fastTyping(' )   ___                               ___         \n') #INSERT ASCII TITLE HERE
    fastTyping('(__/_____) /)                        /(,  )       \n') #INSERT ASCII TITLE HERE
    fastTyping('  /       (/   _  __  _/_  _  __    /    / __    _ \n') #INSERT ASCII TITLE HERE
    fastTyping(' /        / )_(_(_/_)_(___(/_/ (_  /    /  / (__(/_\n') #INSERT ASCII TITLE HERE
    fastTyping('(______)       .-/                (___ /           \n')
    fastTyping('              (_/                                 \n')
    titleRefresh()
    #Level Tile ENDS HERE
    slowTyping('') #ENTER STORY TEXT HERE
    refresh()
    slowTyping('\nWhat are you going to do?\n')
    fastTyping('\n1. \n')
    fastTyping('\n2. \n')
    fastTyping('\n3. \n')
    fastTyping('\n4. \n')

    selectionlist = ['1', '2', '3', '4']
    choice = selectchoice(selectionlist)

    #CHOICE  1 is the route to ChapterOneA
    if choice == '1':
        if 'enter inventory item here' in inv: #INVENTORY CHECK success
            os.system('cls')
            print('Enter inventory check sucess text here')
            chapterOneA1(inv)                       # move on to next area
        else:
            os.system('cls')                   #INVENTORY CHECK failure
            print('Enter inventory check failure text here')
            time.sleep(2)
            chapterOne(inv)                    #Return to master method (previous area)
            
     #CHOICE 2 results in an inventory append of ''         (ITEM CAN BE CHANGE AT THE inv.append)
    elif choice == '2':
        os.system('cls')
        print('Enter Item Found flavour text here')         #ENTER TEXT FOR HAVING FOUND AN ITEM HERE
        time.sleep(1)
        print ('Pick it up?')                               #Enter Action Prompt HERE
        print('\n1.Enter Take the Item Prompt Here')        #Enter Text For User Choice of Takeing Item 
        print('\n2.Enter DID NOT Take the Item Promt Here') #Enter Text For User Choice of NOT Takeing Item

        selectionlist = ['1', '2']
        choice = selectchoice(selectionlist)

        
    if choice == '1':
        inv.append('(add item to inv here)')              #ENTER INVENTORY ITEM NAME ADDED TO (inv) HERE
        print('\nEnter Item Added Text Here')             #ENTER (YOU HAVE FOUND ITEM) TEXT HERE
        time.sleep(2)
        chapterOne(inv)
    elif choice == '2':
        print('\nEnter Item NOT Added Text Here')         #ENTER DID NOT TAKE ITEM TEXT HERE
        time.sleep(2)
        chapterOne(inv)

       #CHOICE 3 results in an inventory append of ''          (ITEM CAN BE CHANGE AT THE inv.append)
    if choice == '3':
        os.system('cls')
        print('\nEnter Item Found flavour text here')        #ENTER TEXT FOR HAVING FOUND AN ITEM HERE
        time.sleep(1)
        print('Pick it up?')                                 #Enter Action Prompt HERE
        print('\n1. Enter Take the Item Prompt Here')        #Enter Text For User Choice of Takeing Item 
        print('\n2. Enter DID NOT Take the Item Promt Here') #Enter Text For User Choice of NOT Takeing Item

        selectionlist = ['1', '2']
        choice = selectchoice(selectionlist)

        
        if choice == '1':
            inv.append('(add item to inv here)')                #ENTER INVENTORY ITEM NAME ADDED TO (inv) HERE
            print('\nEnter Item Added Text Here')               #ENTER (YOU HAVE FOUND ITEM) TEXT HERE
            time.sleep(2)
            chapterOne(inv)
        elif choice == '2':
            print('\nEnter Item NOT Added Text Here')           #ENTER DID NOT TAKE ITEM TEXT HERE
            time.sleep(2)
            chapterOne(inv)
            
            
    #CHOICE 4 results in printing expositional/descriptive text
    if choice == '4':
        os.system('cls')
        print('Enter expositional/descriptive text')
        print('Enter expositional/descriptive text')
        time.sleep(2)
        chapterOne(inv)


def chapterOneA1(inv):
    print('\n Enter descriptor text for Character Route A')
    print('Enter descriptor text for Character Route A')
    time.sleep(1)
    print('What will you do?')
    print('\n1. Enter Choice Text Here')
    print('\n2. Enter Choice Text Here')

    selectionlist = ['1', '2']
    choice = selectchoice(selectionlist)

    if choice == '1':
        if 'Enter inventory item here' in inv:
            os.system('cls')
        print('\nEnter Choice One result Flavor Text here')
        print('Enter Choice One result Flavor Text here')
        ChapterOneA2(inv)

    else:
        os.system('cls')
        print('Enter Inventory check failure Here')
        time.sleep(2)
        chapterOne(inv)


def selectchoice(selectionlist):
    choice = input('\nEnter: ')
    if choice in selectionlist:
        return choice
    elif choice == 'quit', 'exit':
        exit(0)
    else:
        print('Invalid Input')
        return selectchoice(selectionlist)


def titleRefresh():
    time.sleep(2)
    os.system('cls')

def refresh():
    time.sleep(1)
    os.system('cls')



os.system('cls')
inv = ['']
startORexit()
#start(inv)
