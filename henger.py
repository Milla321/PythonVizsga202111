
# -*- coding: ISO-8859-2 -*-

from math import *
rstr =input("Sugár (cm)? ")
mstr = input("Magasság (cm)? ")
r =float(rstr)
m =float(mstr)
terf =r *r * pi *m
vas =terf * 7.8
fa =terf * 0.7
print ("Térfogat: ",round(terf,2)," cm3")
print ("Vashenger: ",round(vas,2)," g")
print ("Fahenger: ",round(fa,2)," g")
