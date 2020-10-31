__author__ = 'pehladik'

import xlrd
from Universite import Universite
from Programme import Programme
from constantes import *

class TableauDepart:
    
    def __init__(self):
        self.listeUniversite = []

    def ajoutUniversite(self, universite):
        self.listeUniversite.append(universite)

    def __str__(self):
        st = ''
        for u in self.listeUniversite:
            st += u.__str__() + "\n "
        return st
        
    def lectureTableau(self, nom_fichier):
        wb = xlrd.open_workbook(nom_fichier)
        sh = wb.sheet_by_name(u'Echange')
        #premiere phase : creation des universites sans les programmes
        for i in range(1,sh.nrows-1):
            nom_univ = sh.cell_value(i,idx_depart_nom_univ)
            if not any(u.est_present(nom_univ) for u in self.listeUniversite):
            #if not (nom_univ in self.listeUniversite):
                univ = Universite(nom_univ)
                self.ajoutUniversite(univ)
        #print self.__str__()
        #seconde phase : on cree les programmes
        for i in range(1,sh.nrows-1):
            nom_univ = sh.cell_value(i,idx_depart_nom_univ)
            if nom_univ.find('\n') !=  -1:
                print ("ATTENTION l(" + str(i+1) + ")" ": saut a la ligne dans le nom")
            specialites = sh.cell_value(i,idx_depart_specialite)
            if specialites.find('\n') !=  -1:
                print ("ATTENTION l(" + str(i+1) + ")" ": saut a la ligne dans la specialite")
            #print nom_univ + " " + specialites
            if specialites == 'Toutes':
                listeSpecialites = listeFilieres
            else:
                specialites = specialites.replace(' ','')
                listeSpecialites = specialites.split(',')

            nbPlaces = 0;
            for j in range(0, 15):
                n = sh.cell_value(i, 7 + j)
                if type(n) == float:
                    nbPlaces += int(n)
                elif type(n) == str:
                    if n == u'ND':
                        nbPlaces = ND
            if nbPlaces == 0:
                print ("ATTENTION l(" + str(i+1) +"): programme sans place")
            programme = Programme(nbPlaces, listeSpecialites)
            self.listeUniversite[[u.nom for u in self.listeUniversite].index(nom_univ)].ajouterProgramme(programme)
                # TODO : diffencier les programmes en fonction des PO et des filieres (introduire PO-diff)
                # TODO : mettre le nombre de places


        #print self.__str__()
        
        