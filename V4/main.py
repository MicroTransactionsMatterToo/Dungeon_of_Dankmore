#!/usr/bin/python3
from colorama import init
from sdl2 import rect
# Initalise Colorama for nice coloured output
init()

# Create the player class
class Player(object):
    # Base stats for future calculations
    base_health = 100
    base_damage = 3
    base_defense = 3
    base_regen_per_turn = 3
    base_magic_damage = 1
    base_mana = 1
    name = "Default Man"
    # Empty inventory to put items into later
    inventory = {}
    # Store room number
    room_number = "0"
    equipped = {
        'weapon': {
            'melee': {

            },
            'ranged': {

            },
            'magic': {

            },
        },
        'armour': {
            'helmet': {
            },
            'chest': {
                'dirtyshirt': {
                    'name': 'Dirty Shirt',

                }
            }
        }
    }
