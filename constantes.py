__author__ = 'pehladik'


# liste des filieres a l'INSA
listeFilieres = ['IC-GC', 'IC-GM', 'IMACS-GP', 'IMACS-AE', 'MIC-IR', 'MIC-MM', 'ICBE-GB', 'ICBE-GPE',
                 'GPE', 'GB', 'GC', 'GM', 'AE', 'GP', 'IR', 'GMM', 'toto']
dicoFilieresEuuivalente = {u'3IC_GM':u'GM',u'2IC-GC':u'IC-GC',u'2MIC_MM':u'MIC-MM',u'4AE':u'AE',u'2IC_GM':u'IC-GM',
                           u'2IMACS_AE':u'IMACS-AE',u'2ICBE_GBA':u'ICBE-GB',u'4GC':u'GC',u'2IMACS_GP':u'IMACS-GP',
                           u'2ICBE_GPE':u'ICBE-GPE',u'3IMACS_AE':u'AE',u'3IC-GC':u'GC',u'3MIC_IR':u'IR',
                           u'2MIC_IR':u'MIC-IR',u'3IMACS_GP':u'GP',u'3MIC_MM':u'GMM',u'4GM':u'GM',u'3ICBE_GPE':u'GPE',
                           u'3ICBE_GBA':u'GB',u'4IR':u'IR',u'4BI':u'GB',u'4GP':u'GP',u'4PR':u'GPE',u'4MM':u'GMM',
                           u'3IC_GC':u'GC',u'5BI':u'GB',u'5AE':u'AE',u'1A_GM':u'IC-GM',u'5GC':u'GC',u'5GM':u'GM',
                           u'1A_GPE':u'ICBE-GPE'}

#index dans les fichiers excel des etudiants
idx_etudiant_id = 6
idx_etudiant_nom = 0
idx_etudiant_prenom = 1
idx_etudiant_ordre = 8
idx_etudiant_choix = 16
idx_etudiant_filiere = 23
idx_etudiant_classement = 15

#index dans le fichier excel des departs
idx_depart_nom_univ = 2
idx_depart_specialite = 4

#constantes
PAS_DE_PROGAMME_ADEQUAT = -1000
ND = 10

#constantes choix
PAS_DE_PROGRAMME = 0
PAS_DE_PLACE = 1
AFFECTATION = 2