 #coding: utf8

import sys
import time
import os
import time
import codecs
import string


plateau=[]
for i in range (30):
    plateau.append([' ']*100)

def clear(UI_file, plateau): #Effacer la console entre les mouvements
    load_board(UI_file, plateau)
    display_map(plateau)
    for i in range(30):
        print '\n'

def display_map(plateau): #Afficher la caractere
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, get_orig_settings())
        out=''
        for j in range (0,len(plateau[j])):
                if(plateau[j][i]=='@'):
                    out=out+'_'
                elif(plateau[j][i]=='&'):
                    out=out+'|'
                elif(plateau[j][i]=='*'):
                    out=out+' '
                elif(plateau[j][i]=='A' and j==1):
                    out=out+'-'
                else:
                    out=out+str(plateau[j][i])
        #out=out+'\n'
        print out+'\n'
