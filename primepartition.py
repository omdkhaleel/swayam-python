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

# One more way
def factors(n):
  factorlist = []
  for i in range(1,n+1):
    if n%i == 0:
      factorlist.append(i)
  return(factorlist)

def prime(n):
  return(factors(n)==[1,n])

def primepartition(n):
  for i in range(1,n//2+1):
    if prime(i) and prime(n-i):
      return(True)
  return(False)
