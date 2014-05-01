import nltk.data
from nltk.corpus import wordnet as wn
from GetDependencyParse import dependency_parse
import re


def detect_metaphor(sentence):
    dep_parse_output, noun_list = dependency_parse(sentence.lower())

    nsubj_pairs = (ns_parse[1:] for ns_parse in filter(lambda dp: dp[0] == "nsubj" and dp[1] in noun_list and dp[2] in noun_list, dep_parse_output))
    for pair in nsubj_pairs:
	return "{}".format(pair)
    if nsubj_pairs == None:
       	print "No Noun-Noun pairs detected."

def get_input():
    fp = open('input.txt', 'r')

    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    data = fp.read()
    out = open('output.txt', 'w')
    out.write('\n'.join(tokenizer.tokenize(data)))

if __name__ == "__main__":
    get_input()
    
    Input = open('output.txt', 'r')
    text = Input.readlines()
    for line in text:
	print line
	#Output = open('readlines.txt', 'wb')
	#Output.write(line)

    	x = detect_metaphor(line)
	if x == None:
		continue
	print x
	with open("pairword.txt", "a") as myfile:
	    line = re.sub('[],[\''']', '', x)
    	    myfile.write(line+"\n")
