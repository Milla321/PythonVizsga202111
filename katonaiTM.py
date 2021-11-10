#
"""Kérje be egy elektronikai eszköz üzemi hőmérsékletének alsó és felső határát. Ha az alsó határ < 25 °C akkor és a felső határ > 85 °C, akkor katonai célokra megfelel az eszköz.  Mentse katonaiTM.py néven
"""

##  Talián Lászlóné, 2021-10-19, SZOFT I/1//2/E

print('Talián Lászlóné, 2021-10-19, SZOFT I/1//2/E')
print('Ha az elektronikai eszköz alsó határa < 25 °C  és a felső határa > 85 °C, akkor katonai célokra megfelel az eszköz')
print('A 002 feladat megoldása')


minÉrték = int (input ("also hatar:" ) )
maxÉrték = int (input ("felso hatar:" ) )

if minÉrték < 25 and maxÉrték > 85:
	print (" katonai célokra megfelel az eszköz")
	

else:
	print (" katonai célokra NEM felel meg az eszköz" )
