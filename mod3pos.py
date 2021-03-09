def mod3pos(l):
  if len(l) == 0:
    return([])
  else:
    return([l[0]] + mod3pos(l[3:]))
