def wkey():
	fname = input('Enter a file name: ')
	fhand = open(fname)
	wdic={}
	for line in fhand:
		line=line.rstrip()
		words=line.split()
		wdic= {i:words[i] for i in range(len(words)-1)}
		print(wdic)
