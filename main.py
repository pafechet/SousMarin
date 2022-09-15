# coding: utf-8

# modules externes
import sys, importlib, os, time, select, tty, termios, codecs, json, entrees
# mes modules
import background, collision_environement

ITERATIONS = 10
objectif = 0
objectifs_list = []
reglages_origine = termios.tcgetattr(sys.stdin)
repertoire = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    importlib.reload(sys)

    print('TESTS')
    plate = background.create('c.txt')
    if (plate[1][0] != '~'):
        print('background.create test error')

    plate = background.writeSubmarine(15, 15, plate)
    if (plate[16][15] != '8'):
        print('background.get/set position error')

    background.setPosition(4, 25)
    if (background.getPosition() != (4, 25)):
        print('background.get/setPosition() test error')

    collision_environement.setO2(87)
    if (collision_environement.getO2() != 87):
        print('collision_environement : get/setO2 test error')

    collision_environement.setVies(10)
    if (collision_environement.getVies() != 10):
        print('collision_environement :get/setVies test error')

    print('Fin des tests')


def init():
    importlib.reload(sys)

    entrees.chargement_fichier()


def isData():  # recuperation evenement clavier
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])


def menu():
    init()
    map = 'menu.txt'
    background.display_submap(map)  # affichage
    entree = ''
    while (entree != 'exit'):
        if (entree == 'play' or entree == 'PLAY'):
            run()
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, reglages_origine)
            background.display_submap(map)
        elif (entree == 'controls' or entree == 'CONTROLS'):
            print('Z,Q,S,D pour se déplacer')
        elif (entree == 'quit' or entree == 'QUIT'):
            quit()
        entree = input('Choix : ')
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, reglages_origine)


def interact(iteration_boucle):
    # gestion des evenement clavier
    # si une touche est appuyee
    t0 = time.time()
    map = 'c.txt'
    # INITIALISATION
    if (iteration_boucle == 0):
        importlib.reload(sys)  # changement encodage terminal
        background.create(map)  # creation de la carte
        background.display_map()  # affichage
        tty.setcbreak(sys.stdin.fileno())

    if isData():
        entree = sys.stdin.read(1)

        if (entree == chr(27)):
            return "EXIT"

        elif (entree == 'Z' or entree == 'z'):  # test des touches, on attend que l'utilisateur choisisse une touche
            y, x = background.getPosition()  # pour se déplacer
            collision_environement.up(y, x, map)


        elif (entree == 'S' or entree == 's'):
            y, x = background.getPosition()
            collision_environement.down(y, x, map)

        elif (entree == 'Q' or entree == 'q'):
            y, x = background.getPosition()
            collision_environement.left(y, x, map)

        elif (entree == 'm' or entree == 'M'):
            print(background.getPosition())

        elif (entree == 'D' or entree == 'd'):
            y, x = background.getPosition()
            collision_environement.right(y, x, map)

            # collision_environement.oxygene()
        # Mode affichage
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, reglages_origine)
        background.create(map)
        background.display_map()
        tty.setcbreak(sys.stdin.fileno())


    else:
        # print 'Pas d\'entree'
        pass

    # Affichage, works, ne pas changer
    y, x = background.getPosition()
    if (iteration_boucle >= ITERATIONS and y > 5):
        collision_environement.oxygene()

        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, reglages_origine)
        background.create(map)
        background.display_map()
        tty.setcbreak(sys.stdin.fileno())

    tps_execution = float(time.time() - t0)

    if (tps_execution < 0.1):
        time.sleep(0.1 - tps_execution)


def clear():
    sys.stdout.write("\033[1;1H")
    sys.stdout.write("\033[2J")


def run():
    iteration = 0
    while True:

        if (collision_environement.getVies() == 0):
            collision_environement.setVies(10)
            collision_environement.setO2(100)
            background.display_submap('lost.txt')
            entree = sys.stdin.read(1)
            if (entree == '\n'):
                background.display_submap('menu.txt')  # affichage
                break
                run()
        else:
            a = interact(iteration)
            if (a == 'EXIT'):
                break
            y, x = background.getPosition()
            if (y < 5):
                iteration = 1
                collision_environement.setO2(100)

            # Réserve d'oxygene sous l'eau
            elif (x <= 167 and x >= 152 and y >= 27 and y <= 31):
                if (x == 153):
                    entrees.set_objectif(1)
                iteration = 1
                collision_environement.setO2(100)

            else:
                if (y >= 89 and x <= 61):
                    entrees.set_objectif(2)
                elif (y >= 89 and x >= 250):
                    entrees.set_objectif(3)
                elif (y >= 45 and y <= 60 and x >= 40 and x <= 90):
                    entrees.set_objectif(4)

                iteration += 1
                if (iteration > ITERATIONS):
                    iteration = 0


def quit():
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, reglages_origine)
    sys.stdout.write("\033[37m")
    sys.stdout.write("\033[40m")
    sys.exit()


menu()
