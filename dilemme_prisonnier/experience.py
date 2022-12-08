############
# Imports
############

import sys
import numpy as np
import random
from psychopy import visual, logging, event, monitors, core
import os
from PIL import Image
import strategies, afficher

##############################################
# Input arguments (sujet, session, condition)
##############################################
sujet = "1"  # premier argument est 1 et non 0

# paramètres qui vont être utilisés pour créer un fichier de résultats


#############################################################################################
#   créer un nom de fichier et vérifier si fichier existe; si existe déjà pourrait continuer
#############################################################################################

nom_fichier = f'exp_{sujet}.npy'

# vérifie si le fichier existe pour éviter de le supprimer ou, éventuellement,
# pour continuer l'expérience là où elle a été arrêtée
#if os.path.isfile(nom_fichier):
    #print(f'\n\nLe fichier \"{nom_fichier}\" existe déjà.\n')
    #quit()


#######################################################
#   seeder le générateur de nombres pseudo-aléatoires
#######################################################

np.random.seed()    # "Seed" le générateur de nombres pseudo-aléatoires
                    # état à sauvegarder à chaque fois qu'on appelle np.random.random
                    # (y compris dans la fonction de dithering)
                    # E.g. :    etat = np.random.get_state() 
                    #           test = np.random.random((1,3))
                    #           np.random.set_state(etat)
                    #           test2 = np.random.random((1,3))
                    # test et test2 sont identiques


######################################################
# ouvrir une fenêtre
######################################################

win = visual.Window(fullscr=True, 
    pos=[0,0], 
    screen=0, 
    units='pix', 
    color=[-1,-1,-1])
    
#######################################################
# définir l'expérience autant que possible dans une structure y compris states après appele à random.random ou dithering les réponses initialisées
#######################################################

nb_stimuli = 2      # visages
nb_conditions = 2   # stratégie coop ou tricher
nb_repetitions = 4 # nombre de fois que toutes les combinaisons précédentes sont répétées
nb_essais = nb_repetitions * nb_stimuli * nb_conditions
# 16 essais

# crée les VI (sans remise) et les sauvegarde dans le dictionnaire resultats

resultats = {}  # dictionnaire dans lequel on mettra les VI, les VD, 
                # les états du générateur de nombre peudo-aléatoire, etc.
                # Ce dictionnaire sera auvegardé à chaque essai.

# quel visage sera affiché
visage_aleatoire = []

visage_list = ["homme.png", "femme.png"]
quel_visage = random.choice(visage_list)

if quel_visage == "homme.png":
    visage_aleatoire = "h"
else:
    visage_aleatoire = "f"

# enregistre la condition visage dans le dictionnaire des résultats
resultats["visage_aleatoire"] = visage_aleatoire


# stratégie de l'ordinateur
strategie_aleatoire = []

coopere = strategies.coop()
tricher = strategies.tricher()
strat_list = [coopere, tricher]
strategie_aleatoire = random.choice(strat_list)

# enregistre la condition strategie dans le dictionnaire des résultats
resultats["strategie_aleatoire"] = strategie_aleatoire


#quelles_conditions = np.tile(quelles_conditions, nb_repetitions)

# crée un indice pour mélanger les essais 
indice = np.arange(nb_essais)
np.random.shuffle(indice)



#resultats['quelles_conditions'] = quelles_conditions

# les VD initialisées

choix_user = []
#strategie_user = np.empty((nb_essais))
#strategie_ordi = np.empty((nb_essais))

#resultats['strategie_user'] = strategie_user
#resultats['strategie_ordi'] = strategie_ordi
#resultats['TR'] = TR

# touches de réponse possibles
touches_de_reponse = ['0','1','escape']     # les touches permises : 
                                            # 0 = trahir; 
                                            # 1 = coopérer; 
                                            # Escape = quitte l'expérience



#######################################################
#   boucle principale: quel essai, quoi présenter, attendre réponse, tout sauvegarder essai par essai (écraser le précédent)
#######################################################

#staircase = data.QuestHandler(???
#resultats['staircase'] = staircase

# texte à présenter selon les essais
recherche_adversaire = "Recherche d'un adversaire en ligne..."
adversaire = "Voici votre adversaire:"
choix = "Faites un choix. Appuyez sur 0 pour trahir ou 1 pour coopérer"
coop = "Vous avez coopéré ensemble, vous gagnez 10$ chaque."
triche = "Vous avez les deux triché, personne ne reçoit d'argent."
ordi_triche = "Votre adversaire a triché, il reçoit 20$. Vous ne gagnez rien."
user_triche = "Vous avez triché, vous recevez 20$. Votre adversaire ne gagne rien."
ordi_triche_risque = "Votre adversaire a triché, il reçoit 20$. Vous perdez 10$."
user_triche_risque = "Vous avez triché, vous recevez 20$. Votre adversaire perd 10$."

# afficher le texte d'introduction
afficher.boite_intro(win)

# simulation de recherche d'adversaire en ligne
afficher.boite_texte(win, recherche_adversaire)
core.wait(3)
afficher.boite_texte(win, adversaire)
core.wait(2)


# affiche un des 2 visages
afficher.visage(quel_visage, win)
win.flip()
core.wait(2.5)


# initialisation des scores
score_user = 0
score_ordi = 0

afficher.boite_texte(win,choix) # demande de faire un choix
choix_user = event.waitKeys(keyList=touches_de_reponse)
choix_ordi = strategie_aleatoire # STRATEGIE DE L'ORDI

# boucle du tournoi entre  l'ordi et l'utilisateur
for essai in range(5): # 10 essais
    # les 2 coopèrent
    if choix_user == ["escape"]: # quitter l'expérience
        quit()
    if choix_user == ["1"] and choix_ordi == 1:
        score_user += 10
        score_ordi += 10
        afficher.boite_texte(win,coop)
        core.wait(3.5)
    # l'ordi triche
    elif choix_user == ["1"] and choix_ordi == 0: 
        score_ordi += 20
        afficher.boite_texte(win,ordi_triche)
        core.wait(3.5)
    # l'utilisateur triche
    elif choix_user == ["0"] and choix_ordi == 1: 
        score_user += 20
        afficher.boite_texte(win,user_triche)
        core.wait(3.5)
    # les 2 trichent
    elif choix_user == ["0"] and choix_ordi == 0: 
        afficher.boite_texte(win,triche)
        core.wait(3.5)
    afficher.boite_texte(win,choix) # demande de faire un choix
    dernier_choix = choix_user
    choix_ordi = strategie_aleatoire # STRATEGIE DE L'ORDI
    choix_user = event.waitKeys(keyList=touches_de_reponse)
    # sauvegarde la stratégie des 2 joueurs
    #strategie_user[essai] = dernier_choix
    #strategie_ordi[essai] = choix_ordi
    
    #resultats['touches'] = touches
    #resultats['strategie_ordi'] = choix_ordi

resultats["score_user"] = score_user
resultats["score_ordi"] = score_ordi
resultats["choix_user"] = choix_user

afficher.resultat(win, score_user, score_ordi) # affiche les résultats à l'écran
event.waitKeys()

np.load(nom_fichier, allow_pickle=True)
np.save(nom_fichier, resultats, allow_pickle=True) # suffit de faire : np.load(nom_fichier, allow_pickle=True) pour récupérer le dictionnaire
# sauvegarder dictionnaire resultats et donner nom au fichier, par défaut allow_pickle est faux
