
"""Feladat: „B” feladatsor 2. szintű feladat.  Írjon programot amely kiszámolja egy háromszög területét. Kérje be a felhasználótól a három oldal értékét.  Mentés: Talian_Milla_haromszog.py néven.
"""

## Talián Lászlóné, 2021-11-05, SZOFT I/1//2/E

print('Talián Milla, 2021-11-05, SZOFT I/1//2/E')
print('Háromszög kerülete') 
print('Háromszög területe')

print('Feladat 2. „B” feladatsor megoldása')
print('.........................')

print("Szerkeszthető háromszög területe")	

oldalA= int(input('Kérem az A oldalt:'))
oldalB= int(input('Kérem az B oldalt:'))
oldalC= int(input('Kérem az C oldalt:'))

import math
kerulet = oldalA+oldalB+oldalC #kerület 
print('Háromszög kerülete: ', round(kerulet ,2)," cm")
s=(oldalA+oldalB+oldalC)/2   #kerület fele
terulet = math.sqrt(s*(s-oldalA)*(s-oldalB)*(s-oldalC))

if(oldalA+oldalB>oldalC and                           
   oldalA+oldalC>oldalB and
   oldalB+oldalC>oldalA):
	print('Háromszög területe: ', round(terulet,2)," cm2")
	
else:
    print ("nem szerkeszthető háromszög")
    

