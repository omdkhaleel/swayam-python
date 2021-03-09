def decreasing(l):
  if l==[] or len(l) == 1:
    return(True)
  else:
    return(
       # Complete the recursive call below this line
           l[0] > l[1] and decreasing(l[1:])
       # Complete the recursive call above this line
    )
