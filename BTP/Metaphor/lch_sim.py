import nltk
from nltk.corpus import wordnet as wn
import re

Input = open('pairword.txt', 'r')
text = Input.readlines()

Input1 = open('pairword1.txt', 'w')

count = 0
for word2 in text:
        word2 = word2.strip()
	print word2
	text1 = nltk.word_tokenize(word2)
	print text1
	#print len(text1)

	wordFromList1 = wn.synsets(text1[0])	   #synset list
	#print wordFromList1
	shabd1 =  wordFromList1[0] 
	#print shabd1
	
	wordFromList2 = wn.synsets(text1[1])
	                    
	shabd2 =  wordFromList2[0]
	s = shabd1.lch_similarity(shabd2)
	print s
	if s < 1.5:
		count = count + 1
		Input1.write(word2+"\n")
	print count
	
	
