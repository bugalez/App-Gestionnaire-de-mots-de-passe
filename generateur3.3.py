#generateur 3.3

#!/usr/bin/python3.5
#-*-coding: utf8-*-


from tkinter import *
from tkinter.messagebox import *
import tkinter as tk
import random
from random import randint
import os
from os.path import exists
import pickle
from login import Logingconf
from manipFichier import ManipFichier
from verif import Logingtest
import time

global mdp, adresse, fichier, nom, motsDePasse,ok

fichier = "/donnee"
adresse = os.getcwd() + fichier
mdp= ""
ok = False

main=Tk()
main.geometry("600x600+200+200")
main.title("Générateur de mots de passe v3.3")

#def alert():
    #askokcancel("alerte", "Voulez vous vraiment effacer {}!".format(nom.get()))

def Intercepte(): 
    """
       fonction qui permet de supprimer le fichier
       cookie quand on clique sur la croix de la
       fenêtre 
    """
    adresse = os.getcwd() + "/cookie" #/cookie
    testFichier = exists(adresse)           # Test si le fichier existe retourne True si il existe
    if testFichier == True:    
        os.remove('cookie')
        main.destroy()
    else:
        main.destroy()
 
def detruire():
    adresse = os.getcwd() + "/cookie" #/cookie
    testFichier = exists(adresse)           # Test si le fichier existe retourne True si il existe
    if testFichier == True:    
        os.remove('cookie')
        main.destroy()
    else:
        main.destroy()
    

def afficher():
        ok = False
        """
           fonction qui affiche les mots de passes
           stocker dans un fichier
           
        """
        
        if ok == False:

            adresse = os.getcwd() + "/cookie"
            testFichier = exists(adresse)           # Test si le fichier existe retourne True si il existe
            if testFichier == False:
                Logingtest()
                time.sleep(1)
                diccook={}
                manip =ManipFichier(adresse, diccook)
                diccook=manip.lireFichier()
                if "ok" in diccook.values():
                    ok=True
                    #root.update()

                
            
            

        
        adresse = os.getcwd() + "/donnee"    # definit ou le fichier sera créer
        motsDePasse={}
        manip =ManipFichier(adresse, motsDePasse)
        motsDePasse=manip.lireFichier()
        ztext.delete("0.0",END)
        
        for cle,valeur in motsDePasse.items():
            ztext.insert('end',cle +":" +valeur + '\n')
            
        

def enregistrer(nom, mdp):
        ok = False
        """
           Fonction qui enregistre les mots de passe et les noms
        """
        if ok == False:

            adresse = os.getcwd() + "/cookie"
            testFichier = exists(adresse)           # Test si le fichier existe retourne True si il existe
            if testFichier == False:
                Logingtest()
                time.sleep(1)
                diccook={}
                manip =ManipFichier(adresse, diccook)
                diccook=manip.lireFichier()
                if "ok" in diccook.values():
                    ok=True



        
        adresse = os.getcwd() + "/donnee"
        testFichier = exists(adresse)           # Test si le fichier existe retourne True si il existe
        if testFichier == False:

            motsDePasse = {}
            motsDePasse[nom]= mdp
            manip =ManipFichier(adresse, motsDePasse) # Créer le fichier si il n'existe pas
            manip.ecrireFichier()
                
                
        else:
            motsDePasse = {}
            manip =ManipFichier(adresse, motsDePasse)
            motsDePasse=manip.lireFichier()
            
            for i in dict(motsDePasse):
                if i == nom:
                    if askokcancel("Attention", "Voulez vous vraiment \n modifiez <{}> ?".format(nom)):
                        motsDePasse[nom]= mdp
                        manip =ManipFichier(adresse, motsDePasse)
                        manip.ecrireFichier()
                                                        

                    else:
                        ztext.insert('end','Opération annulée' + '\n')
                else:
                    motsDePasse[nom]= mdp
                    with open(adresse, 'wb') as fichier:
                        mon_pickler = pickle.Pickler(fichier)
                        mon_pickler.dump(motsDePasse)
                        
                                  
       
def copier():
        """
           Permet de copier le résultat dans le presse papier
        """
        #main.clipboard_clear()  # efface le presse-papier
        #main.clipboard_append(mot.get())# Envois le résultat dans le presse papier
        # effacer l'éventuel contenu précédent du clipboard
        main.clipboard_clear()
        try:
            # saisir la sélection s'il y en a une (sinon -> except)
            t = main.selection_get()
            # et envoyer le texte sélectionné dans le clipboard
            main.clipboard_append(t)
        except:
            pass

        
def generateur(nom, nb, valeur, valeur1, valeur2 ):
        global mdp
        
        """
            Fonction qui est charger de générer des mots de passes
            - Trois options sont possible en fonction des boutons
            radios coché
              - Majuscule
              - Minuscule
              - Caractères spéciaux
              retourne le mots de passe générer associer au 'nom' entrer
        """
        if nb >= 8 and nb <= 50:
        

                
                nom = nom                                       # Choix du nom 
                nb = nb                                         # Choix du nombres de caractéres
                valeur = valeur                                 # Active les caractères spéciaux
                valeur1 = valeur1                               # Active les majuscules
                valeur2 = valeur2                               # Active les chiffres
         

         
                
                chaine = "abcdefghijklmnopqrstuvwxyz"
                chaineCart = "@&éèçàâå€çþýûîôÂøÊðÛÎÔ"
                        

                            
                low = list(chaine.lower())                         # liste de caractères minuscules
                lup= list(chaine.upper())                          # liste de caractères majuscules
                lcarspec = list(chaineCart)                        # liste de caractères spéciaux
                lint = list(range(1, 10))                          # liste de nombres

                
                low*=5
                lup*=5
                lcarspec*=6
                lint*= 7    


                
                low1 = random.sample(low, nb)             # tirage aléatoire dans la liste
                lup1 = random.sample(lup, nb)             # selon le choix de l'utilisateur
                lcarspec = random.sample(lcarspec, nb)
                lint = random.sample(lint, nb)


                if valeur == 1 and valeur1 == 0 and valeur2 == 0 :      # Choix d'activation des cases à cochés
                        listeAléatoire =  low1 + lcarspec
                                
                                
                elif valeur1 == 1 and valeur == 0 and valeur2 == 0:
                        listeAléatoire =  low1 + lup1
                                
                                
                elif valeur2 == 1 and valeur== 0 and valeur1 == 0:
                        listeAléatoire =  low1 + lint
                                
                                
                elif valeur == 1 and valeur1 == 1 and valeur2 == 0:
                        listeAléatoire =  low1 + lcarspec + lup1
                                
                                
                elif valeur == 1 and valeur2 == 1 and valeur1 == 0:
                        listeAléatoire =  low1 + lcarspec + lint
                                
                                
                elif valeur1 == 1 and valeur2 == 1 and valeur == 0:
                        listeAléatoire =  low1 + lup1 + lint
                                
                                
                elif valeur == 1 and valeur1 == 1 and valeur2 == 1:
                        listeAléatoire =  low1 + lcarspec + lup1 + lint
                                
                                
                else:
                        listeAléatoire =  low1                                     # liste par default
                                

                random.shuffle(listeAléatoire)                      
                listeAléatoire = random.sample(listeAléatoire, nb)
                listeAléatoire = [str(i) for i in listeAléatoire]
                mdp = ''.join(listeAléatoire)
                mdp = mdp.replace(' ','')
                mot.set(nom +":"+ mdp )                                           # Retourne la chaine mdp concaténé avec le nom
                #mdp1.set(mdp)
                return mdp
                #print(mdp)

        else:
                mot.set("La valeur doit être comprise entre 8 et 50")
                



      
#mdp1 =  StringVar()             
valeur2 = IntVar()     # chiffres selection
valeur1 = IntVar()      # majuscule selection
valeur = IntVar()       # caractères spéciaux selection
mot = StringVar()       # variable stockant le mots de passe retourné par la fonction generateur
nom = StringVar()       # variable stockant le nom entrer par l'utilisateur
nb= IntVar()            # variable stockant le nombre entrer par l'utilisateur


Frame1 = Frame(main, borderwidth=2, relief=GROOVE)
Frame1.grid(row= 0, column=0, pady=50, padx= 20)

Frame2 = Frame(main, borderwidth=2, relief=GROOVE)
Frame2.grid(row= 1, column=0, padx=40, pady=20)


Frame3 = Frame(main, borderwidth=2, relief=GROOVE)
Frame3.grid(row= 3, column=0, padx=20, pady=10)


Frame4 = Frame(main, borderwidth=2, relief=GROOVE)
Frame4.grid(row= 2,column=0, padx=10, pady=10)

Frame5 = Frame(main)
Frame5.grid(row= 4, column=0, padx=10, pady=10)


nom.set('Nom')
texte =Entry(Frame1, textvariable=nom )
texte['font']= 'Helvetica', '10'
texte.grid()


nb.set(8)
texte1 =Entry(Frame1, textvariable=nb)
texte1['font']= 'Helvetica', '10'
texte1.grid()
main.bind("<Return>", lambda :generateur(nom.get(), nb.get(), valeur.get(), valeur1.get(), valeur2.get()))



mot.set('Selectionner le résultat et CTRL C pour copier')
label1 = Entry(Frame2, textvariable = mot, bg="black")
label1['font']= 'Helvetica', '10'
label1['fg'] = 'white'
label1['width'] = '40'
label1['justify'] = 'center'
label1.grid(row = 0, column =1)

ztext= Text(Frame3, height= 15, width= 80)
#ztext['font']= 'Helvetica', '10'
#ztext = ScrolledText.vbar
ztext.grid()


Checkbutton(Frame4, text="caractères spéciaux", variable=valeur).grid(row = 1, column =0)
Checkbutton(Frame4, text="Majuscules", variable=valeur1).grid(row = 1,column =1)
Checkbutton(Frame4, text="chiffres", variable=valeur2).grid(row = 1,column =2)



bouton1 = Button(Frame4, text = 'Generer', command= lambda:generateur(nom.get(), nb.get(), valeur.get(), valeur1.get(), valeur2.get()))
bouton1.grid(row = 2, column =2, padx =40, pady =0)
bouton2 = Button(Frame5, text = 'Quittez', command= detruire)
bouton2.grid(padx=10,pady=1)
bouton3 = Button(Frame4, text = 'Copier', command = copier)
bouton3.grid(row = 2, column =0)

menubar = Menu(main)
menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Nouvelle Utilisateur", command=Logingconf)
menu1.add_command(label="Sauvergarder", command= lambda:enregistrer(nom.get(), mdp))
menu1.add_command(label="Afficher", command=lambda:afficher())
#menu1.add_command(label="Afficher", command=log)
menu1.add_command(label="Login", command=Logingtest)
menu1.add_separator()
menu1.add_command(label="Quitter", command= detruire)#main.destroy)
menubar.add_cascade(label="Fichier", menu=menu1)

main.config(menu=menubar)

# create a menu
popup = Menu(main, tearoff=0)
popup.add_command(label="Sauvergarder", command= lambda:enregistrer(nom.get(), mdp)) # , command=next) etc...
popup.add_command(label="Afficher", command=lambda:afficher())
popup.add_command(label="Copier", command=copier)
popup.add_command(label="Exit", command=popup.quit)
popup.add_separator()
popup.add_command(label="Quitter", command= detruire)

def do_popup(event):
    # display the popup menu
    try:
        popup.tk_popup(event.x_root, event.y_root+30, 0)
    finally:
        # make sure to release the grab (Tk 8.0a1 only)
        popup.grab_release()

main.bind("<Button-3>", do_popup)

main.protocol("WM_DELETE_WINDOW", Intercepte) 

main.mainloop()









