__author__ = 'pehladik'

from TableauDepart import TableauDepart
from TableauEtudiant import TableauEtudiant
from Affectation import *

tabdep = TableauDepart()
tabetud = TableauEtudiant()

print "====== Lecture du tableau des departs ======"
tabdep.lectureTableau(u'./documents/depart.xlsx')
print "====== Lecture du tableau des choix etudiants ======"
tabetud.lectureTableau(u'./documents/etudiants.xlsx')

#for u in tabdep.listeUniversite:
#    print u

#for e in tabetud.listeEtudiants:
#    print e


print "====== Affectation des choix ======"
run(tabetud.listeEtudiants, tabdep.listeUniversite)

writeReport(tabetud.listeEtudiants, tabdep.listeUniversite)

