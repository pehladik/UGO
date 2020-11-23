__author__ = 'pehladik'

# liste des filieres a l'INSA
listeFilieres = ['2ICBE_GB',
                 '2ICBE_GPE',
                 '2IC_GC',
                 '2IC_GM',
                 '2IMACS_AE',
                 '2IMACS_GP',
                 '2MIC_IR',
                 '2MIC_MA',
                 '2MIC_MM',
                 '3APP_GC',
                 '3APP_GM',
                 '3ICBE_GB',
                 '3ICBE_GPE',
                 '3IC_GC',
                 '3IC_GM',
                 '3IMACS_AE',
                 '3IMACS_GP',
                 '3MIC_IR',
                 '3MIC_MA',
                 '3MIC_MM',
                 '4AE',
                 '4GB',
                 '4GC',
                 '4APP_GC',
                 '4GPE',
                 '4GMM',
                 '4GM',
                 '4APP_GM',
                 '4GP',
                 '4IR',
                 '4GMA',
                 '5AE',
                 '5GB',
                 '5GC',
                 '5APP_GC',
                 '5GPE',
                 '5GMM',
                 '5GM',
                 '5APP_GM',
                 '5GP',
                 '5IR',
                 '5GMA',
                 'M1 DET',
                 'M1 FLUIDS',
                 'M1 ID-RIMS',
                 'M1 RT',
                 'M1 SMMS',
                 'M1 WATER',
                 'M2 DET',
                 'M2 FLUIDS',
                 'M2 SAFETY',
                 'M2 ID-RIMS',
                 'M2 RT',
                 'M2 SMMS',
                 'M2 WATER',
                 'toto']
dicoFilieresEuuivalente = {'2A Ingénierie Chimique, Biochimique et Environnement (ICBE_GB)': '2ICBE_GB',
                           '2A Ingénierie Chimique, Biochimique et Environnement (ICBE_GPE)': '2ICBE_GPE',
                           '2A Ingénierie de la Construction (IC_GC)': '2IC_GC',
                           '2A Ingénierie de la Construction (IC_GM)': '2IC_GM',
                           '2A Ingénierie des Matériaux, Composants et Systèmes (IMACS_AE)': '2IMACS_AE',
                           '2A Ingénierie des Matériaux, Composants et Systèmes (IMACS_GP)': '2IMACS_GP',
                           '2A Modélisation, Informatique et Communication (MIC_IR)': '2MIC_IR',
                           '2A Modélisation, Informatique et Communication (MIC_MA)': '2MIC_MA',
                           '2A Modélisation, Informatique et Communication (MIC_MM)': 'REVOIR',
                           '3A Génie Civil par Apprentissage': '3APP_GC',
                           '3A Génie Mécanique par Apprentissage': '3APP_GM',
                           '3A Ingénierie Chimique, Biochimique et Environnement (ICBE_GB)': '3ICBE_GB',
                           '3A Ingénierie Chimique, Biochimique et Environnement (ICBE_GPE)': '3ICBE_GPE',
                           '3A Ingénierie de la Construction (IC_GC)': '3IC_GC',
                           '3A Ingénierie de la Construction (IC_GM)': '3IC_GM',
                           '3A Ingénierie des Matériaux, Composants et Systèmes (IMACS_AE)': '3IMACS_AE',
                           '3A Ingénierie des Matériaux, Composants et Systèmes (IMACS_GP)': '3IMACS_GP',
                           '3A Modélisation, Informatique et Communication (MIC_IR)': '3MIC_IR',
                           '3A Modélisation, Informatique et Communication (MIC_MA)': '3MIC_MA',
                           '3A Modélisation, Informatique et Communication (MIC_MM)': 'REVOIR',
                           '4A Automatique et Electronique': '4AE',
                           '4A Génie Biologique': '4GB',
                           '4A Génie Civil': '4GC',
                           '4A Génie Civil par Apprentissage': '4APP_GC',
                           '4A Génie des Procédés': '4GPE',
                           '4A Génie Mathématique et Modélisation': 'REVOIR',
                           '4A Génie Mécanique': '4GM',
                           '4A Génie Mécanique par Apprentissage': '4APP_GM',
                           '4A Génie Physique': '4GP',
                           '4A Informatique et Réseaux': '4IR',
                           '4A Mathématiques Appliquées': '4GMA',
                           '5A Automatique et Electronique': '5AE',
                           '5A Génie Biologique': '5GB',
                           '5A Génie Civil': '5GC',
                           '5A Génie Civil par Apprentissage': '5APP_GC',
                           '5A Génie des Procédés': '5GPE',
                           '5A Génie Mathématique et Modélisation': 'REVOIR',
                           '5A Génie Mécanique': '5GM',
                           '5A Génie Mécanique par Apprentissage': '5APP_GM',
                           '5A Génie Physique': '5GP',
                           '5A Informatique et Réseaux': '5IR',
                           '5A Mathématiques Appliquées': '5GMA',
                           'M1 Dynamique des fluides, énergétique et transferts': 'M1 DET',
                           'M1 Fluids Engineering for Industrial Processes': 'M1 FLUIDS',
                           'M1 Ingénierie de la durabilité – recherche et innovation en matériaux et structures': 'M1 ID-RIMS',
                           'M1 Réseaux et télécommunications: Réseaux embarqués et Objets connectés': 'M1 RT',
                           'M1 Sciences pour la mécanique des matériaux et des structure': 'M1 SMMS',
                           'M1 Water Engineering and Water Management': 'M1 WATER',
                           'M2 Dynamique des fluides, énergétique et transferts': 'M2 DET',
                           'M2 Fluids Engineering for Industrial Processes': 'M2 FLUIDS',
                           'M2 Industrial and Safety Engineering': 'M2 SAFETY',
                           'M2 Ingénierie de la durabilité – recherche et innovation en matériaux et structures': 'M2 ID-RIMS',
                           'M2 Réseaux et télécommunications : Réseaux embarqués et Objets connectés': 'M2 RT',
                           'M2 Sciences pour la mécanique des matériaux et des structure': 'M2 SMMS',
                           'M2 Water Engineering and Water Management': 'M2 WATER'}

# index dans les fichiers excel des etudiants
idx_etudiant_id = 0
idx_etudiant_nom = 1
idx_etudiant_prenom = 2
idx_etudiant_ordre = 9
idx_etudiant_choix = 12
idx_etudiant_filiere = 6
idx_etudiant_classement = 7

# index dans le fichier excel des departs
idx_depart_nom_univ = 4
idx_depart_specialite = 5
idx_departs_nombre = 2

# constantes
PAS_DE_PROGAMME_ADEQUAT = -1000
ND = 10

# constantes choix
PAS_DE_PROGRAMME = 0
PAS_DE_PLACE = 1
AFFECTATION = 2
