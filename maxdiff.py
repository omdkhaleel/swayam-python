def maxdifference(l):
  maximum = {}
  minimum = {}
  for (name,score) in l:
    try:
      maximum[name] = max(maximum[name],score)
      minimum[name] = min(minimum[name],score)
    except KeyError:
      maximum[name] = score
      minimum[name] = score
      
  maxdiff = -1
  maxlist = []

  for name in maximum.keys():
    thisdiff = maximum[name] - minimum[name]
    if thisdiff == maxdiff:
      maxlist.append(name)
    if thisdiff > maxdiff:
      maxdiff = thisdiff
      maxlist = [name]
      
  return(sorted(maxlist))
