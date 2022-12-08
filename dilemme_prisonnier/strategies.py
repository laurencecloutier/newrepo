# les différentes stratégies que l'ordi peut utiliser contre l'utilisateur
import random
import numpy as np

# stratégie tit for tat
def titfortat(choix_adversaire):
    if choix_adversaire == "commencer":
        return 1
    return int(choix_adversaire[0])
    #liste_choix = []
    #liste_choix.append(choix_adversaire)
    #if liste_choix==["1"]:
        #return liste_choix[-1]
    #    return 1
    #else:
    #    return 0
#    return 0


# coopère plus souvent
def random_coop():
    prob = random.choices([0,1], weights = (40,60)) [0]
    return str(prob)

def coop():
    return int(random_coop()[0])


# trahit plus souvent
def random_tricher():
    prob = random.choices([0,1], weights = (60,40)) [0]
    return str(prob)

def tricher():
    return int(random_tricher()[0])

