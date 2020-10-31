__author__ = 'pehladik'

from TableauDepart import TableauDepart
from TableauEtudiant import TableauEtudiant
from Affectation import *


tabetud = TableauEtudiant()

tabetud.lectureTableau(u'./documents/etudiants.xlsx')

for e in tabetud.listeEtudiants:
    print e

#run(tabetud.listeEtudiants, tabdep.listeUniversite)