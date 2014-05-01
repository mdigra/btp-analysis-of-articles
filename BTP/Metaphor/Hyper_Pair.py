import nltk
from nltk.corpus import wordnet as wn
import re

Input = open('pairword1.txt', 'r')
text = Input.readlines()

count = 0
for word2 in text:
        word2 = word2.strip()
	print word2
	text1 = nltk.word_tokenize(word2)
	#print text1
	#print len(text1)

	wordFromList1 = wn.synsets(text1[0])	   #synset list
	shabd1 =  wordFromList1[0] 

	hyp1 = lambda s:s.hypernyms()		   #hypernyms
	hyper_list1 = list(shabd1.closure(hyp1))

	path1 = shabd1.hypernym_paths()
	print len(path1)
	elements_1 = [synset.name for synset in path1[0]]
	print elements_1
	elements_1 = [x for x in elements_1 if ('abstraction.n.06') not in x]
	elements_1 = [x for x in elements_1 if ('entity.n.01') not in x]
	elements_1 = [x for x in elements_1 if ('physical_entity.n.01') not in x]
	elements_1 = [x for x in elements_1 if ('whole.n.02') not in x]
	print ".......................---------------------------"
	print elements_1
	print "\n"
	elements1_1 = []
	array_ele1  = []
	array_ele2 = []
	if len(path1) > 1:
		for i in range(1, len(path1)):
			elements1_1 = [synset.name for synset in path1[i]]
			print elements1_1

		#merged_elements = list(set(elements_1) | set(elements1_1))
		#print "---------------**********************-----------"
		#print merged_elements
			print i
			elements1_1 = [x for x in elements1_1 if ('abstraction.n.06') not in x]
			elements1_1 = [x for x in elements1_1 if ('entity.n.01') not in x]
			elements1_1 = [x for x in elements1_1 if ('physical_entity.n.01') not in x]
			elements1_1 = [x for x in elements1_1 if ('whole.n.02') not in x]
			print elements1_1
			print "\n"
			for item in elements1_1:
				if item not in array_ele1:
					array_ele1.append(item)
		print " .....................MERGED path arrays......................"
		print array_ele1
	#print elements1_1
	if not set(elements1_1):
		merged_elements = elements_1
	else:
		merged_elements = list(set(elements_1) | set(array_ele1))
	print "--------------------******************************----------------------"
	print merged_elements
	#break

################################################################################################################################################

	wordFromList2 = wn.synsets(text1[1])
	                    
	shabd2 =  wordFromList2[0]                   #synset list
	#del hyper_list1[-1], hyper_list1[n1-2], hyper_list1[n1-3], hyper_list1[n1-4]

	hyp2 = lambda s:s.hypernyms()
	hyper_list2 = list(shabd2.closure(hyp2))
	path2 = shabd2.hypernym_paths()
	print len(path2)
	elements_2 = [synset.name for synset in path2[0]]
	print "\n................Second Set..............................."
	print elements_2

	elements_2 = [x for x in elements_2 if ('abstraction.n.06') not in x]
	elements_2 = [x for x in elements_2 if ('entity.n.01') not in x]
	elements_2 = [x for x in elements_2 if ('physical_entity.n.01') not in x]
	elements_2 = [x for x in elements_2 if ('whole.n.02') not in x]
	print "-------------------------------------"
	print elements_2

	elements1_2 = []
	if len(path2) > 1:
		for i in range(1, len(path2)):
			elements1_2 = [synset.name for synset in path2[i]]
			print elements1_2

			print i
			elements1_2 = [x for x in elements1_2 if ('abstraction.n.06') not in x]
			elements1_2 = [x for x in elements1_2 if ('entity.n.01') not in x]
			elements1_2 = [x for x in elements1_2 if ('physical_entity.n.01') not in x]
			elements1_2 = [x for x in elements1_2 if ('whole.n.02') not in x]
			print elements1_2
			print "\n"
			for item in elements1_2:
				if item not in array_ele2:
					array_ele2.append(item)
		print " .....................MERGED path arrays......................"
		print array_ele2
		
	#print elements1_2
	if not set(elements1_2):
		merged_elements_2 = elements_2
	else:
		merged_elements_2 = list(set(elements_2) | set(array_ele2))
	print "--------------------**********************************************************"
	print merged_elements_2
	print "\n"

	t = list(set(merged_elements) & set(merged_elements_2))
	print t 
	if not t:	
		count = count + 1
	#print "\n"
	print count
	"""for i in merged_elements:
		for j in merged_elements_2:
			if i == j:
				count = count + 1
				print j"""


Input = open('input.txt')
input1 = Input.read()
input1 = input1.lower()

sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
input_list  = ((sent_detector.tokenize(input1.strip())))
text_len =  len(input_list)
print text_len
per = float(count)/text_len * 100
print per
rat = open('rating3.txt', 'w')
rat.write(str(per)+"\n") 
