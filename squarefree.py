import math
def squarefree(n):
  for i in range(2,1+math.ceil(math.sqrt(n))):
    if n%(i*i) == 0:
      return(False)
  return(True)
