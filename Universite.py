__author__ = 'pehladik'

from Programme import Programme
from constantes import *
from constraint import *


class Universite:
    def __init__(self, nom):
        self.nom = nom
        self.listeDesProgrammes = []
        self.listePlaceOccuppeesParFiliere = {}
        for f in listeFilieres:
            self.listePlaceOccuppeesParFiliere[f] = -1
        self.listeEtudiantsAffectes = []

    def __cmp__(self, nom):
        return cmp(self.nom, nom)

    def __str__(self):
        st = self.nom
        for p in self.listeDesProgrammes:
            st += '| '
            st += str(p)
        return st

    def est_present(self, nom):
        return (self.nom == nom)

    def ajouterProgramme(self, programm):
        self.listeDesProgrammes.append(programm)
        for f in programm.listeDesFilieres:
            self.listePlaceOccuppeesParFiliere[f] = 0

    def findProgramm(self, filiere):
        programme = None
        for p in self.listeDesProgrammes:
            if filiere in p.listeDesFilieres:
                programme = p
        return programme

    def ajouterEtudiant(self, etudiant):
        self.listeEtudiantsAffectes.append(etudiant)
        self.listePlaceOccuppeesParFiliere[etudiant.filiere] += 1

    def isPlace(self, filiere):
        result = 0
        if self.listePlaceOccuppeesParFiliere[filiere] == -1: # Pas de programme disponible dans la filiere
            result = PAS_DE_PROGAMME_ADEQUAT
        else: # le programme existe pour la filiere
            if len(self.listeDesProgrammes) == 1: # cas simple d'un seul programme dans l'universite
                nbPlacesOccupees = 0
                for f in self.listeDesProgrammes[0].listeDesFilieres:
                    nbPlacesOccupees += self.listePlaceOccuppeesParFiliere[f]
                result = self.listeDesProgrammes[0].nbDePlaces - nbPlacesOccupees

            else: # cas avec plusieurs programmes
                problem = Problem()
                i = 0
                # Pour chaque programme p de l'universite il faut que la somme des places occupees
                # ne depasse pas la capacite de p :
                #           sum_filiere(place[filiere][p]) < place_disponible[p]
                for p in self.listeDesProgrammes:
                    i += 1
                    lvar = []
                    for f in p.listeDesFilieres:
                        varname = f + str(i)
                        lvar.append(varname)
                        problem.addVariable(varname, range(0, p.nbDePlaces + 1))
                    # Contraintes sum (filiere) < nb places programme
                    # print lvar
                    v = p.nbDePlaces
                    #print "<= " + str(v)
                    problem.addConstraint(MaxSumConstraint(v), lvar)

                # Il faut que le nombre de place prises par filiere f soit exactement egal au nombre
                # d'etudiants qui occupent cette filiere (+1 pour la filiere a tester) :
                # sum(place[filiere]) = v
                for f in self.listePlaceOccuppeesParFiliere:
                    v = self.listePlaceOccuppeesParFiliere[f]
                    if self.listePlaceOccuppeesParFiliere[f] != -1:
                        lvar = []
                        i = 0
                        for p in self.listeDesProgrammes:
                            i += 1
                            if f in p.listeDesFilieres:
                                varname = f + str(i)
                                lvar.append(varname)
                        if len(lvar) != 0:
                            # print lvar

                            if f == filiere:
                                #print "= " + str(v+1)
                                problem.addConstraint(ExactSumConstraint(v + 1), lvar)
                            else:
                                #print "= " + str(v)
                                problem.addConstraint(ExactSumConstraint(v), lvar)

                solution = problem.getSolution() # recherche d'une solution
                if solution != None:
                    result = 1
            # print solution
        return result