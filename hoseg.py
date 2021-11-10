
"""Feladat 002. Írjon programot, amely bekéri két dolgozat elért pontszámait. A bekért pontszámokat a program átlagolja. Írjuk ki azt is, ki tért el leginkább az átlagtól. 
Mentés: hosseg
"""

##  Talián Lászlóné, 2021-01-17, SZOFT I/1/E

print('Talián Lászlóné, 2021-01-17, SZOFT I/1/E')
print('A 002 feladat megoldása')
print('.........................')
print('Agazati 002 mintafeladat megoldása')

print('Hőmérsékletek:')

def fagy(ho):
		if int (ho) < 0:
			return True
		else:
			return False
		
ho = ''
while ho != 'vége':
	ho = input('Hő: ')
	if ho != 'vége':
		if fagy(int (ho)):
			print('Fagy volt')
		else:
				print('Nem volt fagy')
