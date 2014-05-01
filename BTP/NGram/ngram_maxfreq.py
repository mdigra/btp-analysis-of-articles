#Gives the year corresponding to the word when it was maximun used.

import csv

def generate_list(file_path):
    data_list=None   #local variable    
    try:
        file_obj = open(file_path,'r')
        try:
            gen = (line.split(',') for line in file_obj)  #generator, to generate one line each time until EOF (End of File)
            for j,line in enumerate(gen):
                if not data_list:

                    data_list = [[] for i in range(len(line))]
                    if line[-1].find('\n'):
                        line[-1] = line[-1][:-1]           #to remove last list element's '\n' character

                #convert numbers from string to float, and leave others as strings only
                for i,l in enumerate(line):
                    if i >=2 and j >= 1:
                        data_list[i].append(float(l))
                    else:            
                        data_list[i].append(l)
        except IOError, io_except:
            print io_except
        finally:
            file_obj.close()
    except IOError, io_exception:
        print io_exception

    return data_list

def get_maxvalue(file_path):
    data_list = generate_list(file_path)
    re = []                       #list to store results in tuple formet as follow [(year, word)]
    if data_list:
        for i,d in enumerate(data_list):
            if i >= 1:
                m = max(data_list[i][1:])       #max_value for the word
                idx = data_list[i].index(m)     #getting index of max_value in the list
                yr = data_list[0][idx]          #getting year by using index of max_value in list
                word = data_list[i][0]          #getting corresponding word
                re.append((yr,word))
	return re

if __name__ == '__main__':
    import getngrams
    end = getngrams.linesplit()
    #print end
    out = open('ngram_maxvalues.csv','wb')
    csv_out1=csv.writer(out)
    csv_out1.writerow(['YEAR','WORD'])
    for at in range(1, end):
	file_path = 'ngram_data-' + str(at) + '.csv'
        re = get_maxvalue(file_path)
	#print re
	csv_out=csv.writer(out)
       	for row in re:
       		csv_out.writerow(row)
	at = at + 1
