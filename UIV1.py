# Copyright 2015 Wet Ferret Studios
# Import necessary libraries
from colorama import *
from termcolor import colored
from RPGGameV3 import player
from os import get_terminal_size
from sys import platform
import struct
from os import system
# Execute colorama's init script so that colored won't generate errors in windows
init()

def window_term_size():
    try:
        from ctypes import windll, create_string_buffer
        h = windll.kernel32.GetStdHandle(-12)
        csbi = create_string_buffer(22)
        res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)
        if res:
            (bufx, bufy, curx, cury, wattr,
             left, top, right, bottom, maxx, maxy) = struct.unpack('hhhhHhhhhhh', csbi.raw)
            sizex = right - left + 1
            sizey = bottom - top + 1
            return sizex, sizey
    except:
        return ('Derp')

def print_health():
    hi_health = player.health
    med_health = player.health / 3.0 * 2.0
    low_health = player.health / 3.0
    spaces = player.health - player.current_health
    if player.current_health in range(int(med_health),int(hi_health + 1)):
        health_color = 'green'
    elif player.current_health in range(int(low_health),int(med_health)):
        health_color = 'yellow'
    elif player.current_health in range(0,int(low_health)):
        health_color = 'red'
    else:
        health_color = 'grey'
    print('[', end = '')
    print(colored(chr(9608),health_color) * player.current_health, end = '')
    print(colored(chr(9608),'white') * spaces, end = '')
    print(']')

def print_mana():
    mana_spaces = player.mana - player.current_mana
    print('[', end = '')
    print(colored(chr(9608), 'blue') * player.current_mana, end = '')
    print(colored(chr(9608), 'white') * mana_spaces, end = '')
    print(']')

def battle_ui():
    print(Fore.BLACK)
    if platform == 'darwin':
        system('clear')
        print(chr(9608) * get_terminal_size()[0])
        for i in range (0, (get_terminal_size()[1] - 3)):
            print(chr(9608), end = '')
            print(' ' * (get_terminal_size()[0] - 2), end = '')
            print(chr(9608), end = '')
        print(chr(9608) * get_terminal_size()[0], end = '')
    elif platform == 'nt':
        system('cls')
        print(chr(9608) * window_term_size()[0])
        for i in range(0, (window_term_size()[1] - 3)):
            print(chr(9608), end = '')
            print('' * (window_term_size()[0] - 2), end = '')
            print(chr(9608))
        print(chr(9608) * window_term_size()[0])
    print(Fore.BLUE)