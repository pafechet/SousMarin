# coding: utf-8
import sys, os, codecs, json, entrees

# le module background gere le type abstrait de donnee background
# un background contient une chaine de caractere qui represente
# une image de fond d ecran

import collision_environement

MAP_X = 355
MAP_Y = 120

position = [4, 60]
repertoire = os.path.dirname(os.path.abspath(__file__))


# fonction pour changer la position
def setPosition(y, x):
    global position
    position = [y, x]


def get_term_size():
    y, x = os.popen('stty size', 'r').read().split()
    x = int(x) - 3
    y = int(y) - 3
    return x, y


# fonction pour avoir la position dans la liste 'position' y au rang 0 et x au rang 1
def getPosition():
    return position[0], position[1]


# fonction qui permet d'écrire le sous marin dans le terminal
# le sous marin est sur le fond
def writeSubmarine(y, x, background):
    y = y - 3
    sousmarin = [
        '        _________      ',
        '    ___/  o o o  \___  ',
        '   /    ---------    \ ',
        '  |     ---------     |',
        '8-=\_________________/ ']

    for j in range(len(sousmarin)):  # longeur de la liste (ligne)
        for i in range(len(sousmarin[j])):  # longeur du nombre de caractères (colonnes)
            background[y + j][x + i] = sousmarin[j][i]
    return background


def create(carte):
    o2 = collision_environement.getO2()

    bg = []
    for j in range(MAP_Y):
        bg.append([''] * MAP_X)

    j = 0
    file_path = repertoire + '/' + carte

    f = codecs.open(file_path, 'r', encoding="utf-8")
    for line in f.readlines():
        j += 1
        i = 0
        for ch in line:

            if '\n' in ch:
                bg[j][i] = ' '
            else:
                bg[j][i] = ch
                i += 1
    f.close()
    y, x = getPosition()
    bg = writeSubmarine(y, x, bg)
    xmax = ymin = ymax = xmin = 0

    return bg


def display_submap(map):
    bg = []
    for j in range(MAP_Y):
        bg.append([''] * MAP_X)

    j = 0
    file_path = repertoire + '/' + map

    f = codecs.open(file_path, 'r', encoding="utf-8")
    for line in f.readlines():
        # print line
        j += 1
        i = 0
        for ch in line:

            if '\n' in ch:
                bg[j][i] = ' '
            else:
                # print j,i
                bg[j][i] = ch
                i += 1
    f.close()
    render_map(bg)


def display_map():
    y, x = getPosition()
    bg = create('c.txt')
    x_term = get_term_size()[0]
    y_term = get_term_size()[1]

    ymin = xmin = 0

    if (x - (x_term / 2) < 0):
        xmin = 0
    elif (x + x_term >= len(bg[0])):
        xmin = len(bg[0]) - x_term
    else:
        xmin = x - (60)

    if (y - (y_term / 2) < 0):
        ymin = 0
    elif (y + y_term >= len(bg)):
        ymin = len(bg) - y_term - 15
    else:
        ymin = y - 15
    render_map(bg, xmin, ymin, True)


def render_map(bg, xmin=0, ymin=0, display_o2=False):
    size = get_term_size()
    x_term = size[0]
    y_term = size[1]

    obj = entrees.get_text_objectif()
    ymax = 0
    if (ymin + y_term < MAP_Y):
        ymax = ymin + y_term
    else:
        ymax = MAP_Y

    xmax = 0
    if (xmin + x_term < MAP_X):
        xmax = xmin + x_term
    else:
        xmax = MAP_X

    affichage = ''
    for j in range(ymin, ymax):
        ligne = ''
        for i in range(xmin, xmax):
            ligne = ligne + bg[j][i]
        ligne = ligne + '\n'
        affichage = affichage + ligne

    if (display_o2):
        o2 = collision_environement.getO2()
        if (o2 >= 0):
            line = 'Air: ' + '❤  ' * int(o2 / 10) + '♡  ' * int(10 - o2 / 10)
            affichage = affichage + line + str(o2) + '\n'

        # Affiche les vies
        vies = collision_environement.getVies()
        if (vies >= 0):
            line = 'Vies:' + '❤  ' * (vies) + '♡  ' * (10 - vies)
            affichage = affichage + line + str(vies)

        affichage = affichage + '\nLEVEL ' + str(entrees.get_objectif()) + ' :' + obj

    print(affichage)
