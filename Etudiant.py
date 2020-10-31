__author__ = 'pehladik'

class Etudiant:
    def __init__(self, id, nom, prenom, classement, filiere, choix1, choix2, choix3):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.classement = classement
        self.filiere = filiere
        self.filieractuelle = None
        self.choix1 = choix1
        self.choix2 = choix2
        self.choix3 = choix3
        self.choixfinal = None
        self.explications = ''
        self.explicationsChoix = []

    def __str__(self):
        st = "id: " + str(self.id)
        st += ", nom: " + self.nom
        st += ", prenom: " + self.prenom
        st += ", classement: " + str(self.classement)
        st += ", filiere: " + self.filiere
        if self.choix1 != None:
            st += ", choix1: " + self.choix1
        if self.choix2 != None:
            st += ", choix 2: " + self.choix2
        if self.choix3 != None:
            st += ", choix3: " + self.choix3
        if self.choixfinal != None:
            st += ", choix: " + self.choixfinal
        return st

    def est_present(self, id):
        return (self.id == id)

    def numChoix(self):
        if self.choixfinal != None:
            if self.choix1 == self.choixfinal:
                return 1
            elif self.choix2 == self.choixfinal:
                return 2
            if self.choix3 == self.choixfinal:
                return 3
            else:
                return 4
        else :
            return 0

    def choixUniv(self, numUniv):
        if numUniv == 1:
            return self.choix1
        elif numUniv == 2:
            return self.choix2
        elif numUniv == 3:
            return  self.choix3


