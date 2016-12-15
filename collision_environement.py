#coding: utf-8

#modules externes
import sys
import os
import time
import select
import tty
import termios


import background

#dans ce dossier nous allons traiter des colisions
#il y aura l'environement

o2=100
vies=10
pression=0
items_to_pass=[' ', '~']

def getLife():
    return life

def setLife(l):
    global life
    life=int(l)

def getO2():
    return o2

def setO2(o):
    global o2
    o2=o

def oxygene():
    o2=getO2()
    y,x=background.getPosition()
    if y>4:
        setO2(o2-1)
        if(o2<0):
            if(o2%(-5)==0):
                setVies(getVies()-1)

    else:
        setO2(100)


def getVies():
    return vies

def setVies(o):
    global vies
    vies=o



def moveLeft(y,x, carte):
    a=background.create(carte)
    #print a
    #print y,x
    obstacle=False
    for i in range (y-3, y+2): #hauteur du sous marin
        #print obstacle
        #print a[i][x-1]+'@'
        if (a[i][x-1] in items_to_pass) and (a[i][x-2] in items_to_pass):
            pass
        else: #(y,x, carte)!=' ':
            obstacle=True
    return not obstacle

def left(y,x, carte):
    if moveLeft(y,x, carte):
        background.setPosition(y,x-2)

def moveRight(y,x, carte):
    a=background.create(carte)
    #print a
    #print y,x
    obstacle=False
    for i in range (y-3, y+2): #hauteur du sous marin
        #print obstacle
        #print a[i][x-1]+'@'
        if a[i][x+23] in items_to_pass and (a[i][x+24] in items_to_pass):
            pass
        else: #(y,x, carte)!=' ':
            obstacle=True
    return not obstacle

def right(y,x, carte):
    if moveRight(y,x, carte):
        background.setPosition(y,x+2)

def moveDown(y,x, carte):
    a=background.create(carte)
    #print a
    #print y,x
    obstacle=False

    for i in range (x, x+23): #longeur du sous marin
        #print obstacle
        #print a[i][x-1]+'@'
        if a[y+2][i] in items_to_pass:
            pass
        else: #(y,x, carte)!=' ':
            obstacle=True
    return not obstacle

def down(y,x, carte):
    if moveDown(y,x, carte):
        background.setPosition(y+1,x)

def moveUp(y,x, carte):
    a=background.create(carte)
    #print a
    #print y,x
    obstacle=False
    for i in range (x, x+23): #longeur du sous marin
          #print a[i][x-1]+'@'
        #print  a[y-4][i]
        if a[y-4][i] in items_to_pass:
            pass
        else: #(y,x, carte)!=' ':
            obstacle=True
    return not obstacle

def up(y,x, carte):
    if moveUp(y,x, carte):
        background.setPosition(y-1,x)
