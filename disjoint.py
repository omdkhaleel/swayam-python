def disjointlist(l1,l2):
  s1 = set(l1)
  s2 = set(l2)
  return(s1 & s2 == set())
