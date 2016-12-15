#coding: utf-8

#modules externes
import sys
import os
import time
import select
import tty
import termios
import codecs
import json


ITERATIONS=6
objectif=0
objectifs_list=[]
repertoire=os.path.dirname(os.path.abspath(__file__))

def set_objectif(i):
    global objectif

    if(i<len(objectifs_list) and i==objectif+1):
        objectif=int(i)

def set_objectifs_list(data):
    global objectifs_list
    objectifs_list=data

def get_objectif():
    return objectif

def get_text_objectif():
    temp=get_objectif()
    return objectifs_list[temp]

def chargement_fichier():
    data_file=codecs.open(repertoire + '/objectives.json', 'r', encoding='utf-8')
    data = json.loads(data_file.read())
    if ('objectif' in data):
        set_objectif(data['objectif'])

    if('objectifs' in data):
        set_objectifs_list(data['objectifs'])
    data_file.close()
