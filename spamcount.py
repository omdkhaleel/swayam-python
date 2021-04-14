def spamcount():
	fname=input('Enter the file name: ')
	fhand=open(fname)
	count=0
	spv=0
	for line in fhand:
		line=line.strip()
		if line.startswith('X-DSPAM-Confidence'):
			count=count+1
			cp=line.find(':')
			fv=float(line[cp+1:-1])
			spv=spv+fv
	avg=spv/count
	print('Average spam confidence: ', avg)
