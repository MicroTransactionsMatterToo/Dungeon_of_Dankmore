#Copyright Wet Ferret Studios 2015

#Initialize Player Stats
playerstats = {
    "health": 100,
    "name": 'Gerald Lagley',
    'inventory': [],
    'damagemult': 0,
    }
#Initialize Rooms
roomnumberint = 000000
roomnumber = str(roomnumberint)
room = {
    '0':{
        'name': 'Start Room',
        'items': {
            'noitems': True,
            },
        'desc':  'Insert well written description here',
        'entryinfo': 'insert room intro here',
        }
    
             
#Initialize Commands
def movefunc(direction):
    global roomnumberint
    global roomnumber
    if direction == 'n':
        roomnumberint += 1000
        roomnumber = str(roomnumberint)
    elif direction == 's':
        roomnumberint -= 1000
        roomnumber = str(roomnumberint)
    elif direction == 'e':
        roomnumberint += 10
        roomnumber = str(roomnumberint)
    elif direction == 'w':
        roomnumberint -= 10
        roomnumber = str(roomnumberint)
    elif direction == 'u':
        roomnumberint += 100000
        roomnumber = str(roomnumberint)
    elif direction == 'd':
        roomnumberint -= 100000
        roomnumber = str(roomnumberint)
    else:
        print('Please enter a valid direction')
    
def examinefunc(item):
    global roomnumberint
    global roomnumber
    if room[roomnumber]['items']['noitems'] == False and room[roomnumber]['items'][item]['Trapped'] == False:
        print('Name: ' + room[roomnumber]['items'][item]['name'])
        print('Description: ' + room[roomnumber]['items'][item]['desc'])
        print('Value: ', end = '')
        print(room[roomnumber]['items'][item]['value'], end = '')
        print(' gold')
def lookfunc():
    global roomnumber
    roomnumber = str(roomnumberint)
    print(room[roomnumber]['name'])
    print(room[roomnumber]['desc'])
def userinput(func):
    global roonumber
    print(room[roomnumber]['entryinfo'])
    if func == 'examine':
        examinefunc(input('What would you like to examine: '))
    elif func == 'look':
        lookfunc(roomnumber)
    else:
        print('Please enter a valid command')
