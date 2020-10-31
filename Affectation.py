__author__ = 'pehladik'

#TODO : interface qui permet de faire les changements en ligne
#TODO : garder trace des modifications
#TODO : prendre en compte les departs ensemble

import xlwt
from constantes import *
from TableauDepart import TableauDepart
from TableauEtudiant import TableauEtudiant
import os

# Fonction de comparaison des classements etudiant
def cmpval(x, y):
    if x.classement < y.classement:
        return -1
    elif x.classement == y.classement:
        return 0
    else:
        return 1


def run(listeEtdudiant, listeUniversite):
    #listeEtdudiant.sort(cmpval)
    listeEtdudiant.sort(key=lambda b: b.classement)
    for e in listeEtdudiant:
        affecterProgramme(e, listeUniversite)
        #print e

def writeHTMLReport(listeEtudiant, listeUniversite):
    report = open("./report.html", "w")
    report.write("<!DOCTYPE html>\n<html>\n<meta charset=\"UTF-8\">\n")
    report.write(open("./script.txt",'r').read())

    report.write("<head>\n<!-- En-tete du document  -->\n")

    separateur = ""
    for i in range (0, len(listeEtudiant)):
        report.write(separateur + "<a href=#" + str(i) + ">" + str(i) + "</a>" )
        separateur = ", "

    idx = 0
    for e in listeEtudiant:
        report.write("<p>")
        report.write("<a name=" + str(idx) + ">" + str(idx) + ".</a> ")
        report.write("<strong>")
        report.write(e.nom + " ")
        report.write(e.prenom + " ")
        report.write("</strong>")
        report.write("(" + e.filieractuelle + ", ")
        report.write(str(round(e.classement,3)*100) + "%) ")
        if e.choixfinal is not None:
            if e.choixfinal == 'rien':
                report.write("n'a obtenu <strong><span style=\"color:#FF0000\"> aucune affectation</span></strong> en " + e.filiere)
            else:
                univ = next(u for u in listeUniversite if u.est_present(e.choixfinal))
                idxu = listeUniversite.index(univ)
                #report.write("est affect&eacute;(e) en " + e.filiere + " &agrave; <a href=./univ/univ" + str(idxu) + ".html>"+ e.choixfinal.encode('utf-8') + "</a>  (choix " + str(e.numChoix()) + ")")
                #report.write("Affectation " + " (choix " + str(e.numChoix()) + ") : <a href=./univ/univ" + str(idxu) + ".html>"+ e.choixfinal.encode('utf-8') + "</a>")
                if e.filieractuelle != "":
                    act = str(int(e.filieractuelle[0])+1)
                else:
                    act =""
                report.write("est affect&eacute;(e) en " + act  + e.filiere + " &agrave; ")
                report.write("<a href=./univ/univ" + str(idxu) + ".html>"+ e.choixfinal + "</a>")
                report.write(" (choix " + str(e.numChoix()) + ")")
        else :
            report.write(" <strong><span style=\"color:#FF0000\"> => problem</span></strong>")
        report.write("</p>")

        #report.write("<a href=\"\" onclick=\"bascule('div" + str(idx) + "'); return false;\">Explications</a>\n")
        #report.write("<div id='div" + str(idx) + "' style='display:none;'>")

        idxexpli = 1
        report.write("<ul>")
        for explication in e.explicationsChoix:
            univ = next(u for u in listeUniversite if u.est_present(e.choixUniv(idxexpli)))
            idxu = listeUniversite.index(univ)
            if explication == PAS_DE_PLACE:
                report.write("<li>Pas de place a <a href=./univ/univ" + str(idxu) + ".html>"+ univ.nom + "</a>")
                report.write("<ul><li>Places occupees : ")
                separateur = ''
                for k,v in univ.listePlaceOccuppeesParFiliere.items():
                    if ((v != 0) and (v != -1)):
                        report.write(separateur + k + " (" + str(v) +')')
                        separateur = ', '
                if (len(univ.listeEtudiantsAffectes) != 0):
                    report.write(" | dernier : " + str(round(univ.listeEtudiantsAffectes[-1].classement*100,1)))
                report.write("</li><li>")
                separateur = ''
                for p in univ.listeDesProgrammes:
                    report.write(separateur + str(p))
                    separateur = ' | '
                report.write("</li></ul></li>")
            elif explication == PAS_DE_PROGRAMME:
                report.write("<li>Pas de programme pour la filiere ")
                report.write(e.filiere)
                report.write(" a <a href=./univ/univ" + str(idxu) + ".html>"+ univ.nom + "</a></li>")
            elif explication == AFFECTATION:
                report.write("<li>Affectation a <a href=./univ/univ" + str(idxu) + ".html>"+ univ.nom + "</a></li>")
            idxexpli += 1

        report.write("</ul>")

        #report.write(e.explications.replace('\n','</br>').encode('utf-8'))
        #report.write("</div>")

        idx += 1

    report.write("\n</head>\n</html>")
    report.close()

def writeHTMLReportUniversity(listeUniversite):
    if not os.path.isdir("./univ"):
        os.mkdir("./univ")

    idx = 0
    for u in listeUniversite:
        file = open("./univ/univ" + str(idx) + ".html", "w")
        file.write("<!DOCTYPE html>\n<html>\n<meta charset=\"UTF-8\">\n")
        file.write("<head>\n<!-- En-tete du document  -->\n")

        file.write("<h1>" + u.nom + "</h1>")
        file.write("<h3>Programmes</h3>")
        for p in u.listeDesProgrammes:
            file.write("<li>" + str(p) + "</li>")

        file.write("<h3>Etudiants</h3>")
        for e in u.listeEtudiantsAffectes:
            file.write("<li>" + e.nom + " " +e.prenom
                       + " (" + e.filiere + ", " + str(round(e.classement,3)*100) + "%) " "</li>")

        file.write("\n</head>\n</html>")
        file.close()
        idx += 1


def writeReport(listeEtudiant, listeUniversite):
    book = xlwt.Workbook()
    feuil1 = book.add_sheet(u'etudiants')

    #ajout des entetes
    feuil1.write(0,0,u'id')
    feuil1.write(0,1,u'nom')
    feuil1.write(0,2,u'prenom')
    feuil1.write(0,3,u'classement')
    feuil1.write(0,4,u'filiere')
    feuil1.write(0,5,u'filiere actuelle')
    feuil1.write(0,6,u'choix')
    feuil1.write(0,7,u'explication')

    #ajout des valeurs
    idx = 1
    for e in listeEtudiant:
        feuil1.write(idx, 0, e.id)
        feuil1.write(idx, 1, e.nom)
        feuil1.write(idx, 2, e.prenom)
        feuil1.write(idx, 3, e.classement)
        feuil1.write(idx, 4, e.filiere)
        if e.filieractuelle != None:
            feuil1.write(idx, 5, e.filieractuelle)
        feuil1.write(idx, 6, e.choixfinal)
        style = xlwt.XFStyle()
        style.alignment.wrap = 1
        feuil1.write(idx, 7, e.explications, style)

        idx += 1

    feuil2 = book.add_sheet(u'universite')

     #ajout des entetes
    feuil2.write(0,0,u'nom')
    for i in range(0, len(listeFilieres)):
        feuil2.write(0,i+1,listeFilieres[i])

    idx = 1
    for u in listeUniversite:
        feuil2.write(idx, 0, u.nom)
        for i in range(0, len(listeFilieres)):
            nbPlace = u.listePlaceOccuppeesParFiliere[listeFilieres[i]]
            if nbPlace == -1:
                nbPlace = 0
            feuil2.write(idx, i+1, nbPlace)
        idx += 1

    book.save('output.xls')

def affecterProgramme(etudiant, listeUniversite):
    explication = ""
    testFinAffectation = True
    numChoix = 0

    while (testFinAffectation):  # debut de l'affectation
        numChoix += 1
        if numChoix == 1:
            choix = etudiant.choix1
        elif numChoix == 2:
            choix = etudiant.choix2
        elif numChoix == 3:
            choix = etudiant.choix3
        else:
            choix = None

        if choix == None:
            etudiant.choixfinal = "rien"
            explication += "Aucun choix possible\n"
            testFinAffectation = False
            #break
        else:
            if not any (u.est_present(choix) for u in listeUniversite): # l'universite n'existe pas
                print ("choix " + str(numChoix) + " : univ : " + choix + " n'existe pas (" + etudiant.nom + ") ")
                break
                #quit()

            univ = next(u for u in listeUniversite if u.est_present(choix))
            placeDisponible = univ.isPlace(etudiant.filiere)
            if placeDisponible == PAS_DE_PROGAMME_ADEQUAT: # Pas de programme pour cette filiere
                explication += "Pas de programme pour la filiere " + etudiant.filiere + " a " + choix + "\n"
                etudiant.explicationsChoix.append(PAS_DE_PROGRAMME)

            elif placeDisponible == 0: # plus de place disponible
                etudiant.explicationsChoix.append(PAS_DE_PLACE)

                explication += "choix " + str(numChoix) + " : plus de place sur " + choix + "\n\t|-> Places occupees : "
                u = next(u for u in listeUniversite if u.est_present(choix))
                separateur = ''
                for k,v in u.listePlaceOccuppeesParFiliere.items():
                    if ((v != 0) and (v != -1)):
                        explication += separateur + k + " (" + str(v) +')'
                        separateur = ', '
                if (len(u.listeEtudiantsAffectes) != 0):
                    explication += "| dernier : " + str(round(u.listeEtudiantsAffectes[-1].classement*100,1))
                else:
                    explication += "problem"
                explication += "\n\t|-> "
                separateur = ''
                for p in u.listeDesProgrammes:
                    explication += separateur + str(p)
                    separateur = ' | '
                explication += '\n'


            elif placeDisponible > 0:  # Il y a de la place
                etudiant.choixfinal = choix
                univ.ajouterEtudiant(etudiant)
                explication += "choix " + str(numChoix) + " : Affectation reussie a " + choix + "\n"
                etudiant.explicationsChoix.append(AFFECTATION)
                break

    etudiant.explications = explication
    print ("** Resultat pour " + etudiant.nom + " " + etudiant.prenom + " (" + etudiant.filiere +\
                  ", " + str(round(etudiant.classement*100,1)) + ")")
    print (explication)



tabdep = TableauDepart()
tabetud = TableauEtudiant()

print ("====== Lecture du tableau des departs ======")
tabdep.lectureTableau(u'./documents/depart.xlsx')
print ("====== Lecture du tableau des choix etudiants ======")
tabetud.lectureTableau(u'./documents/etudiants.xlsx')

print ("====== Affectation des choix ======")
run(tabetud.listeEtudiants, tabdep.listeUniversite)

writeReport(tabetud.listeEtudiants, tabdep.listeUniversite)
writeHTMLReport(tabetud.listeEtudiants, tabdep.listeUniversite)
writeHTMLReportUniversity(tabdep.listeUniversite)

