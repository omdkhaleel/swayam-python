def fwcount():
	fname=input('Enter file name: ')
	try:
		fhand=open(fname)
		counts=dict()
		for line in fhand:
			words=line.split()
			for word in words:
				if word not in counts:
					counts[word]=1
				else:
					counts[word]=count+1
		print(counts)
	except:
		print('File cannot be opened')
