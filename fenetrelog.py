class FenetreLog:
    
    def __init__(self, commande):
        self.commande= commande
        self.root=Tk()
        self.root.geometry("250x100+200+200")
        self.root.title("login")

        self.login= Entry(self.root )
        self.login.grid(row= 0, column= 1)
        self.passw= Entry(self.root,show="*" )
        self.passw.grid(row= 1, column=1)
        self.valider= Button(self.root,text="valider", command= self.commande)
        self.valider.grid(row=3, column=1)
        self.lablogin=Label(self.root, text="Login")
        self.lablogin.grid(row=0, column=0)
        self.labpassw = Label(self.root, text="Password")
        self.labpassw.grid(row=1, column=0)
