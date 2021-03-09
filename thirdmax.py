def thirdmax(l):
  (mymax,mysecondmax,mythirdmax) = (0,0,0)
  for i in range(len(l)):
    if l[i] > mymax:
      (mymax,mysecondmax,mythirdmax) = (l[i],mymax,mysecondmax)
    elif l[i] > mysecondmax:
      (mysecondmax,mythirdmax) = (l[i],mysecondmax)
    elif l[i] > mythirdmax:
      mythirdmax = l[i]
  return(mythirdmax)
