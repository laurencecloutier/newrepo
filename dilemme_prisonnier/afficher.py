from psychopy import visual, event, core
from PIL import Image
import numpy as np

# fonction qui affiche seulement l'intro
def boite_intro(win):
    intro = "LE DILEMME DU PRISONNIER:\nCette expérience est une variation du jeu du dilemme du prisonnier. "\
       	"Le but du jeu est d'amasser plus d'argent que votre adversaire. À chaque essai, vous avez le choix " \
       	"entre coopérer avec l'adversaire ou tricher. Si vous coopérez les deux, vous gagnez la même somme d'argent " \
       	"si vous coopérez alors que l'adversaire triche, celui-ci gagne tout l'argent et vous, rien. L'inverse se passe si " \
       	"vous trichez alors que l'adversaire coopère. Enfin, lorsque les deux trichez, personne ne reçoit d'argent. " \
        "Pour continuer, appuyez sur une touche."
    txt = visual.TextBox(
        window=win, text=intro, font_size=18,font_color=[1,1,1], 
        border_color=[1,1,1], textgrid_shape=[100,20], color_space='rgb', 
        size =(1.8,.1), pos=(0,0), grid_horz_justification='left',
        grid_vert_justification='center')
    txt.draw()
    win.flip()
    event.waitKeys()

# fonction qui affiche du texte
def boite_texte(win,text):
    txt = visual.TextBox(
        window=win, text=text, font_size=18, font_color=[1,1,1], 
        border_color=[1,1,1], textgrid_shape=[100,20], color_space='rgb', 
        size =(1.8,.1), pos=(0,0), grid_horz_justification='center', 
        grid_vert_justification='center')
    txt.draw()
    win.flip()

# écrit le résultat de l'utilisateur et de l'ordi
def resultat(win,user,ordi):
    gagne = "Bravo, vous avez gagné! Vous avez amassé {}$ contre {}$.".format(user,ordi)
    perdu = "Vous avez perdu... Votre adversaire a gagné {}$, tandis que vous avez obtenu {}$.".format(ordi,user)
    egal = "Égalité. Vous avez les deux: {}$.".format(user)
    if user>ordi:
        boite_texte(win,gagne)
    elif ordi>user:
        boite_texte(win,perdu)
    else:
        boite_texte(win,egal)

# fonction pour afficher les visages
def visage(path, win):
    im = Image.open(path)
    image = np.array(im)
    image_np = image.astype(np.float64)/255
    image_np = np.flip(image_np, axis=0)
    profil = visual.ImageStim(win=win,
                image = image_np,
                size = (512,512), 
                colorSpace='rgb1')
    visage = profil.draw()
    return visage