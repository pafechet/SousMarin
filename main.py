#coding: utf8

#modules externes
import sys
import os
import time
import select
import tty
import termios

#mes modules
import background

reglages_origine=termios.tcgetattr(sys.stdin)
#termios.tcsetattr(sys.stdin, termios.TCSADRAIN, reglages_origine())
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
    reload(sys) #changement encodage terminal
    sys.setdefaultencoding('utf-8') 
    #clear()
    background.create(0)
    tty.setraw(sys.stdin)
    entree=sys.stdin.read(1)[0]
    while entree != chr(27):
	    if(entree=='Z' or entree=='z'):     #test des touches, on attend que l'utilisateur choisisse une touche
	        y,x=background.getPosition()	#pour se déplacer
		background.setPosition(y-1, x)
            elif(entree=='S' or entree=='s'):
	        y,x=background.getPosition()
		background.setPosition(y+1, x)
	    elif(entree=='Q' or entree=='q'):
		y,x=background.getPosition()
		background.setPosition(y,x-1)
	    elif (entree=='D' or entree=='d'):
		y,x=background.getPosition()
		background.setPosition(y,x+1)
	    #Mode affichage
	    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, reglages_origine)
	    clear()
	    background.create(0)
            #Mode saisie
	    tty.setraw(sys.stdin)
	    entree=sys.stdin.read(1)[0]
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, reglages_origine)
		
	
   

run()
