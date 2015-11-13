#Copyright 2015 Wet Ferret Studios
#Import necessary libraries
from time import sleep
from os import system
from colorama import Fore, Back, init,
from termcolor import colored

#Initialize Display Class
class DisplayOut(object):
    #Health Bar Module
    def healthbar(self,total_health,current_health):
        