#!/usr/bin/env python
import re
import nltk
from nltk.corpus import stopwords
from nltk.probability import FreqDist

DATA = open("input.txt").read()
DATA = DATA.lower()
#print DATA
l = re.findall(r"[\w']+", DATA)
stop = stopwords.words('english')
#print l

m = [i for i in l if i not in stop]
fdist5 = FreqDist(m)
no_dupli = sorted([w for w in set(m) if len(w) > 3 ])
no_integers = [x for x in no_dupli if not (x.isdigit() or x[0] == '-' and x[1:].isdigit())]
#print no_integers

y = open('firstoutput.txt', 'wb')
for i in no_integers:
	word = i + "\n"
	y.write(word)
	




