def isprime(m):
    for i in range(2,m):
        if m%i==0:
            return(False)
    else:
        return(True)
def primepartition(m):
  if m < 0:
    return(False)
  else:
    primelist = []
    for i in range (1,(m//2)+1):
      if isprime(i):
        if isprime(m-i):
          primelist = primelist + [i]+[m-i]
    return(primelist!=[])
