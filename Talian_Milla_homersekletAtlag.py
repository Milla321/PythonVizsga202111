"""Feladat: „A” feladatsor 1. szintű feladat.  Írjon programot amely megvizsgálja három nap átlaghőmérsékletét és eldönti, hogy kell-e fűteni. Csak 15 fok átlag alatt kell elindítani a fűtést.   Mentés Talian_Milla_homersekletAtlag.py néven.
"""

##  Talián Milla, 2021-11-05, SZOFT I/1//2/E

print("Feladat: „A” feladatsor 1. szintű feladat") 

print("Talián Milla, 2021-11-05, SZOFT I/1//2/E")

print("Három nap átlaghőmérséklete")


homer01 = 11.4
homer02 = 18.2
homer03 = 16.0 
homerAverage = ( homer01 + homer02 + homer03 ) / 3 
if(  homerAverage < 15 ):
	print( "Az átlaghőmérséklet {:^10.3f}  fok, indítsa el a  fűtést." .format( homerAverage)) 
else: 
	print( "Az átlaghőmérséklet {:^10.3f} fok, nem kell fűteni." .format( homerAverage )) 

