def matched(s):
  ocount=0
  ccount=0
  plist=[]
  l=len(s)
  for i in range(0,l):
    if s[i]=="(":
      ocount=ocount+1
      plist=plist+[s[i]]
    elif s[i]==")":
      ccount=ccount+1
      plist=plist+[s[i]]
  if plist==[] or plist[0]!=")" and ocount==ccount:
    return (True)
  else:
    return (False)

  # One more way
  def matched(s):
  nesting = 0
  for c in s:
    if c == '(':
      nesting = nesting + 1
    elif c == ')':
      nesting = nesting - 1
    if nesting < 0:
      return(False)
  return(nesting == 0)
