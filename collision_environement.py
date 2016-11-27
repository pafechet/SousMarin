#coding: utf8

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

def moveLeft(y,x):
    a=background.create(0)
    #print a
    #print y,x
    obstacle=False
    for i in range (y-3, y+2): #hauteur du sous marin
        #print obstacle
        #print a[i][x-1]+'@'
        if a[i][x-1] in [' ', '~']:
            pass
        else: #(y,x)!=' ':
            obstacle=True
    return not obstacle

def left(y,x):
    if moveLeft(y,x):
        background.setPosition(y,x-1)

def moveRight(y,x):
    a=background.create(0)
    #print a
    #print y,x
    obstacle=False
    for i in range (y-3, y+2): #hauteur du sous marin
        print obstacle
        #print a[i][x-1]+'@'
        if a[i][x+23] in [' ', '~']:
            pass
        else: #(y,x)!=' ':
            obstacle=True
    return not obstacle

def right(y,x):
    if moveRight(y,x):
        background.setPosition(y,x+1)

def moveDown(y,x):
    a=background.create(0)
    #print a
    #print y,x
    obstacle=False
    for i in range (x, x+22): #longeur du sous marin
        print obstacle
        #print a[i][x-1]+'@'
        if a[y+2][i] in [' ','~']:
            pass
        else: #(y,x)!=' ':
            obstacle=True
    return not obstacle

def down(y,x):
    if moveDown(y,x):
        background.setPosition(y+1,x)

def moveUp(y,x):
    a=background.create(0)
    #print a
    #print y,x
    obstacle=False
    for i in range (x, x+22): #longeur du sous marin
          #print a[i][x-1]+'@'
        if a[y-4][i] in [' ','~']:
            pass
        else: #(y,x)!=' ':
            obstacle=True
    return not obstacle

def up(y,x):
    if moveUp(y,x):
        background.setPosition(y-1,x)
