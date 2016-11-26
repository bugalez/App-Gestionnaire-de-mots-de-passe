import pickle

class ManipFichier():
    """
        classe permettant la manipulation dans des fichiers
           - Lecture écriture dans un fichier
    """
    
    def __init__(self, nomFichier, dico):
        self.nomFichier = nomFichier
        self.dico = dico
        
    def lireFichier(self):
        with open(self.nomFichier, 'rb') as fichier:
            mon_depickler =  pickle.Unpickler(fichier)
            self.varmdp = mon_depickler.load()
            return self.varmdp

    def ecrireFichier(self):
        with open(self.nomFichier, 'wb') as fichier:
            mon_pickler = pickle.Pickler(fichier)
            mon_pickler.dump(self.dico)
        

