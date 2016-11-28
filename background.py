# coding: utf-8
import sys
import os
import codecs
#le module background gere le type abstrait de donnee background
#un background contient une chaine de caractere qui represente
#une image de fond d ecran
position=[5,]

#fonction pour changer la position
def setPosition(y,x):
	global position
	position=[y,x]

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
	bg=[]
	for j in range(31):
		bg.append(['']*120)
	#creation du fond
	#global bg
	repertoire=os.path.dirname(os.path.abspath(__file__))
	#print repertoire
	#on ouvre la carte
	#macarte = open ('carte.txt', 'r')

	#string=macarte.read()

	#separation des lignes
	#la liste retournée est une liste
	#unidimensionnelle, aka que des x pas de y
	#raw_ligne=string.splitlines()
	j=0

	f=codecs.open(repertoire+'/carte.txt', 'r', "utf-8")
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
	bg=writeSubmarine(y,x, bg)

	affichage=''
	for j in range(len(bg)):
		ligne=''
		for i in range(len(bg[j])):
		    ligne=ligne+bg[j][i]
		ligne=ligne+'\n'
		affichage=affichage+ligne

	print affichage


	return bg

#def getChar(bg,x,y):
	#renvoie le contenu d une case donnee
#	return (bg["map"][y-1][x-1])
