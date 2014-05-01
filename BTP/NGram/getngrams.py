#!/usr/bin/env python
from ast import literal_eval
from pandas import DataFrame  # http://github.com/pydata/pandas
import re
import requests               # http://github.com/kennethreitz/requests
import subprocess
import sys

corpora = dict(eng_us_2012=17, eng_us_2009=5, eng_gb_2012=18, eng_gb_2009=6,
               eng_2012=15, eng_2009=0, eng_fiction_2012=16, eng_fiction_2009=4, 
	       eng_1m_2009=1)


def getNgrams(query, corpus, startYear, endYear, smoothing, caseInsensitive):
    params = dict(content=query, year_start=startYear, year_end=endYear,
                  corpus=corpora[corpus], smoothing=smoothing,
                  case_insensitive=caseInsensitive)
    if params['case_insensitive'] is False:
        params.pop('case_insensitive')
    if '?' in params['content']:
        params['content'] = params['content'].replace('?', '*')
    if '@' in params['content']:
        params['content'] = params['content'].replace('@', '=>')
    req = requests.get('http://books.google.com/ngrams/graph', params=params)
    res = re.findall('var data = (.*?);\\n', req.text)
    data = {qry['ngram']: qry['timeseries'] for qry in literal_eval(res[0])}
    df = DataFrame(data)
    df.insert(0, 'year', range(startYear, endYear+1))
    return req.url, params['content'], df

def runQuery(argumentString, at):
    arguments = argumentString.split()
    query = ' '.join([arg for arg in arguments if not arg.startswith('-')])
    if '?' in query:
        query = query.replace('?', '*')
    if '@' in query:
        query = query.replace('@', '=>')
    params = [arg for arg in arguments if arg.startswith('-')]
    corpus, startYear, endYear, smoothing = 'eng_2012', 1800, 2000, 3
    printHelp, caseInsensitive, allData = False, False, False
    toSave, toPrint, toPlot = True, True, False

    url, urlquery, df = getNgrams(query, corpus, startYear, endYear, smoothing, caseInsensitive)

    if toPrint:
        print ','.join(df.columns.tolist())
        for row in df.iterrows():
            try:
                print '%d,' % int(row[1].values[0]) + \
                      ','.join(['%.12f' % s for s in row[1].values[1:]])
            except:
                print ','.join([str(s) for s in row[1].values])
    queries = ''.join(urlquery.replace(',', '_').split())
    if '*' in queries:
        queries = queries.replace('*', 'WILDCARD')
    if caseInsensitive is True:
        word_case = 'caseInsensitive'
    else:
        word_case = 'caseSensitive'

    filename = 'ngram_data-%d.csv' % (at)

    if toSave:
        for col in df.columns:
            if '&gt;' in col:
                df[col.replace('&gt;', '>')] = df.pop(col)
        df.to_csv(filename, index=False)
        print 'Data saved to %s' % filename

def linesplit():
	splitLen = 12         # 12 lines per file
	outputBase = 'ngrams-' 

	input = open('firstoutput.txt', 'r').read().split('\n')

	at = 1
	for lines in range(0, len(input), splitLen):
    		outputData = input[lines:lines+splitLen]
    		output = open(outputBase + str(at) + '.txt', 'w')      #writing the sliced lines to a new file
    		at += 1
    		output.write(',\n'.join(outputData))
    		output.close()
	return at

if __name__ == '__main__':
    argumentString = ' '.join(sys.argv[1:])
    end = linesplit()
    print end
    for at in range(1, end):
	output = open('ngrams-' + str(at) + '.txt').read() 
        runQuery(output, at)
	at = at + 1
