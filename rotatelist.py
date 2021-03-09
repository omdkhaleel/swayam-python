def rotatelist(l,k):
  while k>0:
    l=l[1:len(l)]+[l[0]]
    k=k-1
  return(l)

# One more way
def rotatelist(l,k):
  retlist = l[:]

  if k <= 0:
    return(retlist)

  for i in range(1,k+1):
    retlist = retlist[1:] + [retlist[0]]
  return(retlist)
