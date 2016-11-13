#coding: utf8

#modules externes
import sys
import os
import time
import select
import tty
import termios

#mes modules
import sous_marin
import background
import UI


def show():
    global submarine,background
    #affichage des different element
    background.show(background)

	#afficher le sous_marin
    #sous_marin.writeSubmarine(dissubmarine)

def clear():
    sys.stdout.write("\033[1;1H")
    sys.stdout.write("\033[2J")

def run():
    for i in range( 10):
	    clear()
	    background.create(0)
	    time.sleep(0.1)
   

run()
