#Determines which year is dominant and helps to decide whether article will have high rating or low. 

import csv

myfile = csv.reader(open('ngram_maxvalues.csv'))

header1 = myfile.next()
count = 0
count1 = 0
count2 =0

for YEAR, WORD in myfile:
	if YEAR >= '1800' and YEAR <= '1899':
		print "1800s\t"+ WORD
		count = count + 1
	elif YEAR >= '1900' and YEAR <= '2000':
		print "1900s\t"+ WORD
		count1 = count1 + 1
	"""else:
		print "2000s\t"+ WORD
		count2 = count2 + 1"""
print "No of 1800 words: %d" % count
print "No of 1900 words: %d" % count1
total = count+count1
per = float(count)/total * 100
per1 = float(count1)/total * 100
#print per
def compare():
	if count > count1 :
		print "\nThis article predominantly contains words from 1800's."
		print "%centile of 1800's words is: " + str(per) + "\n"	
		return per
	else:
		print "\nThis article predominantly contains words from 1900's."
		print "Percentile of 1900's words is: " + str(per1) + "\n"
		return per1

if __name__ == '__main__':
	c = compare()
	rat = open('rating2.txt', 'w')
	rat.write(str(c)+"\n") 
