#/usr/bin/python3.5
#-*-coding:UTF-8-*-
    
    def copier():
        # effacer l'éventuel contenu précédent du clipboard
        clipboard_clear()
        try:
            # saisir la sélection s'il y en a une (sinon -> except)
            t = selection_get()
            # et envoyer le texte sélectionné dans le clipboard
            clipboard_append(t)
        except:
            pass
            
            
            
