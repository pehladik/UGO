__author__ = 'pehladik'

from TableauDepart import TableauDepart

tabdep = TableauDepart()

tabdep.lectureTableau(u'./documents/depart.xlsx')

ae = 0
ir = 0
for u in tabdep.listeUniversite:
    for p in u.listeDesProgrammes:
        print (p.listeDesFilieres)
        for f in p.listeDesFilieres:
            if f == u'AE':
                ae += 1
            if f == u'IR':
                ir += 1
    print(u)

print(ir)
print(ae)