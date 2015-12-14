from colorama import *
from termcolor import *
init()
class health(object):
    def __init__(self):
        self.health = 100
        self.current_health = self.health
        self.hi_health = self.health
        self.med_health = self.health / 3.0 * 2.0
        self.low_health = self.health / 3.0
        self.dead = 0
        self.mana = 100
    def healthprint(self,current_health):
        if current_health in range(int(self.med_health), int(self.hi_health) + 1):
            self.color = 'green'
        elif current_health in range(int(self.low_health),int(self.med_health)):
            self.color = 'yellow'
        elif current_health in range(1, int(self.low_health)):
            self.color = 'red'
        else:
            self.color = 'grey'
        self.spaces = self.health - current_health
        print('[', end='')
        print(colored(chr(9608),self.color) * current_health, end='')
        print(colored(chr(9608),'white') * self.spaces, end='')
        print(']')
    def manaprint(self,current_mana):
        self.manaspaces = self.mana - current_mana
        print('[', end = '')
        print(colored(chr(9608),'blue') * current_mana, end = '')
        print(colored(chr(9608),'white') * self.manaspaces, end = '')
        print(']')
test = health()
