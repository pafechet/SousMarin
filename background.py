# coding: utf-8
import sys
import os
import codecs
import json
#le module background gere le type abstrait de donnee background
#un background contient une chaine de caractere qui represente
#une image de fond d ecran

import collision_environement

position=[4 ,26]
repertoire=os.path.dirname(os.path.abspath(__file__))
#fonction pour changer la position
def setPosition(y,x):
	global position
	position=[y,x]


def get_term_size():
    data={}
    with codecs.open(repertoire + '/taille_term.json', 'r', encoding='utf-8') as file_:
        data = json.load(file_)
    file_.close

    try:
        if data['x'] and data ['y']:
            return data['x'], data['y']
        else:
            return 140, 30
    except KeyError:
        return 140, 30
#fonction pour avoir la position dans la liste 'position' y au rang 0 et x au rang 1
def getPosition():
	return position[0], position[1]

#fonction qui permet d'écrire le sous marin dans le terminal
#le sous marin est sur le fond
def writeSubmarine(y,x, background ):

    y=y-3
    sousmarin=[
    '        _________      ',
    '    ___/  o o o  \___  ',
    '   /    ---------    \ ',
    '  |     ---------     |',
    '8-=\_________________/ ']

    for j in range(len(sousmarin)): #longeur de la liste (ligne)
	for i in range(len(sousmarin[j])):#longeur du nombre de caractères (colonnes)
		background[y+j][x+i]=sousmarin[j][i]
    return background



def create(carte):
	o2=collision_environement.getO2()

	bg=[]
	for j in range(120):
		bg.append(['']*310)

	j=0
	file_path=repertoire+'/'+carte

	f=codecs.open(file_path, 'r', encoding="utf-8")
	for line in f.readlines():
		#print line
		j+=1
		i=0
		for ch in line:

			if '\n' in ch:
				bg[j][i]=' '
			else:
				#print j,i
				bg[j][i]=ch.decode('utf-8')
				i+=1
		bg.append(o2)
	f.close()
	y,x=getPosition()
	#print y,x
	bg=writeSubmarine(y,x, bg)
	xmax=0
	ymax=0
	xmin=0
	ymin=0

	'''if(y<30):
		ymax=30
	elif(y<60):
		ymax=60
	elif(y<90):
		ymax=90
	else:
		ymax=120

	if(x<120):
		xmax=120
	elif(x<240):
		xmax=240
	else:
		xmax=360'''




	#display_map(x, ymax, bg)
	return bg



def display_map():
	o2=collision_environement.getO2()
	y,x=getPosition()
	bg=create('c.txt')
	#print x,y
	x_term=get_term_size()[0]
	y_term=get_term_size()[1]
	ymin=0
	xmin=0

	if(x-(x_term/2)<0):
		xmin=0
	else:
		xmin=x-60

	#print 'y-15: '+str(y-15)
	if(y-(y_term/2)<0):
		ymin=0
	else:
		ymin=y-15


	#print ymin, xmin
	affichage=''
	for j in range(ymin,ymin+y_term):
		ligne=''
		for i in range(xmin,xmin+x_term):
		    ligne=ligne+bg[j][i]
		ligne=ligne+'\n'
		affichage=affichage+ligne
	#print o
	affichage=affichage+str(o2)
	print affichage



#def getChar(bg,x,y):
	#renvoie le contenu d une case donnee
#	return (bg["map"][y-1][x-1])
