__author__ = 'pehladik'

import xlrd
from Etudiant import Etudiant
from constantes import *

def remplaceFiliere(etudiant):
    if etudiant.filiere == '':
        print ("ATTENTION: pas de filiere pour " + etudiant.nom)
        etudiant.filiere = u'toto'
    else:
        etudiant.filiere = dicoFilieresEuuivalente[etudiant.filiere]

class TableauEtudiant:

    def __init__(self):
        self.listeEtudiants= []

    def lectureTableau(self, nom_fichier):
        '''
        Rempli la liste des etudiants a partir du fichier specifie en parametre
        :param nom_fichier: fichier excel contenant l'ensemble des etudiants et de leur choix
        :return:
        '''
        wb = xlrd.open_workbook(nom_fichier)
        #print wb.sheet_names()

        # Premiere passe creation des etudiants par nom
        sh = wb.sheet_by_name(u'moveon')
        for i in range(1,sh.nrows):
            id = sh.cell_value(i, idx_etudiant_id)
            if not any(t.est_present(id) for t in self.listeEtudiants):
                nom = sh.cell_value(i, idx_etudiant_nom)
                prenom = sh.cell_value(i, idx_etudiant_prenom)
                filiere = sh.cell_value(i, idx_etudiant_filiere)
                classement = sh.cell_value(i, idx_etudiant_classement)
                if classement == 42:
                    print ("ATTENTION l(" + str(i+1) +"): pas de classement pour " + nom)
                    classement = 0.5
                etudiant = Etudiant(id, nom, prenom, classement, filiere, None, None, None)
                etudiant.filieractuelle = filiere
                remplaceFiliere(etudiant) #remplace la filiere par la liste
                self.listeEtudiants.append(etudiant)

        # Second parcours pour remplir les choix
        for i in range(1, sh.nrows):
            id = sh.cell_value(i, idx_etudiant_id)
            ordre = sh.cell_value(i, idx_etudiant_ordre)
            choix = sh.cell_value(i, idx_etudiant_choix)
            if ordre == 1:
                next(e for e in self.listeEtudiants if e.est_present(id)).choix1 = choix
            elif ordre == 2:
                next(e for e in self.listeEtudiants if e.est_present(id)).choix2 = choix
            elif ordre == 3:
                next(e for e in self.listeEtudiants if e.est_present(id)).choix3 = choix

