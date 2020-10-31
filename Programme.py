__author__ = 'pehladik'

from Etudiant import Etudiant
from constantes import *


class Programme:
    def __init__(self, nb_places, liste_filierees):
        self.nbDePlaces = nb_places
        self.listeDesFilieres = liste_filierees
        self.listeEtudiantsAffectes = []

    def __str__(self):
        st = "filieres: "
        separateur = ''
        if len(self.listeDesFilieres) == len(listeFilieres):
            st+= 'Toutes'
        else:
            for f in self.listeDesFilieres:
                st += separateur + f
                separateur = ', '
        st += " (" + str(self.nbDePlaces) +")"
        return st

    def ajoutEtudiant(self, etudiant):
        self.listeEtudiantsAffectes.append(etudiant)

    def afficherListeDesEtudiants(self):
        st = 'Liste des etudiants'
        for e in self.listeEtudiantsAffectes:
            assert isinstance(e.nom, Etudiant)
            st += ": " + e.nom
        print (st)