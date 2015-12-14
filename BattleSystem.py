# Import libraries
from colorama import *
from sys import platform
from os import get_terminal_size
from UIV1 import *
from RPGGameV3 import player
from termcolor import colored
from random import randrange

# Initalize Battle System Class
test_enemy = [
    'r',1,1,1,'w',1,1,1,'b',1,1,1,'n',
    'r',1,1,1,'w',1,1,1,'b',1,1,1,'n',
    'r',1,1,1,'w',1,1,1,'b',1,1,1,'n','e'
]
slime = [
    0,0,'g',1,1,0,0,'n',
    0,1,'y',1,'g',1,'y',1,'g',1,0,'n',
    1,1,1,1,1,1,'n',
    1,1,1,1,1,1,'n','e'
]

temple_enemies = {
    '0': {
        'name': 'Slime',
        'stats': {
            'min_health': 7,
            'max_health': 14,
            'min_damage': 4,
            'max_damage': 7,
        },
        'display': [
            0,0,'g',1,1,0,0,'n',
            0,1,'y',1,'g',1,'y',1,'g',1,0,'n',
            1,1,1,1,1,1,1,'n',
            1,1,1,1,1,1,1,'n','e',
        ],
    },
    '1': {
        'name': 'Blue Slime',
        'stats': {
            'min_health': 9,
            'max_health': 19,
            'min_damage': 6,
            'max_damage': 14,
        },
        'display': [
            0,0,'b',1,1,1,0,'n',
            0,1,'y',1,'b',1,'y',1,'b',1,0,'n',
            1,1,1,1,1,1,1,'n',
            1,1,1,1,1,1,1,'n','e',
        ]
    }
}
class Battle_System(object):
    enemies = {
    }
    def __init__(self):
        pass

    def set_enemies(self, *args):
        enemy_list_length = len(args)
        for i in range(0,enemy_list_length):
            try:
                self.enemies[str(i)] = args[i]
            except:
                print('Enemy error')
                print(Exception)
                pass
    def display_enemies(self,val):
        if val == 0:
            print(' ', end='')
        elif val == 1:
            print(chr(9608), end='')
        elif val == 'r':
            print(Fore.RED, end='')
        elif val == 'n':
            print('\n', end='')
        elif val == 'g':
            print(Fore.GREEN, end = '')
        elif val == 'b':
            print(Fore.BLUE, end = '')
        elif val == 're':
            print(Fore.BLACK, end = '')
        elif val == 'w':
            print(Fore.WHITE, end = '')
        elif val == 'e':
            print(Fore.BLACK+ '\n')
        elif val == 'y':
            print(Fore.YELLOW, end = '')
        else:
            print(str(val) + 'Invalid pixel')
    def pass_to_display(self):
        for i in self.enemies:
            for j in range(0,len(self.enemies[i]['display'])-1):
                self.display_enemies(self.enemies[i]['display'][j])

    def initiate_battle(self):
        self.set_enemies()

test = Battle_System()