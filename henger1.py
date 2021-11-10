

# Talián Milla
# 2020.10.20
# Esti szoft.

import math

print("Talián Milla, 2020.10.20, Esti szoftver")

print("Henger térfogata számitása")


sugár=float(input('sugár: '))
magasság=float(input('magasság: '))

térfogat = math.pow(sugár,2)* math.pi * magasság

print("Henger térfogata:", '% .2f' % térfogat, "cm3")

Vashengersúlya = térfogat * 7.8
print("Vashenger súlya:", '% .2f' % Vashengersúlya, "g")

Fahengersúlya = térfogat * 0.7
print("Fahenger súlya:", '% .2f' % Fahengersúlya, "g")





