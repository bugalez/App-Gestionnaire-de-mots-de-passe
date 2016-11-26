from tkinter import *
from tkinter.messagebox import *
from getpass import getpass
import hashlib
from manipFichier import ManipFichier
import pickle

global ok,chaine_login

class Logingtest(ManipFichier):
    """
        classe qui instantie un objet fenêtre 
        recupère les entrées login et password
        et les comparent avec les données stocké
        dans un fichier
    """

    def __init__(self):
        #self.commande= commande
        self.root=Tk()
        self.root.geometry("250x100+200+200")
        self.root.title("login")

        self.login= Entry(self.root )
        self.login.grid(row= 0, column= 1)
        self.passw= Entry(self.root,show="*" )
        self.passw.grid(row= 1, column=1)
        self.valider= Button(self.root,text="valider", command= self.testcrypt)
        self.valider.grid(row=3, column=1)
        self.lablogin=Label(self.root, text="Login")
        self.lablogin.grid(row=0, column=0)
        self.labpassw = Label(self.root, text="Password")
        self.labpassw.grid(row=1, column=0)
        

    def testcrypt(self):
        
        self.chaine_login = self.login.get()
        #self.chaine_login= self.chaine_login.encode()
        #self.login_chiffre = hashlib.sha1(self.chaine_login).hexdigest()

        self.conf = "conf"
            
        self.passd = self.passw.get() # mots de passe entrer
        # On encode la saisie pour avoir un type byte
        self.passd = self.passd.encode()
        self.passd_chiffre = hashlib.sha1(self.passd).hexdigest()
        #self.varcrypt= (self.login_chiffre, self.passd_chiffre)
        self.dicovarcrypt= {self.chaine_login: self.passd_chiffre}
        
        self.varcrypt = "test"
        self.dicologinfichier={}
        
        with open(self.conf, 'rb') as fichier:
            mon_depickler =  pickle.Unpickler(fichier)
            self.dicologinfichier = mon_depickler.load()

        self.var1=self.dicovarcrypt[self.chaine_login]
        try:
            self.var2=self.dicologinfichier[self.chaine_login]
        except KeyError:
            self.var2 = None
        
        
        if self.var1 == self.var2:
            fichier= "cookie"
            cook ={}
            cook[self.chaine_login]="ok"
            manip=ManipFichier(fichier,fichier)
            manip.ecrireFichier()


        else:
            self.ok =False
            
            #Appel le fichier login.py pour s'enregistrer


        self.root.destroy()
