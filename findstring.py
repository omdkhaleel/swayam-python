def fndstr():
  fhand=open('mbox.txt')
  for iine in fhand:
    line=line.rstrip()
    if line.find('@github.io')==-1: continue
    print(line)  
