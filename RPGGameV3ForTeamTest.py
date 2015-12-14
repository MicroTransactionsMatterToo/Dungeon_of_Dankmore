# Copyright 2015 Wet Ferret Studios
# Import necessary libraries
from time import sleep
import os
from random import *
from colorama import *
from termcolor import *
import UIV1

init()
print(Fore.BLUE + '')
print('To use my input program type player.input(\'command_here\') Make sure to include the quote marks. Otherwise type player.function_here')


# Initialize Player Class


class Player(object):
    base_health = 100
    base_damage = 3
    base_defense = 3
    base_regen_per_turn = 3
    base_magic_damage = 1
    base_mana = 10
    name = 'Gerald Lagley'
    inventory = {
    }
    room_number = '0'
    equipped = {
        'weapon': {
            'fist': {
                'name': 'Fist',
                'desc': 'Your fist, a very trusty weapon.',
                'value': 'You wouldn\'t sell your own body would you',
                'equippable': True,
                'type': 'weapon',
                'perks': {
                    'health': 0,
                    'damage': 3,
                    'defense': 0,
                    'magic_damage': 0,
                },
                'amount': 1,
            }
        },
        'armor': {
            'clothes': {
                'name': 'Clothes',
                'desc': 'A reliable set of cotton clothes. Not very strong but keeps you warm.',
                'value': 20,
                'equippable': True,
                'type': 'armor',
                'perks': {
                    'health': 0,
                    'damage': 0,
                    'defense': 3,
                    'magic_damage': 0,
                },
                'amount': 1,
            }
        },
        'ring': {
            'wedding ring': {
                'name': 'Wedding Ring',
                'desc': 'A ring given to you by your wife on your wedding day.',
                'value': 100,
                'equippable': True,
                'type': 'ring',
                'perks': {
                    'health': 2,
                    'damage': 2,
                    'defense': 2,
                    'magic_damage': 3,
                },
                'amount': 1,
            }
        },
        'amulet': {
            'silver locket': {
                'name': 'Silver Locket',
                'desc': 'A family heirloom containing pictures of your children.',
                'value': 75,
                'equippable': True,
                'type': 'amulet',
                'perks': {
                    'health': 1,
                    'damage': 1,
                    'defense': 0,
                    'magic_damage': 4,
                    'regen': 3,
                    'mana': 2,
                },
                'amount': 1,
            }
        }
    }
    current_weapon = 'fist'
    current_armor = 'clothes'
    current_ring = 'wedding ring'
    current_amulet = 'silver locket'
    gold = 500

    def __init__(self):
        self.room_number = '0'
        self.command = 'null'
        self.health = self.base_health
        self.damage = self.base_damage
        self.defense = self.base_defense
        self.magic_damage = self.base_magic_damage
        self.regen_per_turn = self.base_regen_per_turn
        self.regen_per_turn += self.equipped['amulet'][self.current_amulet]['perks']['regen']
        self.mana = self.base_mana
        self.room = room[self.room_number]
        for i in self.equipped:
            for j in self.equipped[i]:
                try:
                    self.health += self.equipped[i][j]['perks']['health']
                    self.defense += self.equipped[i][j]['perks']['defense']
                    self.damage += self.equipped[i][j]['perks']['damage']
                    self.magic_damage += self.equipped[i][j]['perks']['magic_damage']
                    self.mana += self.equipped[i][j]['perks']['mana']
                    self.current_health = self.health
                    self.current_mana = self.mana
                except KeyError:
                    print('I done goofed')

    def name_set(self):
        if input('Do you wish to set your name: ') == 'y' or 'Y':
            self.name = input('Please enter your name: ')
            print("Your name is " + self.name)
        else:
            print('Your name is ' + self.name)

    def move(self, direction):
        try:
            self.room_number = room[self.room_number]['directions'][direction.lower()]
            self.room = room[self.room_number]
            sleep(1)
            if self.room['environment'] == 'Temple':
                print('You walk forward through the white marble doorway and into the ' + room[self.room['directions'][direction.lower()]['name']])
            else:
                print('You move 1 room ' + direction)
        except KeyError:
            print('Please enter a valid direction')
            return False

    def examine(self, item):
        try:
            print('You look around and find a ' + room[self.room_number]['items'][item]['name'] + ' lying on the floor')
            print('The object is ' + room[self.room_number]['items'][item]['desc'])
            print('You ascertain its value to be roughly ' + str(room[self.room_number]['items'][item]['value']) + colored(' gold', 'yellow'))
        except KeyError:
            print('You look everywhere but fail to find a ' + str(item))

    def look(self):
        try:
            if room[self.room_number]['environment'] == 'Temple':
                print('A polished, marble plaque reads ' + room[self.room_number]['name'])
            else:
                print('Name: ' + room[self.room_number]['name'])
        except SyntaxError:
            print('Error: Syntax Error')
        print('You see ')
        for i in room[self.room_number]['items']:
            try:
                print(room[self.room_number]['items'][i]['name'])
            except KeyError:
                print('KeyError')

    def pickup(self, item):
        if item.lower() == 'all':
            conf = input('Do you want to pick up all of the items in this room: ')
            if conf.lower() == 'y' or conf.lower() == 'yes':
                for item in room[self.room_number]['items']:
                    try:
                        self.inventory[item] = room[self.room_number]['items'][item]
                        del room[self.room_number]['items'][item]
                    except KeyError:
                        print('You look everywhere but can\'t find anything to pick up.')
        elif item.lower() == 'gold':
            conf = input('Do you want to pick up the coins on the floor: ')
            if conf.lower() == 'y' or conf.lower() == 'yes':
                try:
                    self.gold += room[self.room_number]['gold']
                    room[self.room_number]['gold'] -= room[self.room_number]['gold']
                except KeyError:
                    if self.room['environment'] == 'Temple':
                        print('You look carefully around the gleaming marble room,', end='')
                        print('thoroughly checking every corner, but fail to find any coins.')
                    else:
                        print('You look everwhere but fail to find any coins (environment not defined)')
        else:
            conf = input('Do you want to pick up the ' + item.lower() + ': ')
            if conf.lower() == 'y' or conf.lower() == 'yes':
                try:
                    self.inventory[item] = room[self.room_number]['items'][item]
                    del room[self.room_number]['items'][item]
                except KeyError:
                    print('You look everywhere but can\'t find a ' + item.lower())
            else:
                print('You consider it, but decide not to pick up the ' + item.lower())

    def input(self, command):
        self.command = command
        if str(self.command) == 'move':
            self.move(input(colored('Please enter a direction: ', 'green')))
        elif str(self.command) == 'look':
            self.look()
        elif str(self.command) == 'pickup':
            print(colored('The items you can pick up are: ', 'green'))
            colored(self.list_items(), 'blue')
            self.pickup(input(colored('What do you want to pick up: ', 'green')))
        elif str(self.command) == 'help' or str(self.command) == '?':
            print('These are possible help items: ')
            print(colored('[1]Commands  ', 'red'), end = '')
            print(colored('[2]Battle    ', 'red'), end = '')
            print(colored('[3]Equipping Items', 'red'))
            print(colored('[4]Picking Up Items', 'red'), end = '')
            print(colored('[5]Moving', 'red'), end = '')
            print(colored('[6]Debug', 'red'))
            self.game_help(input((colored('What would you like help with: '))))
        else:
            print('Derher')

    def list_items(self):
        for i in room[self.room_number]['items']:
            try:
                print(Fore.BLUE + room[self.room_number]['items'][i]['name'])
            except KeyError:
                print('KeyError')

    def game_help(self,help_item):
        if help_item == '1' or help_item.lower() == 'commands':
            print(colored('Commands available: ', 'green'))
            print(colored('Help: List possible help items', 'blue'))
            print(colored('Stats (Debug): Updates stats. Use by typing player.stats()', 'blue'))
            print(colored('Look: Gives an overview of the current room', 'blue'))
            print(colored('Equip: Equips a specified item', 'blue'))
            print(colored('Pickup: Picks up an item in your current room', 'blue'))
            print(colored('Examine: Examines a specific item', 'blue'))
            print(colored('Name_set (Debug): Used to set player name. Use like this player.name_set()', 'blue'))
        elif help_item == '2' or help_item.lower() == 'battle':
            print(colored('Pending :)', 'red'))
        elif help_item == '3' or help_item.lower() == 'equipping items':
            print(colored('If you haven\'t used exit then type equip. If you have used exit then type player.equip(item name here)', 'blue'))
        elif help_item == '4' or help_item.lower() == 'picking up items':
            print(colored('To pick up items type pickup', 'blue'))
        elif help_item == '5' or help_item.lower() == 'moving':
            print(colored('To move type move', 'blue'))
        elif help_item == '6' or help_item.lower() == 'debug':
            print(colored('Debug Commands: player.stats(), player.health, player.inventory, player.list_items().', 'blue'))
        else:
            print(colored('Please enter a valid help topic', 'red'))

    def stats(self):
        self.health = self.base_health
        self.defense = self.base_defense
        self.damage = self.base_damage
        self.magic_damage = self.base_magic_damage
        self.regen_per_turn = self.base_regen_per_turn
        self.regen_per_turn += self.equipped['amulet'][self.current_amulet]['perks']['regen']
        for i in self.equipped:
            for j in self.equipped[i]:
                try:
                    self.health += self.equipped[i][j]['perks']['health']
                    self.defense += self.equipped[i][j]['perks']['defense']
                    self.damage += self.equipped[i][j]['perks']['damage']
                    self.magic_damage += self.equipped[i][j]['perks']['magic_damage']
                except KeyError:
                    return False

    def equip(self, item):
        if item.lower() in self.inventory:
            item_type = self.inventory[item]['type']
            for i in self.equipped[item_type]:
                self.inventory[i] = self.equipped[item_type][i]
            self.equipped[item_type].clear()
            self.equipped[item_type][item] = self.inventory[item]
            del self.inventory[item]
            self.stats()
        else:
            print('You rummage through your bag but can\'t find a ' + item + '.')


# Initialize rooms

room = {
    '0': {
        'name': 'Temple Atrium',
        'items': {
            'wooden stick': {
                'name': 'Wooden Stick',
                'desc': 'a wooden stick, could be useful',
                'value': 0,
                'equippable': True,
                'type': 'weapon',
                'perks': {
                    'health': 0,
                    'damage': 6,
                    'defense': 0,
                    'magic_damage': 0,
                },
            },
        },
        'desc': 'Insert desc here',
        'entry_info': 'Insert desc here',
        'directions': {
            'n': '1000',
        },
        'environment': 'Temple',
        'hostile': False,
    },
    '1000': {
        'name': 'Temple Antechamber',
        'items': {

        },
        'desc': 'Insert desc here',
        'entry_info': 'Insert entry info here',
        'directions': {
            'n': '2000',
            'e': '1010',
            'w': '990',
            's': '0'
        },
        'environment': 'Temple',
        'hostile': True,
    },
    '2000': {
        'name': 'Temple Hallway',
        'items': {

        },
        'desc': 'Insert desc here',
        'entry_info': 'Insert entry info here',
        'directions': {

        },
    },
}

# Create player with Player() class

player = Player()
