"""Feladat: „B” feladatsor 1. szintű feladat.  Írjon programot amely megvizsgálja három tehenészeti telephely egy hónapos tejhozamát és  eldönti, hogy kell -e a hozam növelése érdekében több tehenet vásárolni.  Mentse Talian_Milla_tejAtlag.py néven.
"""

##  Talián Milla, 2021-11-05, SZOFT I/1//2/E

print("Feladat: „B” feladatsor 1. szintű feladat") 

print("Talián Milla, 2021-11-05, SZOFT I/1//2/E")

print("Három tehenészeti telephely egy hónapos tejhozam atlaga")

tejhozam01 = 452.35
tejhozam02 = 628.45
tejhozam03 = 553.0

tejhozamAverage = ( tejhozam01 + tejhozam02 + tejhozam03 )/3 

if( tejhozamAverage < 500 ):
	print( "Az Az  átlagtejhozam {:^10.3f) liter, tehenet kell  vásárolni" .format( tejhozamAverage )) 
else: 
	print( "Az  átlagtejhozam {:^10.3f} liter, nem kell tehenet vásárolni" .format( tejhozamAverage )) 

