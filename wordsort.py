def uniq():
	fname=input('Enter the file name: ')
	fhand=open(fname)
	wlist=[]
	for line in fhand:
		line=line.strip()
		word=line.split()
		for x in word:
			if x in wlist: continue
			else:
				wlist.append(x)
	print(sorted(wlist))
