import nltk.data
import os.path

Input = open('input.txt')
input1 = Input.read()
input1 = input1.lower()

sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
input_list  = ((sent_detector.tokenize(input1.strip())))

count = open('idiom_results.txt')
count1 = count.read()
idiom_list  = ((sent_detector.tokenize(count1.strip())))

def text_len():
	#print len(input_list)
	return len(input_list)

def idiom_len():
	if os.path.getsize("idiom_results.txt") == False:
		return 0	
	else:
		#print len(idiom_list)
		return len(idiom_list)

def percent_idiom(a, b):
	percent = float(a)/b * 100
	return percent

if __name__ == '__main__':
	a = text_len()
	print a
	b = idiom_len()
	print b
	c = percent_idiom(b, a)
	print "idiom_percentage  " + str(c)
	rat = open('rating1.txt', 'w')
	rat.write(str(c)+"\n") 
