# name = Ryan Dale
# project = Text Based Game
# start date = 15/1/19
from tkinter import *
import time
import os
import pygame
import winsound



def slowTyping(t):
  for x in t:
      print(x, end ="", flush=True)
      time.sleep(.04)

def fastTyping(t):
    for x in t:
        print(x, end="", flush=True)
        time.sleep(.01)


#menu_theme = pygame.mixer.Sound("s1.wav")
 

def startORexit():
    pygame.init()
    pygame.mixer.music.load("s1.ogg")
    pygame.mixer.music.play(-1)





    
    #winsound.PlaySound("/res/s1", winsound.SND_FILENAME) 
        

    fastTyping('\n                Programmed and Written by\n\n                      \n')
    fastTyping('          ____ ____ ____ ____ ____ ____ ____ ____ \n')
    fastTyping('         ||B |||l |||a |||n |||c |||q |||u |||e ||\n')
    fastTyping('         ||__|||__|||__|||__|||__|||__|||__|||__||\n')
    fastTyping('         |/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|\n')
    time.sleep(1)
    os.system('cls')
    
    print('\n                   Welcome to                                      ')
    fastTyping('       ____  __    __  __  ____    __    ____  ___  _   _  ____  ___\n')
    fastTyping('      (  _ \(  )  (  )(  )( ___)  (  )  (_  _)/ __)( )_( )(_  _)/ __)\n')
    fastTyping('       ) _ < )(__  )(__)(  )__)    )(__  _)(_( (_-. ) _ (   )(  \__ \\ \n')
    fastTyping('      (____/(____)(______)(____)  (____)(____)\___/(_) (_) (__) (___/ \n')
    fastTyping('\n')
    fastTyping('\n')
    fastTyping('\n')
    slowTyping('\n\n                         1. Start              \n\n')
    slowTyping('                          2. Exit                  ')
    fastTyping('\n\n')

    selectionlist = ['1', '2', '3', '4']
    choice = selectchoice(selectionlist)

    if choice == '1':
        start(inv)
        os.system('cls')

    elif choice == '2':
        exit(0)

def start(inv):
    os.system('cls')
    slowTyping('\nYou are in-front of the house. What are you going to do?\n')
    fastTyping('\n1. Open the door. Not sure that\'s legal.\n')
    fastTyping('\n2. Check the Mail. Bills, how ravashing.\n')
    fastTyping('\n3. Look under the mat. Not sure why you\'d do that.\n')
    fastTyping('\n4. Look through the window. Let\'s hope no one is in!.\n')

    selectionlist = ['1', '2', '3', '4']
    choice = selectchoice(selectionlist)

    if choice == '1':
        if 'key' in inv:
            os.system('cls')
            print('You opened the door with the Key. Where were you keeping that?')
            inside(inv)
        else:
            os.system('cls')
            print('The door is closed. You\'ll need a key.')
            time.sleep(2)
            start(inv)
    elif choice == '2':
        os.system('cls')
        print('You open the mailbox and find a floppy disk.')
        time.sleep(1)
        print ('Pick it up?')
        print('\n1. Take the floppy disk and close the mailbox.')
        print('\n2. Close the mailbox.')

        selectionlist = ['1', '2']
        choice = selectchoice(selectionlist)
    if choice == '1':
        inv.append('Floppy Disk')
        print('\nYou take the Floppy Disk and close the mailbox')
        time.sleep(2)
        start(inv)
    elif choice == '2':
        print('\nYou close the mailbox.')
        time.sleep(2)
        start(inv)

    if choice == '3':
        os.system('cls')
        print('\nThere is a key under the mat.')
        time.sleep(1)
        print('Pick it up?')

        print('\n1. Take the key and replace the mat.')
        print('\n2. Leave it alone.')

        selectionlist = ['1', '2']
        choice = selectchoice(selectionlist)
        if choice == '1':
            inv.append('key')
            print('\nYou take the key and repurpose the mat.')
            time.sleep(2)
            start(inv)
        elif choice == '2':
            print('\nYou leave the key alone and put the mat back to where it was.')
            time.sleep(2)
            start(inv)

    if choice == '4':
        os.system('cls')
        print('As you look through the window you see that no one is inside.')
        print('Blue light fills the room, coming from a computer on a desk from the far side.')
        time.sleep(2)
        start(inv)


def inside(inv):
    print('\n You are inside the house')
    print('You go to the desk with the computer.')
    time.sleep(1)
    print('What will you do?')
    print('\n1. Switch on the computer.')
    print('\n2. Leave the house.')

    selectionlist = ['1', '2']
    choice = selectchoice(selectionlist)

    if choice == '1':
        if 'Floppy Disk' in inv:
            os.system('cls')
        print('\nThe computer begins to boot.')
        print('On the screen appears a message. \"Congrats. You win!\"')
        exit(0)
        inside(inv)

    else:
        os.system('cls')
        print('There is a Password. You must find the Floppy Disk.')
        time.sleep(2)
        start(inv)


def selectchoice(selectionlist):
    choice = input('\nEnter: ')
    if choice in selectionlist:
        return choice
    elif choice == 'quit':
        exit(0)
    else:
        print('Invalid Input')
        return selectchoice(selectionlist)



os.system('cls')
inv = ['']
startORexit()
#start(inv)
