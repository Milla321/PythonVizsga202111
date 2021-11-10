
"""Feladat: „A” feladatsor 2. szintű feladat.  Írjon programot amely kiszámolja egy téglatest térfogatát. Kérje be a felhasználótól a három oldal adatot.  Mentés Talian_Milla_teglatest.py néven.
"""

## Talián Lászlóné, 2021-11-05, SZOFT I/1//2/E

print('Talián Lászlóné, 2021-11-05, SZOFT I/1//2/E')
print('Téglatest térfogata')


astr =input("Oldala (cm)? ")
bstr = input("Oldalb (cm)? ")
cstr = input("Oldalc (cm)? ")

a =float(astr)
b =float(bstr)
c =float(cstr)
terfogat =a*b*c

print ("Téglatest térfogata:: ", round(terfogat,2)," cm3")

