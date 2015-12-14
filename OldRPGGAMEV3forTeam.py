#Copyright 2015 Wet Ferret Studios
#Import neccessary libraries
import time
#Initialize Player Class

class Player(object):
    base_health = 100
    base_damage = 3
    base_defense = 3
    base_regen_per_turn = 3
    base_magic_damage = 1
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
                }
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
                }
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
                }
            }
        }
    }
    current_weapon = 'fist'
    current_armor = 'clothes'
    current_ring = 'wedding ring'
    current_amulet = 'silver locket'

    def __init__(self):
        self.room_number = '0'
        self.command = 'null'
        self.health = self.base_health
        self.damage = self.base_damage
        self.defense = self.base_defense
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
            time.sleep(1)
            print('You have moved ' + direction)
        except KeyError:
            print('Please enter a valid direction')
            return False

    def examine(self, item):
        try:
            print('You look around and find a ' + room[self.room_number]['items'][item]['name'] + ' lying on the floor')
            print('The object is ' + room[self.room_number]['items'][item]['desc'])
            print('You ascertain its value to be roughly ' + str(room[self.room_number]['items'][item]['value']) + ' gold.')
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
            self.move(input('Please enter a direction: '))
        elif str(self.command) == 'look':
            self.look()
        elif str(self.command) == 'pickup':
            print('The items you can pick up are: ')
            self.listitems()
            self.pickup(input('What do you want to pick up: '))
        else:
            print('Derher')

    def list_items(self):
        for i in room[self.room_number]['items']:
            try:
                print(room[self.room_number]['items'][i]['name'])
            except KeyError:
                print('KeyError')

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
                    print('I done goofed')

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
                }
            },
        },
        'desc': 'Insert desc here',
        'entry_info': 'Insert desc here',
        'directions': {
            'n': '1000',
        },
        'environment': 'Temple',
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
player = Player()