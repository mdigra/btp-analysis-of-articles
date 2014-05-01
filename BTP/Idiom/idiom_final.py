import nltk.data
import re

Input = open('input.txt')
input1 = Input.read()
input1 = input1.lower()

Idiom = open('idiom_list.txt')
Idiom1 = Idiom.read()
Idiom1 = Idiom1.lower()

sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')

idiom_list  = ((sent_detector.tokenize(Idiom1.strip())))
#print idiom_list
 
input_list  = ((sent_detector.tokenize(input1.strip())))
print input_list

def compare(): 
	Output = open('idiom_results.txt', 'wb')
#Output.write("The following idioms are used...... \n\n")
	for i in input_list:
		for j in idiom_list:
			match = re.search(j, i)
			if match:
				#count =
				Output.write(i+"\n")
				#print i

if __name__ == '__main__':
	compare()
