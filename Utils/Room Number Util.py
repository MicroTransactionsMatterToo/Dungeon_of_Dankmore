#Wet Ferret Room Code Generator
roomnumber = 0
def roomcode(direction):
    global roomnumber
    if direction == 'n':
        roomnumber += 1000
    elif direction == 's':
        roomnumber -= 1000
    elif direction == 'e':
        roomnumber+= 10
    elif direction == 'w':
        roomnumber -= 10
    elif direction == 'u':
        roomnumber += 100000
    elif direction == 'd':
        roomnumber -= 100000
    else:
        return 0
    print(roomnumber)
x=1
while True:
    roomcode(input('Direction: '))
    x += 1
