import os

pathname3 = os.path.join("Metaphor", "rating3.txt")
pathname2 = os.path.join("NGram", "rating2.txt")
pathname1 = os.path.join("Idiom", "rating1.txt")
pathname = os.path.join("Idiom", "rating.txt")

P3 = open(pathname3)
P3 = P3.read()
print P3

#P2 = open(pathname2)
#P2 = P2.read()
#print P2

P1 = open(pathname1)
P1 = P1.read()
print P1

P = open(pathname)
P = P.read()
print P

P2 = 70.31
#P1 = 6.35
#P = 2.0

if all ([P2 > '60', P > '3.5', P1 > '0.1', P3 > '1.0']):
	print "Good Article, as it contains idioms, simile & metaphor along with present era words." 
else:
	print " Article is lacking one of the key parametes, needs improvement."



