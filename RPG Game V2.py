# Copyright 2015 Wet Ferret Studios

# Initialize Player Stats
playerstats = {
    'basehealth': 100,
    'name': 'Gerald Lagley',
    'inventory': {

    },
    'damage': 4,
    'equipped': {
        'weapon': {

        },
        'ring': {
            'wedding ring': {
                'name': 'Wedding Ring',
                'desc': 'A simple ring of gold that you received from your wife on your wedding day',
                'value': 20,
                'equippable': True
            }
        },
        'amulet': {

        },
        'armor': {

        },
        'armorclass': 0,
        'extrahealth': 0,
        'negativehealth': 0,
        'extradamage': 0,
        'negativedamage': 0,
        'negativearmor': 0,
        'totalhealth': 0,
    },
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
                'equippable': True,
                'damagemult': 12,
                'type': 'weapon'
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
            'directions': ['N', 'S', 'E', 'W', 'U', 'D']
        }
    },
    '1000': {
        'name': 'Temple Antechamber',
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
            'directions': ['N', 'S', 'E', 'W', 'U', 'D']
        },

    },
    '2000': {
        'name': 'Temple Hallway',
        'items': {

        }
    }

}
roomtrapped = False
roomnoitems = room[roomnumber]['items']['noitems']
currentlyequipped = {
    'currentweapon': '',
    'currentring': '',
    'currentamulet': '',
    'currentarmor': '',
}


# Initialize Commands
def movefunc(direction):
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
        print('Value: ', end='')
        print(room[roomnumber]['items'][item]['value'], end='')
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
            print('Value: ', end='')
            print(room[roomnumber]['items'][item]['value'], end='')
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
            print(items + ': ', end='')
            print(room[roomnumber]['directions'][items.lower()])
        movefunc(input('Which direction would you like to go: '))
    else:
        print('Please enter a valid command')


def pickupfunc(item):
    global room
    global roomnumber
    global playerstats
    if item in room[roomnumber]['items']:
        if input('Do you want to pick up ' + item).lower() == 'yes' or 'y':
            playerstats['inventory'].append(room[roomnumber]['items'][item])
            room[roomnumber]['items'].remove(item)
        else:
            print('You look all around but utterly fail to find' + item)


def equipfunc(item):
    global room
    global playerstats
    global roomnumber
    global currentlyequipped
    if item in playerstats['inventory']:
        if playerstats['inventory'][item.lower()]['equippable']:
            if playerstats['inventory'][item.lower()]['type'] == 'weapon':
                for keys in playerstats['equipped']['weapon']:
                    playerstats['inventory'].append(playerstats['equipped']['weapon'][keys])
                playerstats['equipped']['weapon'].clear()
                playerstats['equipped']['weapon'].append(playerstats['inventory'][item.lower()])
                playerstats['inventory'].remove(item.lower())
                currentlyequipped['currentweapon'] = item.lower()
                print(
                    playerstats['equipped']['weapon'][item.lower()]['name'] + ' has been equipped to your weapon slot')
            elif playerstats['inventory'][item.lower()]['type'] == 'ring':
                for keys in playerstats['equipped']['ring']:
                    playerstats['inventory'].append(playerstats['equipped']['ring'][keys])
                playerstats['equipped']['ring'].clear()
                playerstats['equipped']['ring'].append(playerstats['inventory'][item.lower()])
                playerstats['inventory'].remove(item.lower())
                currentlyequipped['currentring'] = item.lower()
                print(playerstats['equipped']['ring'][item.lower()]['name'] + ' has been equipped to your ring slot')
            elif playerstats['inventory'][item.lower()]['type'] == 'amulet':
                for keys in playerstats['equipped']['amulet']:
                    playerstats['inventory'].append(playerstats['equipped']['amulet'][keys])
                playerstats['equipped']['amulet'].clear()
                playerstats['equipped']['amulet'].append(playerstats['inventory'][item.lower()])
                playerstats['inventory'].remove(item.lower())
                currentlyequipped['currentamulet'] = item.lower()
                print(
                    playerstats['equipped']['amulet'][item.lower()]['name'] + ' has been equipped to your amulet slot')
            elif playerstats['inventory'][item.lower()]['type'] == 'armor':
                for keys in playerstats['equipped']['armor']:
                    playerstats['inventory'].append(playerstats['equipped']['armor'][keys])
                playerstats['equipped']['armor'].clear()
                playerstats['equpped']['armor'].append(playerstats['inventory'][item.lower()])
                playerstats['inventory'].remove(item.lower())
                currentlyequipped['currentarmor'] = item.lower()
                print(playerstats['equipped']['armor'][item.lower()]['name'] + ' has been equipped to your armor slot')
            else:
                # Creating variable for failure notice as it exceeds character limit
                failure1 = "You rummage through the seemingly endless depths of your rucksack but fail to find"
                print(failure1 + item.lower)


def statscalc():
    global playerstats
    global currentlyequipped
    playerstats['damagemult'] = playerstats['equipped']['weapon'][currentlyequipped['currentweapon']]['damagemult'] + \
                                playerstats['basedamage'] - playerstats['negativedamage']
    playerstats['armorclass'] = playerstats['equipped']['armor'][currentlyequipped['currentarmor']]['armorvalue'] - \
                                playerstats['negativearmor']
    playerstats['totalhealth'] = playerstats['basehealth'] - playerstats['negativehealth'] + playerstats['extrahealth']
