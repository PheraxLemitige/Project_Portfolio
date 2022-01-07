#%%
from numpy import *
import random as rd
from tkinter import *
import time
#creation du damier
def creation_damier (): 
    """
    Ce programme crée un damier vide 
    return : 
        tableau
    """
    damier = zeros ((8, 8), dtype = int)
    return damier

#placement des pieces

#pion
def placement_pion(damier):
    """
    Cette fonction place les pions dans le damier
    """
    for i in range (8):
        damier[1, i] = 1 + i
        damier[6, i] = 17 + i

#tour
def placement_tour(damier):
    """
    Cette fonction place les tours dans le damier
    """
    damier[0,0] = 9
    damier[0,7] = 10
    damier[7,0] = 25
    damier[7,7] = 26

#Cheval
def placement_cheval(damier):
    """
    Cette fonction place les chevaux dans le damier
    """
    damier[0,1] = 11
    damier[0,6] = 12
    damier[7,1] = 27
    damier[7,6] = 28

#fou
def placement_fou(damier):
    """
    Cette fonction place les fous dans le damier
    """
    damier[0,2] = 13
    damier[0,5] = 14
    damier[7,2] = 29
    damier[7,5] = 30

#reine
def placement_reine(damier):
    """
    Cette fonction place les reines dans le damier
    """
    damier[0,3] = 15
    damier[7,3] = 31

#roi
def placement_roi(damier):
    """
    Cette fonction place les rois dans le damier
    """
    damier[0,4] = 16
    damier[7,4] = 32

def placement (damier):
    placement_pion(damier)
    placement_tour(damier)
    placement_cheval(damier)
    placement_fou(damier)
    placement_reine(damier)
    placement_roi(damier)

def trouver_piece (damier, nbr_piece):
    for x in range (8):
        for y in range (8):
            if damier[x, y] == nbr_piece:
                return x, y

def direction (damier, piece, x, y):
    x_piece, y_piece = trouver_piece(damier, piece)
    direction_x = 0
    direction_y = 0
    if x_piece - x < 0:
        direction_x =  1
    elif x_piece - x > 0:
        direction_x = - 1
    else:
        direction_x = 0
    if y_piece - y < 0:
        direction_y = 1
    elif y_piece - y > 0:
        direction_y = - 1
    else:
        direction_y = 0
    return direction_x, direction_y

#deplacement d'une piece

    #savoir si un coup est possible

        #case existe
def case_existe (x, y):
    if x >= 8 or x < 0 or y >= 8 or y < 0:
        return False
    else:
        return True

        #si case vide
def case_vide_allier (damier, x, y, couleur):
    """
    J'envoie True si la case et vide ou False si la case n'est pas vide
    """
    if couleur == 'noir':
        return not 0 < damier[x, y] < 17
    else:
        return not 16 < damier [x, y] < 33

def case_vide_enemie (damier, x, y, couleur):
    """
    J'envoie True si la case et vide ou False si la case n'est pas vide
    """
    if couleur == 'blanc':
        return  0 < damier[x, y] < 17
    else:
        return  16 < damier [x, y] < 33

        #si porté
    

            #pion
def porter_pion (damier, piece, x, y, couleur):
    x_piece, y_piece = trouver_piece(damier, piece)
    deplacement = x - x_piece
    if (y_piece + 1 == y or y_piece - 1 == y) and x_piece + deplacement == x and case_vide_enemie(damier, x, y, couleur):
        return True
    elif  deplacement == 2 or deplacement == -2:
        return case_vide_allier(damier, x, y, couleur) and case_vide_allier(damier, x_piece + deplacement // 2, y_piece, couleur) and (x_piece == 6 or x_piece == 1)
    elif deplacement == 1 or deplacement == -1:
        return case_vide_allier(damier, x, y, couleur) and y == y_piece
    else:
        return False

            #tour
def porter_tour (damier,piece, x, y,couleur):
    x_tour, y_tour = trouver_piece(damier, piece)
    if x - x_tour == 0:
        deplacement = abs(y - y_tour)
    else:
        deplacement =abs(x - x_tour)
    direc_x , direc_y = direction(damier, piece, x, y)
    if x_tour != x and y_tour != y:
        return False
    elif x_tour == x and y_tour == y:
        return False
    else:
        for case in range(1, deplacement):
            if not case_vide_allier(damier,x_tour + (case * direc_x), y_tour + (case * direc_y), couleur):
                return False
        if not case_vide_allier(damier, x, y, couleur):
            return False
        else:
            return True
            #cheval
def porter_cheval (damier, piece, x, y, couleur):
    x_cheval, y_cheval = trouver_piece(damier, piece)
    if not case_vide_allier(damier, x, y, couleur):
        return False
    elif x_cheval + 2 == x and (y_cheval + 1 == y or y_cheval - 1 == y):
        return True
    elif x_cheval - 2 == x and (y_cheval + 1 == y or y_cheval - 1 == y):
        return True
    elif y_cheval + 2 == y and (x_cheval + 1 == x or x_cheval - 1 == x):
        return True
    elif y_cheval - 2 == y and (x_cheval + 1 == x or x_cheval - 1 == x):
        return True
    else:
        return False
            #fou
def porter_fou (damier, piece, x, y, couleur):
    x_fou, y_fou = trouver_piece(damier, piece)
    direc_x, direc_y = direction(damier, piece, x, y)
    deplacement = abs(x_fou - x)
    if abs(x_fou - x) != abs(y_fou - y):
        return False
    else:
        for case in range(1, deplacement):
            if not case_vide_allier(damier,x_fou + (case * direc_x), y_fou + (case * direc_y), couleur):
                return False
        if not case_vide_allier(damier, x, y, couleur):
            return True
        else:
            return False


    
            #reine
def porter_reine (damier, piece, x, y, couleur):
    return porter_fou(damier, piece, x, y, couleur) or porter_tour(damier, piece, x, y, couleur)
    
            #roi
def porter_roi (damier, piece, x, y, couleur):
    x_roi, y_roi = trouver_piece(damier, piece)
    if not case_vide_allier(damier, x, y, couleur):
        return False
    elif x_roi - x < -1 or x_roi - x > 1 or y_roi - y < -1 or y_roi - y > 1:
        return False
    else:
        return True

def porter (nbr_piece, x, y, damier, couleur):
    if nbr_piece < 9 or 16 < nbr_piece < 25:
        return porter_pion(damier, nbr_piece, x, y, couleur)
    elif 8 < nbr_piece < 11 or 24 < nbr_piece < 27:
        return porter_tour(damier, nbr_piece, x, y, couleur)
    elif 10 < nbr_piece < 13 or 26 < nbr_piece < 29:
        return porter_cheval(damier, nbr_piece, x, y, couleur)
    elif 12 < nbr_piece < 15 or 28 < nbr_piece < 31:
        return porter_fou(damier,nbr_piece, x, y, couleur)
    elif nbr_piece == 15 or nbr_piece == 31:
        return porter_reine(damier, nbr_piece, x, y, couleur)
    else:
        return porter_roi(damier,nbr_piece, x, y, couleur)

    #verifier si piece adverse prise
def peut_avancer(damier, nbr_piece, x, y, couleur):
    return case_existe(x, y) and porter(nbr_piece, x, y, damier, couleur)

def deplacer (damier, nbr_piece, x, y):
    x_piece, y_piece = trouver_piece(damier, nbr_piece)
    damier[x_piece, y_piece] = 0
    damier[x, y] = nbr_piece

#tour de joueur(change de joueur)

def tour_joueur (joueur_actuel):
    if joueur_actuel == 1:
        return 2
    else:
        return 1



#demande de coordonnees

def verif_exit (x, y):
    if x == 'EXIT' or y == 'EXIT':
        return True
    else:
        return False
def verif_lettre (tour):
    dico = 'ABCDEFGH'
    lettre = input("Quelle est la lettre de l'endroit voulu?")
    if not lettre in dico:
        while not lettre == 'EXIT' and not lettre in dico:
            if tour == 1:
                lettre = input("Quelle est la lettre de la piece a deplacer?")
            else:
                lettre = input("Quelle est la lettre de l'endroit voulu?")
    return lettre



def demande_case_existe (x, y, tour):
    dico_lettre = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6, 'H' : 7, 'EXIT' : 'EXIT'}
    while not verif_exit(x, y) and not case_existe(x, y) :
                print("Cette case n'existe pas. Si vous vous etes trompe de piece marquer EXIT.")
                if tour == 1:
                    x = input("Quel est le chiffre de la piece a deplacer?")
                else:
                    x = input("Quel est le chiffre de l'endroit voulu?")
                y = verif_lettre (tour)
                if not verif_exit(x, y):
                    x = int(x) - 1
                    y = dico_lettre[y]
    return x, y

def pas_piece (x, y, joueur, damier, tour):
    dico_lettre = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6, 'H' : 7, 'EXIT' : 'EXIT'}
    nbr_piece = damier[x, y]
    if joueur == 1:
        while not verif_exit(x, y) and not 0 < nbr_piece < 17:
            print("Cette piece n'est pas la votre. Si vous vous etes trompe de piece marquer EXIT.")
            x = input("Quel est le chiffre de la piece a deplacer?")
            y = verif_lettre (tour)
            if not verif_exit(x, y):
                x = int(x) - 1
                y = dico_lettre[y]
                nbr_piece = damier[x, y]
    if joueur == 2:
        while not verif_exit(x, y) and not 16 < nbr_piece < 33:
            print("Cette piece n'est pas la votre. Si vous vous etes trompe de piece marquer EXIT.")
            x = input("Quel est le chiffre de la piece a deplacer?")
            y = verif_lettre (tour)
            if not verif_exit(x, y):
                x = int(x) - 1
                y = dico_lettre[y]
                nbr_piece = damier[x, y]
    return x, y


def demande_piece (joueur, damier):
    dico_lettre = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6, 'H' : 7, 'EXIT' : 'EXIT'}
    x = input("Quel est le chiffre de la piece a deplacer?")
    y = verif_lettre (1)
    if not verif_exit(x, y):
        x = int(x) - 1
        y = dico_lettre[y]
        if not verif_exit(x, y) or not case_existe(x, y):
            x, y = demande_case_existe(x, y, 1)
        if not verif_exit(x, y):
            x ,y = pas_piece(x, y, joueur, damier, 1)
        return x, y    
    else:
        return x, y

def demande_porter(nbr_piece, damier, couleur, x, y):
    dico_lettre = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6, 'H' : 7}
    while not verif_exit(x, y) and not peut_avancer(damier, nbr_piece, x, y, couleur):
            print("La piece n'a pas la portee. Si vous vous etes trompe de piece marque EXIT.")
            x = input("Quel est le chiffre de l'endroit voulu?")
            y = verif_lettre (2)
            if not verif_exit(x, y):
                x = int(x) - 1
                y = dico_lettre[y]
                nbr_piece = damier[x, y]
    return x, y

def demande_cordonnee (damier, joueur):
    dico_lettre = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6, 'H' : 7, 'EXIT' : 'EXIT'}
    if joueur == 1:
        couleur = 'noir'
    else:
        couleur = 'blanc'
    x = input("Quel est le chiffre du deplacement voulu")
    y = verif_lettre (2)
    if not verif_exit(x, y):
        x = int(x) - 1
        y = dico_lettre[y]
        if not case_existe(x, y):
            x, y = demande_case_existe(x, y, 2)
    if not verif_exit(x, y):
        nbr_piece = damier[x, y]
        if not peut_avancer(damier, nbr_piece, x, y, couleur):
            x, y = demande_porter(nbr_piece, damier, couleur, x, y)
    return x, y

def demande (joueur, damier):
    x, y = demande_piece(joueur, damier)
    x_voulu, y_voulu = demande_cordonnee(damier, joueur)
    while verif_exit(x, y) or verif_exit(x_voulu, y_voulu):
        x, y = demande_piece(joueur, damier)
        x_voulu, y_voulu = demande_cordonnee(damier, joueur)
    nbr_piece = damier[x, y]
    return nbr_piece, x_voulu, y_voulu
#affichage du damier et des pieces
def donne_symbole (damier, x, y):
    if 0< damier[x, y] < 9:
        return '♟'
    elif 16 < damier[x, y] < 25:
        return '♙'
    elif 8 < damier[x, y] < 11:
        return '♜'
    elif 24 < damier[x, y] < 27:
        return '♖'
    elif 10 < damier[x, y] < 13:
        return '♞'
    elif 26 < damier[x, y] < 29:
        return '♘'
    elif 12 < damier[x, y] < 15:
        return '♝'
    elif 28 < damier[x, y] < 31:
        return '♗'
    elif damier[x, y] == 15:
        return '♛'
    elif damier[x, y] == 31:
        return '♕'
    elif damier[x, y] == 16:
        return  '♚'
    elif damier[x, y] == 32:
        return '♔'
    else:
        return ' '
def affichage (damier):
    print('    A | B | C | D | E | F | G | H ')
    print(' -----------------------------------')
    i = 1
    for ligne in range (8):
        l = str(i+ligne)+' | '
        for colonne in range(8):
            l = l + donne_symbole(damier, ligne, colonne) + '  |'
        print(l)
        print(' -----------------------------------')
    print()
#jouer au echec
def jouer ():
    echequier = creation_damier()
    placement(echequier)
    player = 1
    affichage(echequier)
    arret = 'non'
    perdu = ''
    while not arret == 'oui' :
        print('Au tour du joueur ' + str(player))
        piece, co_x, co_y = demande(player, echequier)
        deplacer(echequier, piece, co_x, co_y)
        player = tour_joueur(player)
        affichage(echequier)
        arret = input('Il y a echec et mat ou pas?')
        if arret == 'oui':
            perdu = input('Quel joueur a perdu?')
    if perdu == '1':
        print('Joueur 2 a gagne!')
    else:
        print('Joueur 1 a gagne!')

jouer()
# %%
