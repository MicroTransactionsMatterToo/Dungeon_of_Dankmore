#Copyright 2015 Wet Ferret Studios
#Import neccessary libraries
import time
#Initializing Player Class

class Player(object):
    basehealth = 100
    name = 'Gerald Lagley'
    inventory = {

    }
    room_number = '0'
    equipped = {
        'weapon': {

        },
        'armor': {

        },
        'ring': {

        },
        'amulet':{

        }
    }

    def __init__(self):
        self.room_number = '0'
        self.command = 'null'

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
            if input('Do you want to pick up ' + item).lower() == 'yes' or 'y':
                try:
                    self.inventory.append(room[self.room_number]['items'][item])
                    room[self.room_number]['items'].remove(item)
                except KeyError:
                    print('You look everywhere but can\'t find a ' + item.lower())

    def Input(self):
        self.command = input('Please enter a command: ')
        if str(self.command.lower()) == 'move':
            self.move(input('Please enter a direction: '))

        else:
            print('Derher')

#Initialize rooms
room = {
    '0': {
        'name': 'Temple Atrium',
        'items': {
            'wooden stick': {
                'name': 'Wooden Stick',
                'desc': 'a wooden stick, could be useful',
                'value': 0,
                'equippable': True,
                'damagemult': 3,
                'type': 'weapon'
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
    },
    '2000': {
        'name': 'Temple Hallway',
        'items': {

        },
        'desc': 'Insert desc here',
        'entry_info': 'Insert entry info here',
    },
}
player = Player()