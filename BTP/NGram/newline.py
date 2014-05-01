with open('input.txt','r+' ) as f:
	clean = f.read().replace('\n', ' ').replace('\r', ' ')
	f.seek(0)
	f.write(clean)
	f.truncate()



