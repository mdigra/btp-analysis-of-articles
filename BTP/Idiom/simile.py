import nltk
import re

Input = open('input.txt')
text = Input.read()
text = text.lower()

sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
 
input_list  = ((sent_detector.tokenize(text.strip())))

def text_len():
	#print len(input_list)
	return len(input_list)

def compare():
	Output = open('similes.txt', 'wb')
	for i in input_list:
		if re.search("(.*) as (.*) as (.*)", i) or re.search("(.*) resembles (.*)", i) or re.search("(.*) like (.*)", i):
			Output.write(i+"\n")
			print i

def simile_list():
	Input = open('similes.txt')
	text = Input.read()
	sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')

	text  = ((sent_detector.tokenize(text.strip())))
	return len(text)

def percent_simile(a, b):
	percent = float(a)/b * 100
	return percent

if __name__ == '__main__':
	a = text_len()
	compare()
	b = simile_list()
	print a, b
	c = percent_simile(b, a)
	print "simile_percentage  " + str(c)
	rat = open('rating.txt', 'w')
	rat.write(str(c)+"\n")
