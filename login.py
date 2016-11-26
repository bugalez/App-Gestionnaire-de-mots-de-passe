#!/usr/bin/python3.5
#-*-coding:UTF-8-*-

from tkinter import *
from tkinter.messagebox import *
from getpass import getpass
import hashlib
from manipFichier import ManipFichier



class Logingconf(ManipFichier):
    def __init__(self):
        self.root=Tk()
        self.root.geometry("250x100+200+200")
        self.root.title("login")

        self.login= Entry(self.root )
        self.login.grid(row= 0, column= 1)
        self.passw= Entry(self.root,show="*" )
        self.passw.grid(row= 1, column=1)
        self.valider= Button(self.root,text="valider", command= self.crypt)
        self.valider.grid(row=3, column=1)
        self.lablogin=Label(self.root, text="Login")
        self.lablogin.grid(row=0, column=0)
        self.labpassw = Label(self.root, text="Password")
        self.labpassw.grid(row=1, column=0)

        #self.root.mainloop()
        
    def crypt(self):

        self.chaine_login = self.login.get()
        #self.chaine_login= self.chaine_login.encode()
        #self.login_chiffre = hashlib.sha1(self.chaine_login).hexdigest()

        self.conf = "conf"
        
        self.passd = self.passw.get() # mots de passe entrer
        # On encode la saisie pour avoir un type bytes
        self.passd = self.passd.encode()
        self.passd_chiffre = hashlib.sha1(self.passd).hexdigest()
        #self.varcrypt= (self.login_chiffre, self.passd_chiffre)
        self.varcrypt= {self.chaine_login: self.passd_chiffre}
        ManipFichier(self.conf, self.varcrypt).ecrireFichier()
        #self.crypt.ecrireFichier()
        
        
        self.root.destroy()

