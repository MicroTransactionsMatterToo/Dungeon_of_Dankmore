# Copyright 2015 Wet Ferret Studios

# Initialize Player Stats
playerstats = {
    'health': 100,
    'name': 'Gerald Lagley',
    'inventory': {

    },
    'damagemult': 0,
}

# Initialize Rooms
roomnumberint = 0
roomnumber = str(roomnumberint)
room = {
    '0': {
        'name': 'Temple Atrium',
        'items': {
            'noitems': False,
            'wooden stick': {
                'name': 'Wooden Stick',
                'desc': 'A wooden stick, could be useful',
                'value': 0,
            },
        },
        'desc': 'Insert desc here',
        'entryinfo': 'Insert room desc here',
        'directions': {
            'n': True,
            's': False,
            'e': False,
            'w': False,
            'u': False,
            'd': False,
            'directions': ['N','S','E','W','U','D']
        }
    },
    '1000': {
        'name': 'Temple Atrium',
        'items': {
            'noitems': True,
        },
        'desc': 'desc',
        'entryinfo': 'entryinfo',
        'directions': {
            'n': True,
            's': True,
            'e': True,
            'w': True,
            'u': False,
            'd': False,
            'directions': ['N','S','E','W','U','D']
        }
    }

}
roomtrapped = False
roomnoitems = room[roomnumber]['items']['noitems']


# Initialize Commands
def movefunc(direction):
    """

    :type direction:str
    """
    global roomnumberint
    global roomnumber
    if direction.lower() == 'n' and room[roomnumber]['directions'][direction.lower()] == True:
        roomnumberint += 1000
        roomnumber = str(roomnumberint)
    elif direction.lower() == 's' and room[roomnumber]['directions'][direction.lower()]:
        roomnumberint -= 1000
        roomnumber = str(roomnumberint)
    elif direction.lower() == 'e' and room[roomnumber]['directions'][direction.lower()]:
        roomnumberint += 10
        roomnumber = str(roomnumberint)
    elif direction.lower() == 'w' and room[roomnumber]['directions'][direction.lower()]:
        roomnumberint -= 10
        roomnumber = str(roomnumberint)
    elif direction.lower() == 'u' and room[roomnumber]['directions'][direction.lower()]:
        roomnumberint += 100000
        roomnumber = str(roomnumberint)
    elif direction.lower() == 'd' and room[roomnumber]['directions'][direction.lower()]:
        roomnumberint -= 100000
        roomnumber = str(roomnumberint)
    else:
        print('Please enter a valid direction')


def roomproperties():
    global roomnumber
    global roomnumberint
    global roomnoitems
    if room[roomnumber]['items']['noitems'] is True:
        roomnoitems = True
    else:
        roomnoitems = False


def examinefunc(item):
    global roomnumberint
    global roomnumber
    global roomnoitems
    if roomnoitems is False:
        print('Name: ' + room[roomnumber]['items'][item]['name'])
        print('Description: ' + room[roomnumber]['items'][item]['desc'])
        print('Value: ', end = '')
        print(room[roomnumber]['items'][item]['value'], end = '')
        print(' gold')
    elif roomnoitems is True:
        print('You look around the room but can\'t find a single item')
    else:
        assert isinstance(item, str)
        print('You look but fail to find ' + item)

def lookfunc():
    global roomnumber
    global roomnumberint
    global roomnoitems
    global room
    roomnumber = str(roomnumberint)
    print(room[roomnumber]['name'])
    print(room[roomnumber]['desc'])
    if roomnoitems is True:
        print('There are no items in this room')
    elif roomnoitems is False:
        print('Items you can see: ')
        for item in room:
            print('Name: ' + room[roomnumber]['items'][item]['name'])
            print('Description: ' + room[roomnumber]['items'][item]['desc'])
            print('Value: ', end = '')
            print(room[roomnumber]['items'][item]['value'], end = '')
            print(' gold')
    else:
        print('Error')
def userinput(func):
    global roomnumber
    global room
    if func == 'examine':
        examinefunc(input("What would you like to examine"))
    elif func == 'look':
        lookfunc()
    elif func == 'move':
        print('Valid Directions are: ')
        for items in room[roomnumber]['directions']['directions']:
            print(items + ': ', end = '')
            print(room[roomnumber]['directions'][items.lower()])
        movefunc(input('Which direction would you like to go: '))
    else:
        print('Please enter a valid command')
        movefunc(input('Which direction would you like to go: '))
x = 1
while True:
    userinput(input('Enter command: '))
    x += 1