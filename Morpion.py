                        ###############################################
                        #                   Morpion                   #
                        ###############################################
#  Tasks:

# Opti fonctions check
# Bot intelligent

################################### Imports ######################################

from random import randint
from time import sleep

##################################################################################


######################## Fonctions principales ###################################

def jeu_2_joueurs():
    joueur = 2
    tableau = [[ " " for _ in range(3)] for _ in range(3)]
    for _ in range(9):
        joueur = joueur_switch(joueur)
        coup_joueur = coup()
        while coup_possible(coup_joueur,tableau) == False:
            print("Vous ne pouvez pas jouer la")
            coup_joueur = coup()
        actu_grille(tableau, coup_joueur, joueur)
        afficher_grille(tableau)
        if gagner(tableau) == True:
            print(f"Le joueur {joueur} a gagné")
            return
    print("Ex-Aequo")




def jeu_joueur_bot():
    joueur = 2
    tableau = [[ " " for _ in range(3)] for _ in range(3)]
    for _ in range(9):
        joueur = joueur_switch(joueur)
        if joueur == 1:
            coup_joueur = coup()
            while coup_possible(coup_joueur,tableau) == False:
                print("Vous ne pouvez pas jouer la")
                coup_joueur = coup()
            actu_grille(tableau, coup_joueur, joueur)
            afficher_grille(tableau)
        else:
            print("Le bot joue...")
            sleep(2)
            coup_joueur = coup_bot(tableau)
            actu_grille(tableau, coup_joueur, joueur)
            afficher_grille(tableau)
        if gagner(tableau) == True:
            print(f"Le joueur {joueur} a gagné")
            return
    print("Ex-Aequo")







####################### Fonctions auxiliaires ############################




def joueur_switch(last_player):
    if last_player == 1:
        return 2
    else:
        return 1


def coup():
    coup_l = int(input("Dans quelle ligne jouez-vous? "))
    coup_c = int(input("Dans quelle colonne jouez-vous? "))
    return coup_l, coup_c


def actu_grille(grille, coup, joueur):
    if joueur == 1:
        grille[coup[0]-1][coup[1]-1] = "X"
    else:
        grille[coup[0]-1][coup[1]-1] = "O"


def afficher_grille(grille):
    for i in range(3):
        print(grille[i])


def gagner(grille):
    if diag_gagnee(grille) == True:
        return True
    elif col_gagnee(grille) == True:
        return True
    elif lig_gagnee(grille) == True:
        return True
    else:
        return False


def diag_gagnee(grille):
    if grille[0][0] == grille[1][1] == grille[2][2] == "X" or grille[2][0] == grille[1][1] == grille[0][2] == "X":
        return True
    elif grille[0][0] == grille[1][1] == grille[2][2] == "O" or grille[2][0] == grille[1][1] == grille[0][2] == "O":
        return True
    else:
        return False


def col_gagnee(grille):
    if grille[0][0] == grille[0][1] == grille[0][2] == "X" or grille[0][0] == grille[0][1] == grille[0][2] == "O":
        return True
    elif grille[1][0] == grille[1][1] == grille[1][2] == "X" or grille[1][0] == grille[1][1] == grille[1][2] == "O":
        return True
    elif grille[2][0] == grille[2][1] == grille[2][2] == "X" or grille[2][0] == grille[2][1] == grille[2][2] == "O":
        return True
    else:
        return False


def lig_gagnee(grille):
    if grille[0][0] == grille[1][0] == grille[2][0] == "X" or grille[0][0] == grille[1][0] == grille[2][0] == "O":
        return True
    elif grille[0][1] == grille[1][1] == grille[2][1] == "X" or grille[0][1] == grille[1][1] == grille[2][1] == "O":
        return True
    elif grille[0][2] == grille[1][2] == grille[2][2] == "X" or grille[0][2] == grille[1][2] == grille[2][2] == "O":
        return True
    else:
        return False
    
    
def coup_possible(coup_joue, grille):
    if not(0<coup_joue[0]<4) or not(0<coup_joue[1]<4):
        return False
    elif grille[coup_joue[0]-1][coup_joue[1]-1] == "X" or grille[coup_joue[0]-1][coup_joue[1]-1] == "O":
        return False
    else:
        return True
    

################## BOT ##########################
    
def coup_bot(grille):
    coup_alea = (randint(1,3),randint(1,3))
    while coup_possible(coup_alea, grille) == False:
        coup_alea = (randint(1,3),randint(1,3))
    return coup_alea
    

    
    