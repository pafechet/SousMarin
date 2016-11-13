# coding: utf-8
import sys
import os
import codecs
#le module background gere le type abstrait de donnee background
#un background contient une chaine de caractere qui represente
#une image de fond d ecran
position=[5,5]
def setPosition(y,x):
	global position
	position=[y,x]

def getPosition():
	return position[0], position[1]
	

def writeSubmarine(y,x, background ):

    y=y-3
    sousmarin=[
    '        _________      ',
    '    ___/  o o o  \___  ',
    '   /    ---------    \ ',
    '  |     ---------     |',
    '8-=\_________________/ ']

    for j in range(len(sousmarin)):
	for i in range(len(sousmarin[j])):
		background[y+j][x+i]=sousmarin[j][i]
    return background



def create(carte):
	bg=[]
	for j in range(31):
		bg.append(['']*120)
	#creation du fond
	#global bg
	repertoire=os.path.dirname(os.path.abspath(__file__))
	print repertoire
	#on ouvre la carte
	macarte = open ('carte.txt', 'r')

	string=macarte.read()

	#separation des lignes
	#la liste retournée est une liste
	#unidimensionnelle, aka que des x pas de y
	raw_ligne=string.splitlines()
	j=0

	f=codecs.open('carte.txt', 'r', "utf-8")
    	for line in f.readlines():
        	j+=1
        	i=0
		#print line
        	for ch in line:
			#print ch
        	        if ch in '\n':
			    if '\n' in ch:
             	                bg[j][i]=' '
        	        else:
			    #print j,i
        	            bg[j][i]=ch.encode('utf-8')
        	            i+=1          

    	f.close()
	
	y,x=getPosition()
	setPosition(y+1, x)
	bg=writeSubmarine(y,x, bg)

	affichage=''
	for j in range(len(bg)):
		ligne=''
		for i in range(len(bg[j])):
		    ligne=ligne+bg[j][i]
		ligne=ligne+'\n'
		affichage=affichage+ligne

	print affichage
		



	macarte.close

	return bg

def getChar(bg,x,y):
	#renvoie le contenu d une case donnee
	return (bg["map"][y-1][x-1])

def show(bg):

	#couleur fond
	sys.stdout.write("\033[40m")
	#couleur white
	sys.stdout.write("\033[37m")
