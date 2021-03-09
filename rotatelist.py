def rotatelist(l,k):
  while k>0:
    l=l[1:len(l)]+[l[0]]
    k=k-1
  return(l)
