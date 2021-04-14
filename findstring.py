def fndstr():
  fname=input('Enter the file name: ')
  fstr=input('Enter the searching word: ')
  fhand=open(fname)
  for iine in fhand:
    line=line.rstrip()
    if line.find(fstr)==-1: continue
    print(line)  
