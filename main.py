#coding: utf-8

#modules externes
import sys
import os
import time
import select
import tty
import termios

#mes modules
import background
import collision_environement

reglages_origine=termios.tcgetattr(sys.stdin)
#termios.tcsetattr(sys.stdin, termios.TCSADRAIN, reglages_origine())
variables={'time':0,
            'life':1,
            'o2':100
}
def interact(iteration_boucle):
	#gestion des evenement clavier
	#si une touche est appuyee
    t0=time.time()


    map='c.txt'
    #INITIALISATION
    if(iteration_boucle==0):
        reload(sys) #changement encodage terminal
        sys.setdefaultencoding('utf-8')
        #clear()

        background.create(map) #creation de la carte
        background.display_map() #affichage
        tty.setcbreak(sys.stdin.fileno())


    if isData():
        print 'ENTREE DETECTEE'
        entree=sys.stdin.read(1)[0]
        while entree != chr(27) and time.time()-t0<0.1:

            if(entree=='Z' or entree=='z'):     #test des touches, on attend que l'utilisateur choisisse une touche
                y,x=background.getPosition()	#pour se déplacer
                collision_environement.up(y,x, map)

            elif(entree=='S' or entree=='s'):
                y,x=background.getPosition()
                collision_environement.down(y,x, map)

            elif(entree=='Q' or entree=='q'):
                y,x=background.getPosition()
                collision_environement.left(y,x, map)

            #elif(entree=='m' or entree=='M'):
                #print background.getPosition()

            elif (entree=='D' or entree=='d'):
                y,x=background.getPosition()
                collision_environement.right(y,x, map)



            #collision_environement.oxygene()
    		#Mode affichage
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, reglages_origine)
            clear()
            background.create(map)
            background.display_map()
            tty.setraw(sys.stdin)
            entree=sys.stdin.read(1)[0]
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, reglages_origine)
        if (entree==chr(27)):
            quit()

    else:
        #print 'Pas d\'entree'
        pass


    tps_execution=float(time.time()-t0)

    if(tps_execution<0.1):
        time.sleep(0.1-tps_execution)


def isData():
	#recuperation evenement clavier
	return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

'''
def show():
    timer=1
    time.sleep()
    timer=timer-0.5
    sys.stdout.write("\033[1;1H")
    sys.stdout.write("\033[2J")

    sys.stdout.write("\033[14;25H")
    sys.stdout.write("\033[1m"+"Time")
    timer="\033[0m"+str(timer)
    sys.stdout.write("\033[15;25H")
    sys.stdout.write(timer)
'''
def init():

    reload(sys)
    sys.setdefaultencoding('utf8')
    tty.setraw(sys.stdin)

    repertoire=os.path.dirname(os.path.abspath(__file__))




def clear():
    sys.stdout.write("\033[1;1H")
    sys.stdout.write("\033[2J")

def run():
    iteration=0
    y,x=background.getPosition()
    while True:
        interact(iteration)
        iteration+=1
        #print iteration
        #collision_environement.oxygene()
        if(iteration>=2):
            o2=collision_environement.getO2()
            print o2
            collision_environement.setO2(o2-1)
            iteration=1


def quit():
    sys.stdout.write("\033[37m")
    sys.stdout.write("\033[40m")
    sys.exit()


run()
