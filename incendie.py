#########################################
# groupe MPCI 4
# Elive DIPOKO
# Ali GOUMANE
# Marie PHILIBERT
# Stalin SIVASANGAR
#https://github.com/uvsq21916121/projet_incendie.git
#########################################



#importation des bibliothèques
import tkinter as tk
import random as rd

#DEFINITION DES CONSTANTES
HAUTEUR = 600
LARGEUR = 600
color_font = "white"
type_de_terrain = ["blue", "green"  , "yellow"]

largeur_parcelle = LARGEUR //100
hauteur_parcelle = HAUTEUR // 100

DUREE_FEU = 1
#DUREE_CENDRE = 500

etat= 100*[0]

for i in range(0,100):
    etat[i] = 100*[0]

#DEFINITION DES FONCTIONS
def choix_du_terrain():
    """initialisation du terrain """
    for i in range(100):
        for j in range(100):
            color = rd.choice(type_de_terrain)
            canvas.create_rectangle((i*largeur_parcelle, j*hauteur_parcelle),((i+1)*largeur_parcelle, (j+1)*hauteur_parcelle), fill=color)
            if (color == "blue"):
                etat[i][j] = 2
            if (color =="yellow"):
                etat[i][j] = 0
            if (color == "green"):
                etat[i][j] = 1
    print (etat[0][0])
    return

    





    
    


#PROGRAMME PRINCIPAL
racine = tk.Tk()
canvas = tk.Canvas (racine ,width =LARGEUR, height = HAUTEUR , bg = color_font)
bouton = tk.Button(racine , text ="Démarrer" ,command = choix_du_terrain, font = ("helvetica",30))
bouton.grid (column = 1,row = 6)
canvas.grid(column = 1 ,row = 1 ,rowspan = 5)
racine.mainloop()